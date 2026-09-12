import telebot
from telebot import types
import sqlite3

# ---------------------------------------------------------
# الإعدادات الأساسية
# ---------------------------------------------------------
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # حط التوكن بتاعك هنا
DEVELOPER_ID = 123456789           # حط الـ ID بتاعك هنا

bot = telebot.TeleBot(API_TOKEN)

# ---------------------------------------------------------
# التعامل مع قاعدة البيانات
# ---------------------------------------------------------
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # جدول الأدمنية
    conn.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
    ''')
    # جدول الحالات
    conn.execute('''
        CREATE TABLE IF NOT EXISTS user_states (
            user_id INTEGER PRIMARY KEY,
            state TEXT
        )
    ''')
    # إضافة المطور كأدمن تلقائياً
    conn.execute('INSERT OR IGNORE INTO admins (user_id, username) VALUES (?, ?)', (DEVELOPER_ID, 'Developer'))
    conn.commit()
    conn.close()

init_db()

# ---------------------------------------------------------
# الدوال المساعدة
# ---------------------------------------------------------
def is_admin(user_id):
    conn = get_db_connection()
    admin = conn.execute('SELECT user_id FROM admins WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    return admin is not None

def set_state(user_id, state):
    conn = get_db_connection()
    conn.execute('INSERT OR REPLACE INTO user_states (user_id, state) VALUES (?, ?)', (user_id, state))
    conn.commit()
    conn.close()

def get_state(user_id):
    conn = get_db_connection()
    res = conn.execute('SELECT state FROM user_states WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    return res['state'] if res else None

def clear_state(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM user_states WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

# ---------------------------------------------------------
# الأوامر الرئيسية والواجهات
# ---------------------------------------------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    clear_state(message.from_user.id)
    markup = types.InlineKeyboardMarkup()
    if is_admin(message.from_user.id):
        markup.add(types.InlineKeyboardButton("⚙️ قسم الأدمن", callback_data="section_admin"))
    bot.send_message(message.chat.id, "أهلاً بك في البوت!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "section_admin")
def admin_section(call):
    if not is_admin(call.from_user.id):
        return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🛡️ إدارة الأدمنية", callback_data="admin_admins"))
    bot.edit_message_text("⚙️ لوحة التحكم:", call.message.chat.id, call.message.message_id, reply_markup=markup)

# ---------------------------------------------------------
# قسم إدارة الأدمنية (عرض - إضافة - حذف)
# ---------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == "admin_admins")
def admin_manage_admins(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.answer_callback_query(call.id, "❌ غير مصرح لك!", show_alert=True)
        return
    
    conn = get_db_connection()
    admins = conn.execute("SELECT user_id, username FROM admins").fetchall()
    conn.close()
    
    text = "🛡️ <b>قائمة الأدمنية الحاليين:</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    
    for adm in admins:
        text += f"👤 ID: <code>{adm['user_id']}</code> | @{adm['username'] or 'بدون'}\n"
        if adm['user_id'] != DEVELOPER_ID:
            markup.add(types.InlineKeyboardButton(f"❌ حذف {adm['username'] or adm['user_id']}", callback_data=f"admin_remove_admin_{adm['user_id']}"))
            
    markup.add(types.InlineKeyboardButton("➕ إضافة أدمن جديد", callback_data="admin_add_admin"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="section_admin"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_admin")
def admin_add_admin_start(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.answer_callback_query(call.id, "❌ غير مصرح لك!", show_alert=True)
        return
    
    set_state(user_id, 'admin_add_admin')
    bot.send_message(call.message.chat.id, "👤 أرسل الآن الـ ID الرقمي للأدمن الجديد:")

@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_remove_admin_"))
def admin_remove_admin_handler(call):
    user_id = call.from_user.id
    if not is_admin(user_id):
        bot.answer_callback_query(call.id, "❌ غير مصرح لك!", show_alert=True)
        return
    
    target_id = int(call.data.split("_")[-1])
    if target_id == DEVELOPER_ID:
        bot.answer_callback_query(call.id, "❌ لا يمكنك حذف المطور الأساسي!", show_alert=True)
        return
        
    conn = get_db_connection()
    conn.execute("DELETE FROM admins WHERE user_id = ?", (target_id,))
    conn.commit()
    conn.close()
    
    bot.answer_callback_query(call.id, "✅ تم حذف الأدمن بنجاح.")
    admin_manage_admins(call)

# ---------------------------------------------------------
# استقبال مدخلات النثر (إضافة أدمن جديد)
# ---------------------------------------------------------
@bot.message_handler(func=lambda msg: get_state(msg.from_user.id) == 'admin_add_admin')
def process_add_admin(message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        return
    
    input_text = message.text.strip().replace('@', '')
    
    if not input_text.isdigit():
        bot.reply_to(message, "❌ خطأ! أرسل ID رقمي صحيح فقط.")
        return
    
    new_admin_id = int(input_text)
    
    conn = get_db_connection()
    conn.execute("INSERT OR REPLACE INTO admins (user_id, username) VALUES (?, ?)", (new_admin_id, "Admin"))
    conn.commit()
    conn.close()
    
    clear_state(user_id)
    bot.reply_to(message, f"✅ تم إضافة الأدمن بنجاح:\nID: <code>{new_admin_id}</code>", parse_mode='HTML')

# ---------------------------------------------------------
# تشغيل البوت
# ---------------------------------------------------------
if __name__ == '__main__':
    bot.infinity_polling()
