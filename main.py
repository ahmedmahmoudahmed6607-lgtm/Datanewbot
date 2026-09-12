#!/usr/bin/env python3
# White Wolf t.me/j49_c
# channel t.me/bshshshkk

import telebot
import sqlite3
import os
import threading
import time
import random
import tempfile
import shutil
from datetime import datetime
from telebot import types

BOT_TOKEN = os.environ.get('BOT_TOKEN', '8463349327:AAEHCXtmznGBEhq41FPYH9Q1f6NPBvKdnIc')
DEVELOPER_ID = int(os.environ.get('DEVELOPER_ID', '7951916432'))

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

EMOJI_MAP = {
    '✅': '<tg-emoji emoji-id="6258259403200270844">✅</tg-emoji>',
    '☑️': '<tg-emoji emoji-id="4945049066271671758">☑️</tg-emoji>',
    '🔍': '<tg-emoji emoji-id="5965466792527666087">🔍</tg-emoji>',
    '🔎': '<tg-emoji emoji-id="5965466792527666087">🔎</tg-emoji>',
    '👤': '<tg-emoji emoji-id="5373020661574826232">👤</tg-emoji>',
    '📱': '<tg-emoji emoji-id="5834628314731387616">📱</tg-emoji>',
    '💳': '<tg-emoji emoji-id="5447453226498552490">💳</tg-emoji>',
    '🔗': '<tg-emoji emoji-id="5967301267549068409">🔗</tg-emoji>',
    '🎟': '<tg-emoji emoji-id="5785167918027250397">🎟</tg-emoji>',
    '🎟️': '<tg-emoji emoji-id="5785167918027250397">🎟️</tg-emoji>',
    '⚙️': '<tg-emoji emoji-id="5857054220179480029">⚙️</tg-emoji>',
    '➕': '<tg-emoji emoji-id="5857339990123486296">➕</tg-emoji>',
    '📋': '<tg-emoji emoji-id="5803363345113290876">📋</tg-emoji>',
    '🗑': '<tg-emoji emoji-id="5920209833071482745">🗑</tg-emoji>',
    '🗑️': '<tg-emoji emoji-id="5920209833071482745">🗑️</tg-emoji>',
    '❌': '<tg-emoji emoji-id="5796291784539639311">❌</tg-emoji>',
    '🛡': '<tg-emoji emoji-id="5920298756074379058">🛡</tg-emoji>',
    '🛡️': '<tg-emoji emoji-id="5920298756074379058">🛡️</tg-emoji>',
    '👥': '<tg-emoji emoji-id="6001388309853510348">👥</tg-emoji>',
    '🚫': '<tg-emoji emoji-id="5888789252493283486">🚫</tg-emoji>',
    '🔓': '<tg-emoji emoji-id="5998940732545571769">🔓</tg-emoji>',
    '➖': '<tg-emoji emoji-id="5280753674451175517">➖</tg-emoji>',
    '🔄': '<tg-emoji emoji-id="5976831692604709621">🔄</tg-emoji>',
    '💰': '<tg-emoji emoji-id="6037182124916740433">💰</tg-emoji>',
    '🎁': '<tg-emoji emoji-id="5976317950091598658">🎁</tg-emoji>',
    '🔙': '<tg-emoji emoji-id="5253743295141538873">🔙</tg-emoji>',
    '✨': '<tg-emoji emoji-id="5254001839287859496">✨</tg-emoji>',
    '📊': '<tg-emoji emoji-id="5935935761336505948">📊</tg-emoji>',
    '📢': '<tg-emoji emoji-id="5902385465390013835">📢</tg-emoji>',
    '🌐': '<tg-emoji emoji-id="5837128389424585193">🌐</tg-emoji>',
    '🧙': '<tg-emoji emoji-id="5803157577525106419">🧙</tg-emoji>',
    '📡': '<tg-emoji emoji-id="5836811137370297987">📡</tg-emoji>',
    '🌾': '<tg-emoji emoji-id="5981216003810400332">🌾</tg-emoji>',
    '🛠': '<tg-emoji emoji-id="5965466792527666087">🛠</tg-emoji>',
    '🛠️': '<tg-emoji emoji-id="5965466792527666087">🛠️</tg-emoji>',
    '👑': '<tg-emoji emoji-id="5319149831673887746">👑</tg-emoji>',
    '🆕': '<tg-emoji emoji-id="5857339990123486296">🆕</tg-emoji>',
    '📤': '<tg-emoji emoji-id="5920298756074379058">📤</tg-emoji>',
    '📥': '<tg-emoji emoji-id="5920415115328362511">📥</tg-emoji>',
    '📞': '<tg-emoji emoji-id="5373020661574826232">📞</tg-emoji>',
    '🏦': '<tg-emoji emoji-id="5803363345113290876">🏦</tg-emoji>',
    '💎': '<tg-emoji emoji-id="5254001839287859496">💎</tg-emoji>',
    '🔑': '<tg-emoji emoji-id="5785167918027250397">🔑</tg-emoji>',
    '🎫': '<tg-emoji emoji-id="5785167918027250397">🎫</tg-emoji>',
    '📌': '<tg-emoji emoji-id="5920298756074379058">📌</tg-emoji>',
    '📝': '<tg-emoji emoji-id="5314299563761222650">📝</tg-emoji>',
    '📈': '<tg-emoji emoji-id="5935935761336505948">📈</tg-emoji>',
    '📅': '<tg-emoji emoji-id="5314299563761222650">📅</tg-emoji>',
    '📦': '<tg-emoji emoji-id="5881760620117760960">📦</tg-emoji>',
    '🔢': '<tg-emoji emoji-id="5965466792527666087">🔢</tg-emoji>',
    '✏️': '<tg-emoji emoji-id="5314299563761222650">✏️</tg-emoji>',
    '🖨': '<tg-emoji emoji-id="5967617875358258757">🖨</tg-emoji>',
    '🖨️': '<tg-emoji emoji-id="5967617875358258757">🖨️</tg-emoji>',
    '🖼': '<tg-emoji emoji-id="5294079682365384341">🖼</tg-emoji>',
    '🖼️': '<tg-emoji emoji-id="5294079682365384341">🖼️</tg-emoji>',
    '⏳': '<tg-emoji emoji-id="5314299563761222650">⏳</tg-emoji>',
    '⏰': '<tg-emoji emoji-id="5314299563761222650">⏰</tg-emoji>',
    '🎉': '<tg-emoji emoji-id="5254001839287859496">🎉</tg-emoji>',
    '🔹': '<tg-emoji emoji-id="5967301267549068409">🔹</tg-emoji>',
    '⭐': '<tg-emoji emoji-id="5254001839287859496">⭐</tg-emoji>',
    '😎': '<tg-emoji emoji-id="5976308930660276596">😎</tg-emoji>',
    '💗': '<tg-emoji emoji-id="6043941205144771802">💗</tg-emoji>',
    '🎯': '<tg-emoji emoji-id="5965466792527666087">🎯</tg-emoji>',
    '📂': '<tg-emoji emoji-id="5881760620117760960">📂</tg-emoji>',
    '🗂': '<tg-emoji emoji-id="5881760620117760960">🗂</tg-emoji>',
    '🗂️': '<tg-emoji emoji-id="5881760620117760960">🗂️</tg-emoji>',
    '💲': '<tg-emoji emoji-id="6003691769533829755">💲</tg-emoji>',
    '⚠️': '<tg-emoji emoji-id="5999278377104578246">⚠️</tg-emoji>',
    '🔴': '<tg-emoji emoji-id="5999278377104578246">🔴</tg-emoji>',
    '🟢': '<tg-emoji emoji-id="4945049066271671758">🟢</tg-emoji>',
    '🔵': '<tg-emoji emoji-id="5967301267549068409">🔵</tg-emoji>',
    '💬': '<tg-emoji emoji-id="5314299563761222650">💬</tg-emoji>',
    '🧹': '<tg-emoji emoji-id="5920415115328362511">🧹</tg-emoji>',
    '⬆️': '<tg-emoji emoji-id="5920298756074379058">⬆️</tg-emoji>',
    '⬇️': '<tg-emoji emoji-id="5922681088534124293">⬇️</tg-emoji>',
    '🏷': '<tg-emoji emoji-id="5881760620117760960">🏷</tg-emoji>',
    '🏷️': '<tg-emoji emoji-id="5881760620117760960">🏷️</tg-emoji>',
    '📣': '<tg-emoji emoji-id="5902385465390013835">📣</tg-emoji>',
    '🎨': '<tg-emoji emoji-id="5254001839287859496">🎨</tg-emoji>',
}

EMOJI_IDS = [
    "4945049066271671758",
    "5965466792527666087",
    "5373020661574826232",
    "5967507756691757055",
    "5967301267549068409",
    "5785167918027250397",
    "5857054220179480029",
    "5857339990123486296",
    "5881760620117760960",
    "5920209833071482745",
    "5920415115328362511",
    "5920298756074379058",
    "5922681088534124293",
    "6001388309853510348",
    "5999278377104578246",
    "5998940732545571769",
    "6003691769533829755",
    "5280753674451175517",
    "5314299563761222650",
    "6037182124916740433",
    "5976317950091598658",
    "5976831692604709621",
    "5253743295141538873",
    "5254001839287859496",
]

E_STATS    = "5935935761336505948"
E_BCAST    = "5902385465390013835"
E_VODAFONE = "5834628314731387616"
E_WE       = "5837128389424585193"
E_NATERA   = "5316653334688446735"
E_ORANGE   = "5836714629455157161"
E_ETISALAT = "5836811137370297987"
E_TAMWEEN  = "5981216003810400332"
E_ORDERS   = "5907001756369296257"
E_REFERRAL = "5319070993254201336"
E_SUPPORT  = "5316653334688446735"
E_CONFIRM  = "5987615535146210396"
E_CANCEL   = "5330237710655306682"
E_BACK     = "6258259403200270844"

DATABASE_PATH = 'bot_database.db'

SERVICES = {
    'vodafone_data': {
        'name': 'سحب بيانات فودافون',
        'emoji': '📱',
        'price': 35.0,
        'section': 'vodafone',
        'service_code': 'vodafone_data',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'vodafone_vip': {
        'name': 'بيانات رقم مميز فودافون',
        'emoji': '💎',
        'price': 45.0,
        'section': 'vodafone',
        'service_code': 'vodafone_vip',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'vodafone_ownership': {
        'name': 'سحب ملكية سابقة 010',
        'emoji': '🔑',
        'price': 50.0,
        'section': 'vodafone',
        'service_code': 'vodafone_ownership',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards': {
        'name': 'سحب بطاقات 015',
        'emoji': '🔑',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_data',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_data': {
        'name': 'سحب بيانات 015',
        'emoji': '🔑',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_open_cache_015': {
        'name': 'فتح كاشات 015',
        'emoji': '🔓',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_open_cache',
        'target_prompt': '📞 أرسل رقم 015 المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_vodafone': {
        'name': 'بطاقات وي - فودافون',
        'emoji': '📱',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_voda',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_we': {
        'name': 'بطاقات وي - وي',
        'emoji': '🌐',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_we',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_etisalat': {
        'name': 'بطاقات وي - اتصالات',
        'emoji': '📡',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_etis',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_orange': {
        'name': 'بطاقات وي - أورنج',
        'emoji': '✨',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_orange',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_natera': {
        'name': 'بطاقات وي - نترا',
        'emoji': '🧙',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_natera',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'we_cards_tamween': {
        'name': 'بطاقات وي - تموين',
        'emoji': '🌾',
        'price': 50.0,
        'section': 'we',
        'service_code': 'we_cards_tamween',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
    'natera_numbers': {
        'name': 'أرقام نترا',
        'emoji': '📱',
        'price': 60.0,
        'section': 'natera',
        'service_code': 'natera',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم قومي'
    },
    'orange_data': {
        'name': 'بيانات أورنج',
        'emoji': '📱',
        'price': 60.0,
        'section': 'orange',
        'service_code': 'orange',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم قومي'
    },
    'orange_open_cache': {
        'name': 'فتح كاشات أورنج',
        'emoji': '🔓',
        'price': 50.0,
        'section': 'orange',
        'service_code': 'orange_open_cache',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'orange_close_cache': {
        'name': 'قفل كاشات أورنج',
        'emoji': '🔑',
        'price': 50.0,
        'section': 'orange',
        'service_code': 'orange_close_cache',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'etisalat_data': {
        'name': 'سحب بيانات اتصالات',
        'emoji': '📱',
        'price': 35.0,
        'section': 'etisalat',
        'service_code': 'Etisalat_data',
        'target_prompt': '📞 أرسل الرقم المستهدف:',
        'quantity_label': 'رقم'
    },
    'tamween': {
        'name': 'سحب بيانات تموين',
        'emoji': '🔑',
        'price': 50.0,
        'section': 'tamween',
        'service_code': 'tamween',
        'target_prompt': '📞 أرسل الرقم القومي المستهدف:',
        'quantity_label': 'رقم'
    },
}

SECTION_ARABIC_NAMES = {
    'vodafone': 'فودافون',
    'we': 'وي',
    'natera': 'النترا',
    'orange': 'أورنج',
    'etisalat': 'اتصالات',
    'tamween': 'تموين',
}

DEFAULT_SETTINGS = {
    'welcome_text': (
        '👑 مرحباً بك في بوت سحب البيانات\n\n'
        'القوانين:\n'
        '1. لا تكرر إرسال الطلب.\n'
        '2. أرسل الطلب بالمتطلبات المطلوبة.\n'
        '3. لا ترسل اسم/رقم المحفظة.\n'
        '4. لا تستعجل الطلب.\n'
        '5. للاستفسارات، استخدم الدعم الفني.\n\n'
        'طريقة الاستخدام:\n'
        '1. أرسل صورة الإيصال.\n'
        '2. أرسل رقم المحفظة المحول منها.\n'
        '3. أرسل اسم المحفظة.\n'
        '4. أرسل الرقم المستهدف.\n\n'
        'انتظر قليلاً 😎'
    ),
    'welcome_image': '',
    'support_username': '@support',
    'global_transfer_num': '01214691014',
    'trust_channel_id': '',
}

QUICK_REPLIES = [
    "✅ تم استلام طلبك وسيتم معالجته قريباً.",
    "⏳ طلبك قيد المراجعة، سيتم الرد خلال ساعات.",
    "❌ تم رفض الطلب بسبب عدم تطابق البيانات، يرجى إعادة الإرسال بشكل صحيح.",
    "💳 يرجى إرسال صورة الإيصال بوضوح.",
    "📞 تواصل مع الدعم الفني للمساعدة.",
]

def apply_emoji_formatting(text: str) -> str:
    if not text:
        return text
    for ch, repl in EMOJI_MAP.items():
        text = text.replace(ch, repl)
    return text

def wrap_in_blockquote(text: str) -> str:
    if text is None:
        return ""
    return f"<blockquote>{apply_emoji_formatting(str(text))}</blockquote>"

orig_send_msg   = bot.send_message
orig_send_photo = bot.send_photo
orig_edit_text  = bot.edit_message_text
orig_edit_cap   = bot.edit_message_caption

def send_wrapped_message(chat_id, text, **kwargs):
    kwargs.setdefault('parse_mode', 'HTML')
    return orig_send_msg(chat_id, wrap_in_blockquote(text), **kwargs)

def send_wrapped_photo(chat_id, photo, caption=None, **kwargs):
    kwargs.setdefault('parse_mode', 'HTML')
    return orig_send_photo(chat_id, photo, caption=wrap_in_blockquote(caption) if caption else None, **kwargs)

def edit_wrapped_text(text, chat_id=None, message_id=None, **kwargs):
    kwargs.setdefault('parse_mode', 'HTML')
    return orig_edit_text(wrap_in_blockquote(text), chat_id=chat_id, message_id=message_id, **kwargs)

def edit_wrapped_caption(chat_id=None, message_id=None, caption=None, **kwargs):
    kwargs.setdefault('parse_mode', 'HTML')
    return orig_edit_cap(chat_id=chat_id, message_id=message_id, caption=wrap_in_blockquote(caption) if caption else None, **kwargs)

bot.send_message         = send_wrapped_message
bot.send_photo           = send_wrapped_photo
bot.edit_message_text    = edit_wrapped_text
bot.edit_message_caption = edit_wrapped_caption

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        username TEXT,
        first_name TEXT,
        joined_at TEXT DEFAULT CURRENT_TIMESTAMP,
        referred_by INTEGER DEFAULT NULL,
        is_banned INTEGER DEFAULT 0
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        service_key TEXT,
        service_name TEXT,
        service_code TEXT,
        quantity INTEGER,
        price REAL,
        wallet_num TEXT,
        wallet_name TEXT,
        target_num TEXT,
        receipt_file_id TEXT,
        status TEXT DEFAULT 'pending',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        section_order_id INTEGER DEFAULT 1
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        ticket_type TEXT,
        message TEXT,
        status TEXT DEFAULT 'open',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS ticket_photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id INTEGER,
        file_id TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_id TEXT,
        channel_name TEXT,
        sub_type TEXT DEFAULT 'telegram'
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS admins (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        admin_type TEXT DEFAULT 'full',
        added_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS section_admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        section TEXT,
        added_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    try:
        c.execute('ALTER TABLE users ADD COLUMN captcha_passed INTEGER DEFAULT 0')
    except Exception:
        pass

    try:
        c.execute("ALTER TABLE orders ADD COLUMN section TEXT DEFAULT ''")
    except Exception:
        pass

    c.execute('''CREATE TABLE IF NOT EXISTS service_prices (
        service_key TEXT PRIMARY KEY,
        price REAL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS dynamic_sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        section_name TEXT,
        welcome_text TEXT DEFAULT '',
        position TEXT DEFAULT 'after',
        is_locked INTEGER DEFAULT 0,
        color TEXT DEFAULT 'none',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS dynamic_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        section_id INTEGER,
        button_name TEXT,
        service_price REAL DEFAULT 0,
        transfer_num TEXT DEFAULT '',
        service_code TEXT DEFAULT '',
        welcome_text TEXT DEFAULT '',
        is_locked INTEGER DEFAULT 0,
        color TEXT DEFAULT 'none'
    )''')

    conn.commit()

    for key, value in DEFAULT_SETTINGS.items():
        c.execute('INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)', (key, value))

    c.execute('INSERT OR IGNORE INTO admins (user_id, username) VALUES (?, ?)', (DEVELOPER_ID, 'developer'))

    conn.commit()
    conn.close()

def get_setting(key, default=''):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT value FROM settings WHERE key = ?', (key,))
    row = c.fetchone()
    conn.close()
    return row['value'] if row else default

def set_setting(key, value):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', (key, str(value)))
    conn.commit()
    conn.close()

def is_developer(user_id):
    return user_id == DEVELOPER_ID

def is_admin(user_id):
    if user_id == DEVELOPER_ID:
        return True
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT user_id FROM admins WHERE user_id = ?', (user_id,))
    row = c.fetchone()
    conn.close()
    return row is not None

def get_user_sections(user_id):
    if is_admin(user_id):
        return []
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT DISTINCT section FROM section_admins WHERE user_id = ?', (user_id,))
    rows = c.fetchall()
    conn.close()
    return [r['section'] for r in rows]

def is_section_admin_any(user_id):
    if is_admin(user_id):
        return False
    return len(get_user_sections(user_id)) > 0

def is_section_admin(user_id, section):
    if is_admin(user_id):
        return True
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT id FROM section_admins WHERE user_id = ? AND section = ?', (user_id, section))
    row = c.fetchone()
    conn.close()
    return row is not None

def has_passed_captcha(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT captcha_passed FROM users WHERE user_id = ?', (user_id,))
    row = c.fetchone()
    conn.close()
    return row and row['captcha_passed'] == 1

def mark_captcha_passed(user_id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET captcha_passed = 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

def get_service_price(service_key):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT price FROM service_prices WHERE service_key = ?', (service_key,))
    row = c.fetchone()
    conn.close()
    if row:
        return row['price']
    return SERVICES.get(service_key, {}).get('price', 0)

def get_user_info(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    row = c.fetchone()
    order_count = c.execute('SELECT COUNT(*) as cnt FROM orders WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    return row, order_count['cnt'] if order_count else 0

def get_banned_users():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT user_id, username, first_name FROM users WHERE is_banned = 1')
    rows = c.fetchall()
    conn.close()
    return rows

def check_user_banned(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT is_banned FROM users WHERE user_id = ?', (user_id,))
    row = c.fetchone()
    conn.close()
    return row and row['is_banned'] == 1

def add_user(user_id, username, first_name, referred_by=None):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    existing = c.fetchone()
    is_new = existing is None
    if is_new:
        c.execute(
            'INSERT OR IGNORE INTO users (user_id, username, first_name, referred_by) VALUES (?, ?, ?, ?)',
            (user_id, username or '', first_name or '', referred_by)
        )
        conn.commit()
    conn.close()
    return is_new

def get_user_count():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) as cnt FROM users')
    row = c.fetchone()
    conn.close()
    return row['cnt']

def get_subscriptions():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM subscriptions')
    rows = c.fetchall()
    conn.close()
    return rows

def check_subscription(user_id):
    subs = get_subscriptions()
    if not subs:
        return True, []
    not_subscribed = []
    for sub in subs:
        if sub['sub_type'] == 'telegram':
            try:
                member = bot.get_chat_member(sub['channel_id'], user_id)
                if member.status in ['left', 'kicked']:
                    not_subscribed.append(sub)
            except Exception:
                pass
    return len(not_subscribed) == 0, not_subscribed

def get_section_order_id(service_code):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) as cnt FROM orders WHERE service_code = ?', (service_code,))
    row = c.fetchone()
    conn.close()
    return row['cnt'] + 1

def save_order(user_id, service_key, service_name, service_code, quantity, price, wallet_num, wallet_name, target_num, receipt_file_id, section=''):
    conn = get_db_connection()
    c = conn.cursor()
    section_id = get_section_order_id(service_code)
    c.execute(
        '''INSERT INTO orders
           (user_id, service_key, service_name, service_code, quantity, price,
            wallet_num, wallet_name, target_num, receipt_file_id, section_order_id, section)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (user_id, service_key, service_name, service_code, quantity, price,
         wallet_num, wallet_name, target_num, receipt_file_id, section_id, section)
    )
    order_id = c.lastrowid
    conn.commit()
    conn.close()
    return order_id, section_id

def get_pending_orders_by_section():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT service_code, COUNT(*) as cnt FROM orders WHERE status='pending' GROUP BY service_code")
    rows = c.fetchall()
    conn.close()
    return {row['service_code']: row['cnt'] for row in rows}

def get_all_orders_count():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) as cnt FROM orders')
    row = c.fetchone()
    conn.close()
    return row['cnt']

def get_accepted_orders_count():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) as cnt FROM orders WHERE status='accepted'")
    row = c.fetchone()
    conn.close()
    return row['cnt']

def get_referral_count(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) as cnt FROM users WHERE referred_by = ?', (user_id,))
    row = c.fetchone()
    conn.close()
    return row['cnt']

def get_daily_income(date_str=None):
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COALESCE(SUM(price),0) as total FROM orders WHERE status='accepted' AND created_at LIKE ?",
        (f'{date_str}%',)
    ).fetchone()
    conn.close()
    return row['total']

def get_monthly_income(year_month=None):
    if not year_month:
        year_month = datetime.now().strftime('%Y-%m')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COALESCE(SUM(price),0) as total FROM orders WHERE status='accepted' AND created_at LIKE ?",
        (f'{year_month}%',)
    ).fetchone()
    conn.close()
    return row['total']

def get_top_services(limit=5):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT service_name, COUNT(*) as cnt FROM orders GROUP BY service_name ORDER BY cnt DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return rows

def get_rejection_rate():
    conn = get_db_connection()
    total = conn.execute("SELECT COUNT(*) as c FROM orders WHERE status IN ('accepted','rejected')").fetchone()['c']
    rejected = conn.execute("SELECT COUNT(*) as c FROM orders WHERE status='rejected'").fetchone()['c']
    conn.close()
    if total == 0:
        return 0.0
    return round((rejected / total) * 100, 1)

def get_today_orders_count():
    today = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COUNT(*) as c FROM orders WHERE created_at LIKE ?", (f'{today}%',)
    ).fetchone()
    conn.close()
    return row['c']

def get_new_users_today():
    today = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COUNT(*) as c FROM users WHERE joined_at LIKE ?", (f'{today}%',)
    ).fetchone()
    conn.close()
    return row['c']

def search_orders_advanced(query):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM orders WHERE target_num LIKE ? OR wallet_num LIKE ? ORDER BY id DESC LIMIT 10",
        (f'%{query}%', f'%{query}%')
    ).fetchall()
    conn.close()
    return rows

def get_orders_by_date(date_str):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM orders WHERE created_at LIKE ? ORDER BY id DESC LIMIT 30",
        (f'{date_str}%',)
    ).fetchall()
    conn.close()
    return rows

def add_order_note(order_id, note, admin_id):
    conn = get_db_connection()
    existing = conn.execute("SELECT value FROM settings WHERE key=?", (f'note_order_{order_id}',)).fetchone()
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_note = f"[{now_str} | {admin_id}]: {note}"
    if existing and existing['value']:
        new_note = existing['value'] + '\n' + new_note
    conn.execute("INSERT OR REPLACE INTO settings (key,value) VALUES (?,?)",
                 (f'note_order_{order_id}', new_note))
    conn.commit()
    conn.close()

def get_order_notes(order_id):
    conn = get_db_connection()
    row = conn.execute("SELECT value FROM settings WHERE key=?", (f'note_order_{order_id}',)).fetchone()
    conn.close()
    return row['value'] if row and row['value'] else None

def is_maintenance_mode():
    return get_setting('maintenance_mode', '0') == '1'

def get_maintenance_msg():
    return get_setting('maintenance_msg', '🛠️ البوت في وضع الصيانة حالياً. سيعود قريباً.')

def get_top_users(limit=10):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT user_id, COUNT(*) as cnt, COALESCE(SUM(price),0) as total "
        "FROM orders WHERE status='accepted' GROUP BY user_id ORDER BY cnt DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return rows

def get_section_stats():
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT service_key AS section_name, COUNT(*) as cnt, COALESCE(SUM(price),0) as total "
        "FROM orders WHERE status='accepted' GROUP BY service_key ORDER BY cnt DESC"
    ).fetchall()
    conn.close()
    return rows

def get_recent_users(limit=10):
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT user_id, username, first_name, joined_at FROM users ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return rows

def get_user_by_username(username):
    conn = get_db_connection()
    uname = username.lstrip('@').strip()
    row = conn.execute(
        "SELECT * FROM users WHERE username LIKE ?", (f'%{uname}%',)
    ).fetchone()
    conn.close()
    return row

def get_daily_order_limit():
    return int(get_setting('daily_order_limit', '0'))

def get_user_daily_orders(user_id):
    today = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COUNT(*) as c FROM orders WHERE user_id=? AND created_at LIKE ?",
        (user_id, f'{today}%')
    ).fetchone()
    conn.close()
    return row['c']

def get_announcement():
    return get_setting('bot_announcement', '')

def set_announcement(text):
    set_setting('bot_announcement', text)

def clear_announcement():
    set_setting('bot_announcement', '')

def get_section_income_summary():
    month = datetime.now().strftime('%Y-%m')
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT service_key AS section_name, COUNT(*) as cnt, COALESCE(SUM(price),0) as total "
        "FROM orders WHERE status='accepted' AND created_at LIKE ? "
        "GROUP BY service_key ORDER BY total DESC",
        (f'{month}%',)
    ).fetchall()
    conn.close()
    return rows

def delete_order_by_id(order_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM orders WHERE id=?", (order_id,))
    conn.commit()
    conn.close()

def get_users_by_join_date(date_str):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COUNT(*) as c FROM users WHERE joined_at LIKE ?",
        (f'{date_str}%',)
    ).fetchone()
    conn.close()
    return row['c']

def get_weekly_income():
    from datetime import timedelta
    week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    conn = get_db_connection()
    row = conn.execute(
        "SELECT COALESCE(SUM(price),0) as total FROM orders "
        "WHERE status='accepted' AND created_at >= ?",
        (week_ago,)
    ).fetchone()
    conn.close()
    return row['total']

def get_orders_pending_count():
    conn = get_db_connection()
    row = conn.execute("SELECT COUNT(*) as c FROM orders WHERE status='pending'").fetchone()
    conn.close()
    return row['c']

def get_section_image(section_key):
    section_img = get_setting(f'image_{section_key}', '')
    if section_img:
        return section_img
    return get_setting('welcome_image', 'https://j.top4top.io/p_3793scp9c0.png')

def post_delivery_to_trust_channel(order_row, client_name, rating_emoji=''):
    trust_channel = get_setting('trust_channel_id', '')
    if not trust_channel:
        return
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    day_names = {0: 'الاثنين', 1: 'الثلاثاء', 2: 'الأربعاء',
                 3: 'الخميس', 4: 'الجمعة', 5: 'السبت', 6: 'الأحد'}
    day_str = day_names.get(now.weekday(), date_str)
    time_str = now.strftime('%I:%M %p').replace('AM', 'ص').replace('PM', 'م')
    service_name = order_row['service_name'] if order_row['service_name'] else order_row['service_code']
    try:
        me = bot.get_me()
        dev_tag = f"@{me.username}" if me.username else me.first_name
    except Exception:
        dev_tag = 'المطور'
    rating_line = f"⭐ تقييم العميل: {rating_emoji}\n" if rating_emoji else ''
    msg = (
        "✅ <b>تم تسليم الطلب</b> ✅\n\n"
        f"👤 الخدمة: {service_name}\n"
        f"👤 اسم العميل: {client_name}\n"
        f"🕐 التاريخ: {date_str}\n"
        f"اليوم: {day_str}\n"
        f"الوقت: {time_str}\n"
        f"{rating_line}\n"
        f"{dev_tag}"
    )
    section_key = order_row['service_code'].lower().replace('_data', '').split('_')[0]
    image_url = get_setting(f'image_{section_key}', '') or get_setting('welcome_image', '')
    try:
        if image_url:
            bot.send_photo(trust_channel, image_url, caption=msg, parse_mode='HTML')
        else:
            bot.send_message(trust_channel, msg, parse_mode='HTML')
    except Exception:
        try:
            bot.send_message(trust_channel, msg, parse_mode='HTML')
        except Exception:
            pass

def post_to_trust_channel(order_row, client_name, rating_emoji):
    post_delivery_to_trust_channel(order_row, client_name, rating_emoji)

def get_last_referral(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT joined_at FROM users WHERE referred_by = ? ORDER BY joined_at DESC LIMIT 1', (user_id,))
    row = c.fetchone()
    conn.close()
    return row['joined_at'] if row else 'لا يوجد'

def get_transfer_num(section):
    defaults = {
        'vodafone': '01214691014',
        'we': '01214691014',
        'etisalat': '01214691014',
        'tamween': '01214691014',
        'natera': '01559376830',
        'orange': '01559376830',
    }
    return get_setting(f'cash_{section}', defaults.get(section, '01214691014'))

def get_section_admins_for_section(section):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT user_id FROM section_admins WHERE section = ?', (section,))
    rows = c.fetchall()
    conn.close()
    return [r['user_id'] for r in rows]

def get_pending_orders_for_sections(sections):
    if not sections:
        return []
    conn = get_db_connection()
    placeholders = ','.join('?' * len(sections))
    rows = conn.execute(
        f"SELECT * FROM orders WHERE status='pending' AND section IN ({placeholders}) ORDER BY id DESC",
        sections
    ).fetchall()
    conn.close()
    return rows

def section_admin_order_markup(order_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("✅ قبول الطلب", callback_data=f"sec_accept_{order_id}",
            style='success', icon_custom_emoji_id=E_CONFIRM),
        types.InlineKeyboardButton("❌ رفض الطلب", callback_data=f"sec_reject_{order_id}",
            style='danger', icon_custom_emoji_id=E_CANCEL)
    )
    markup.add(
        types.InlineKeyboardButton("📦 تسليم الطلب", callback_data=f"sec_deliver_{order_id}",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[10])
    )
    return markup

FULL_ADMIN_ALLOWED_EXACT = {
    'admin_change_cash', 'admin_stats', 'admin_users', 'admin_pending',
    'admin_toggle_sections', 'admin_ban', 'admin_unban', 'admin_banned_list',
    'admin_broadcast', 'admin_msg_user', 'admin_search_user',
    'admin_change_price', 'admin_accepted_orders', 'admin_view_order',
    'section_admin', 'back_main', 'noop', 'check_subscription',
    'admin_detailed_stats', 'admin_quick_replies', 'admin_advanced_search',
    'admin_export_orders', 'admin_date_filter', 'admin_maintenance_toggle',
    'admin_order_notes', 'admin_pending_alert_settings',
    'admin_top_users', 'admin_section_stats', 'admin_recent_users',
    'admin_search_username', 'admin_announcement', 'admin_announcement_set',
    'admin_announcement_clear', 'admin_daily_limit', 'admin_daily_limit_custom',
    'admin_db_backup', 'admin_delete_order',
    'admin_maintenance_activate_now', 'admin_maintenance_custom_msg',
    'admin_pending_alert_custom',
}
FULL_ADMIN_ALLOWED_PREFIXES = (
    'admin_change_cash_sec_', 'admin_set_price_', 'admin_toggle_sec_',
    'admin_quick_ban_', 'admin_quick_unban_', 'admin_quick_msg_',
    'admin_view_pending_section_', 'admin_show_receipt_',
    'dev_accept_', 'dev_reject_', 'dev_reply_', 'dev_rate_', 'dev_accept_nopost_',
    'admin_note_order_', 'admin_qr_send_', 'admin_filter_date_',
    'admin_set_alert_threshold_', 'admin_export_section_',
    'admin_set_daily_limit_', 'admin_confirm_delete_', 'admin_qr_pick_',
)

SECTION_ADMIN_ALLOWED_EXACT = {
    'section_admin', 'back_main', 'noop', 'check_subscription',
    'admin_change_cash', 'admin_change_price',
    'sec_admin_pending',
}
SECTION_ADMIN_ALLOWED_PREFIXES = (
    'admin_change_cash_sec_', 'admin_set_price_',
    'sec_accept_', 'sec_reject_', 'sec_deliver_',
    'admin_show_receipt_',
)

def section_admin_can(data):
    if data in SECTION_ADMIN_ALLOWED_EXACT:
        return True
    for prefix in SECTION_ADMIN_ALLOWED_PREFIXES:
        if data.startswith(prefix):
            return True
    return False

def full_admin_can(data):
    if data in FULL_ADMIN_ALLOWED_EXACT:
        return True
    for prefix in FULL_ADMIN_ALLOWED_PREFIXES:
        if data.startswith(prefix):
            return True
    return False

user_states = {}
captcha_data = {}
countdown_timers = {}

def set_state(user_id, state, **data):
    if user_id not in user_states:
        user_states[user_id] = {'state': state, 'data': {}}
    else:
        user_states[user_id]['state'] = state
    user_states[user_id]['data'].update(data)

def get_state(user_id):
    return user_states.get(user_id, {}).get('state', 'idle')

def get_data(user_id, key, default=None):
    return user_states.get(user_id, {}).get('data', {}).get(key, default)

def clear_state(user_id):
    user_states.pop(user_id, None)

def cancel_countdown(user_id):
    if user_id in countdown_timers:
        try:
            countdown_timers[user_id].cancel()
        except Exception:
            pass
        countdown_timers.pop(user_id, None)

def start_countdown(chat_id, user_id, message_id, has_photo, order_data):
    def update_timer(remaining):
        if user_id not in countdown_timers:
            return
        if get_state(user_id) != 'await_confirm':
            countdown_timers.pop(user_id, None)
            return
        if remaining <= 0:
            countdown_timers.pop(user_id, None)
            expired_text = "⏰ انتهى الوقت! تم إرسال طلبك تلقائياً للمراجعة."
            try:
                if has_photo:
                    bot.edit_message_caption(chat_id, message_id, caption=expired_text)
                else:
                    bot.edit_message_text(expired_text, chat_id, message_id)
            except Exception:
                pass
            notify_developer_order(chat_id, user_id, order_data)
            clear_state(user_id)
            return

        secs = remaining % 60
        timer_text = f"⏱ 00:{secs:02d}"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(timer_text, callback_data="noop",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[19]))
        markup.add(
            types.InlineKeyboardButton("✅ تأكيد", callback_data=f"confirm_order_{order_data['service_key']}",
                style='success', icon_custom_emoji_id=E_CONFIRM),
            types.InlineKeyboardButton("❌ رفض الطلب", callback_data="cancel_order",
                style='danger', icon_custom_emoji_id=E_CANCEL)
        )
        try:
            bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)
        except Exception:
            pass

        t = threading.Timer(1, update_timer, args=[remaining - 1])
        countdown_timers[user_id] = t
        t.start()

    t = threading.Timer(1, update_timer, args=[58])
    countdown_timers[user_id] = t
    t.start()

def notify_developer_order(chat_id, user_id, order_data):
    service = order_data['service']
    order_id = order_data['order_id']
    section_id = order_data['section_id']

    pending_map = get_pending_orders_by_section()
    total_pending = sum(pending_map.values())
    threshold = int(get_setting('pending_alert_threshold', '10'))
    if total_pending >= threshold:
        try:
            alert_text = (
                f"⚠️ <b>تنبيه: الطلبات المعلقة وصلت {total_pending} طلب!</b>\n\n"
                f"الحد المضبوط: {threshold} طلب\n"
                f"يرجى مراجعة الطلبات المعلقة."
            )
            bot.send_message(DEVELOPER_ID, alert_text, parse_mode='HTML')
        except Exception:
            pass

    text = (
        f"🆕 <b>طلب جديد</b>\n\n"
        f"👤 المستخدم: <a href='tg://user?id={user_id}'>{user_id}</a>\n"
        f"📋 رقم الطلب: #{order_id}\n"
        f"📋 رقم الطلب في القسم: #{section_id}\n"
        f"📱 الخدمة: {service['service_code']}\n"
        f"📱 اسم الخدمة: {service['name']}\n"
        f"🔢 العدد: {order_data['quantity']}\n"
        f"📱 رقم المحفظة: {order_data['wallet_num']}\n"
        f"🏦 اسم المحفظة: {order_data['wallet_name']}\n"
        f"📞 الرقم المستهدف: {order_data['target_num']}\n"
        f"💰 المبلغ: {order_data['price']} جنيه"
    )
    markup = developer_order_markup(order_id)

    targets = [DEVELOPER_ID]
    section = service.get('section', '')
    if section:
        sec_admin_ids = get_section_admins_for_section(section)
        for sa_id in sec_admin_ids:
            if sa_id not in targets:
                targets.append(sa_id)

    for target in targets:
        try:
            bot.send_photo(target, order_data['receipt_file_id'],
                           caption=text, reply_markup=markup, parse_mode='HTML')
        except Exception:
            try:
                bot.send_message(target, text, reply_markup=markup, parse_mode='HTML')
            except Exception:
                pass

def developer_order_markup(order_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("✅ قبول", callback_data=f"dev_accept_{order_id}",
            style='success', icon_custom_emoji_id=E_CONFIRM),
        types.InlineKeyboardButton("❌ رفض", callback_data=f"dev_reject_{order_id}",
            style='danger', icon_custom_emoji_id=E_CANCEL)
    )
    markup.add(types.InlineKeyboardButton("💬 إرسال رسالة", callback_data=f"dev_reply_{order_id}",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[5]))
    return markup

def developer_ticket_markup(ticket_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("💬 رد على التذكرة", callback_data=f"dev_ticket_reply_{ticket_id}",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[5]))
    return markup

def subscription_markup(not_subscribed):
    markup = types.InlineKeyboardMarkup()
    for sub in not_subscribed:
        if sub['sub_type'] == 'telegram':
            cid = sub['channel_id']
            url = f"https://t.me/{cid.lstrip('@')}"
        else:
            url = sub['channel_id']
        markup.add(types.InlineKeyboardButton(
            f"📢 اشترك في {sub['channel_name']}", url=url))
    markup.add(types.InlineKeyboardButton(
        "✅ تحققت من الاشتراك", callback_data="check_subscription",
        style='success', icon_custom_emoji_id=EMOJI_IDS[0]))
    return markup

def main_menu_markup(user_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("قسم فودافون", callback_data="section_vodafone",
            style='primary', icon_custom_emoji_id=E_VODAFONE),
        types.InlineKeyboardButton("قسم وي", callback_data="section_we",
            style='primary', icon_custom_emoji_id=E_WE)
    )
    markup.add(
        types.InlineKeyboardButton("قسم نترا", callback_data="section_natera",
            style='success', icon_custom_emoji_id=E_NATERA),
        types.InlineKeyboardButton("قسم أورنج", callback_data="section_orange",
            style='success', icon_custom_emoji_id=E_ORANGE)
    )
    markup.add(
        types.InlineKeyboardButton("قسم اتصالات", callback_data="section_etisalat",
            style='danger', icon_custom_emoji_id=E_ETISALAT),
        types.InlineKeyboardButton("قسم تموين", callback_data="section_tamween",
            style='danger', icon_custom_emoji_id=E_TAMWEEN)
    )
    markup.add(
        types.InlineKeyboardButton("طلباتي", callback_data="section_orders",
            style='primary', icon_custom_emoji_id=E_ORDERS),
        types.InlineKeyboardButton("الإحالات", callback_data="section_referrals",
            style='primary', icon_custom_emoji_id=E_REFERRAL)
    )
    markup.add(types.InlineKeyboardButton("الدعم الفني", callback_data="section_support",
        style='success', icon_custom_emoji_id=E_SUPPORT))
    if is_admin(user_id) or is_section_admin_any(user_id):
        markup.add(types.InlineKeyboardButton("⚙️ قسم الادمن", callback_data="section_admin",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[6]))
    return markup

def vodafone_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📱 سحب بيانات فودافون", callback_data="service_vodafone_data",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[1]))
    markup.add(types.InlineKeyboardButton("💎 بيانات رقم مميز فودافون", callback_data="service_vodafone_vip",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[2]))
    markup.add(types.InlineKeyboardButton("🔑 سحب ملكية سابقة 010", callback_data="service_vodafone_ownership",
        style='success', icon_custom_emoji_id=EMOJI_IDS[3]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='danger', icon_custom_emoji_id=E_BACK))
    return markup

def we_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔑 بطاقات 015", callback_data="we_cards_section",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[5]))
    markup.add(types.InlineKeyboardButton("🔑 بيانات وي 015", callback_data="service_we_data",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[7]))
    markup.add(types.InlineKeyboardButton("🔓 فتح كاشات 015", callback_data="service_we_open_cache_015",
        style='success', icon_custom_emoji_id=EMOJI_IDS[15]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def natera_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📱 أرقام نترا", callback_data="service_natera_numbers",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[1]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def orange_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📱 بيانات أورنج", callback_data="service_orange_data",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[1]))
    markup.add(types.InlineKeyboardButton("🔓 فتح كاشات", callback_data="service_orange_open_cache",
        style='primary', icon_custom_emoji_id=E_BACK))
    markup.add(types.InlineKeyboardButton("🔑 قفل كاشات", callback_data="service_orange_close_cache",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[6]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def etisalat_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📱 بيانات اتصالات", callback_data="service_etisalat_data",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[1]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def orders_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("📋 الطلب", callback_data="noop",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[8]),
        types.InlineKeyboardButton("📊 الحالة", callback_data="noop",
            style='success', icon_custom_emoji_id=EMOJI_IDS[9])
    )
    markup.add(types.InlineKeyboardButton("📭 لا توجد طلبات", callback_data="noop",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[10]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def support_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📞 مشكلة في السحب", callback_data="support_withdrawal",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[14]))
    markup.add(types.InlineKeyboardButton("❓ استفسار عام", callback_data="support_inquiry",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[1]))
    markup.add(types.InlineKeyboardButton("🔍 بيانات مشكوك بها", callback_data="support_suspicious",
        style='success', icon_custom_emoji_id=EMOJI_IDS[19]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def referrals_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def section_admin_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("━━━━ 📋 إدارة طلبات القسم ━━━━", callback_data="noop"))
    markup.add(types.InlineKeyboardButton("⏳ طلبات قسمي المعلقة", callback_data="sec_admin_pending",
        style='danger', icon_custom_emoji_id=EMOJI_IDS[19]))
    markup.add(types.InlineKeyboardButton("━━━━ ⚙️ إعدادات القسم ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("💰 تغيير رقم الكاش", callback_data="admin_change_cash",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[16]),
        types.InlineKeyboardButton("💲 تغيير سعر الخدمة", callback_data="admin_change_price",
            style='success', icon_custom_emoji_id=EMOJI_IDS[17])
    )
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='primary', icon_custom_emoji_id=E_BACK))
    return markup

def admin_markup():
    markup = types.InlineKeyboardMarkup()
    maintenance = is_maintenance_mode()
    maintenance_label = "🟢 تشغيل البوت" if maintenance else "🔴 وضع الصيانة"
    maintenance_style = 'success' if maintenance else 'danger'
    markup.add(types.InlineKeyboardButton(maintenance_label, callback_data="admin_maintenance_toggle",
        style=maintenance_style, icon_custom_emoji_id=EMOJI_IDS[14]))
    markup.add(
        types.InlineKeyboardButton("📢 إذاعة", callback_data="admin_broadcast",
            style='primary', icon_custom_emoji_id=E_BCAST),
        types.InlineKeyboardButton("📣 إعلان مثبت", callback_data="admin_announcement",
            style='danger', icon_custom_emoji_id=E_BCAST)
    )
    markup.add(types.InlineKeyboardButton("━━━━ 📂 إدارة الأقسام ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("➕ إضافة قسم", callback_data="admin_add_section",
            style='success', icon_custom_emoji_id=EMOJI_IDS[7]),
        types.InlineKeyboardButton("📂 إدارة الأقسام", callback_data="admin_manage_sections",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[8])
    )
    markup.add(
        types.InlineKeyboardButton("⏸ تشغيل/إيقاف الأقسام", callback_data="admin_toggle_sections",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[9]),
        types.InlineKeyboardButton("🎨 ألوان الأقسام", callback_data="admin_colors",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[21])
    )
    markup.add(
        types.InlineKeyboardButton("📝 رسالة داخل الأقسام", callback_data="admin_edit_section_welcome",
            style='success', icon_custom_emoji_id=EMOJI_IDS[18]),
        types.InlineKeyboardButton("📝 رسالة داخل الأزرار", callback_data="admin_edit_button_welcome",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[20])
    )
    markup.add(
        types.InlineKeyboardButton("🖼 صور الأقسام", callback_data="admin_section_images",
            style='success', icon_custom_emoji_id=EMOJI_IDS[3]),
        types.InlineKeyboardButton("💰 تغيير رقم الكاش", callback_data="admin_change_cash",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[16])
    )
    markup.add(types.InlineKeyboardButton("━━━━ ⚙️ إعدادات البوت ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("✏️ رسالة الترحيب", callback_data="admin_edit_welcome",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[2]),
        types.InlineKeyboardButton("🖼 صورة الترحيب", callback_data="admin_edit_image",
            style='success', icon_custom_emoji_id=EMOJI_IDS[3])
    )
    markup.add(
        types.InlineKeyboardButton("📌 الاشتراك الإجباري", callback_data="admin_subscription",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[0]),
        types.InlineKeyboardButton("👤 حساب الدعم", callback_data="admin_support_account",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[5])
    )
    markup.add(
        types.InlineKeyboardButton("🔗 قناة الثقة", callback_data="admin_trust_channel",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[4]),
        types.InlineKeyboardButton("📡 إعداد قناة الثقة", callback_data="admin_setup_trust",
            style='success', icon_custom_emoji_id=EMOJI_IDS[4])
    )
    markup.add(types.InlineKeyboardButton("━━━━ 📋 إدارة الطلبات ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("⏳ الطلبات المعلقة", callback_data="admin_pending",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[19]),
        types.InlineKeyboardButton("✅ الطلبات المقبولة", callback_data="admin_accepted_orders",
            style='success', icon_custom_emoji_id=EMOJI_IDS[0])
    )
    markup.add(
        types.InlineKeyboardButton("🔎 عرض طلب بالرقم", callback_data="admin_view_order",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[1]),
        types.InlineKeyboardButton("🗓 طلبات بتاريخ", callback_data="admin_date_filter",
            style='success', icon_custom_emoji_id=EMOJI_IDS[18])
    )
    markup.add(
        types.InlineKeyboardButton("🔍 بحث متقدم", callback_data="admin_advanced_search",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[1]),
        types.InlineKeyboardButton("📝 ملاحظات على طلب", callback_data="admin_order_notes",
            style='success', icon_custom_emoji_id=EMOJI_IDS[18])
    )
    markup.add(
        types.InlineKeyboardButton("📤 تصدير الطلبات", callback_data="admin_export_orders",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[10]),
        types.InlineKeyboardButton("🗑 حذف طلب", callback_data="admin_delete_order",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[14])
    )
    markup.add(
        types.InlineKeyboardButton("⚠️ تنبيه الطلبات", callback_data="admin_pending_alert_settings",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[14]),
        types.InlineKeyboardButton("🚦 حد الطلبات اليومي", callback_data="admin_daily_limit",
            style='success', icon_custom_emoji_id=EMOJI_IDS[19])
    )
    markup.add(types.InlineKeyboardButton("━━━━ 👥 إدارة المستخدمين ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("👥 جميع المستخدمين", callback_data="admin_users",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[13]),
        types.InlineKeyboardButton("🆕 أحدث المستخدمين", callback_data="admin_recent_users",
            style='success', icon_custom_emoji_id=EMOJI_IDS[13])
    )
    markup.add(
        types.InlineKeyboardButton("🏆 كبار المستخدمين", callback_data="admin_top_users",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[13]),
        types.InlineKeyboardButton("📨 رسالة لمستخدم", callback_data="admin_msg_user",
            style='success', icon_custom_emoji_id=EMOJI_IDS[5])
    )
    markup.add(
        types.InlineKeyboardButton("🔍 بحث بـ ID", callback_data="admin_search_user",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[1]),
        types.InlineKeyboardButton("🔎 بحث بالاسم", callback_data="admin_search_username",
            style='success', icon_custom_emoji_id=EMOJI_IDS[1])
    )
    markup.add(
        types.InlineKeyboardButton("🚫 حظر مستخدم", callback_data="admin_ban",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[14]),
        types.InlineKeyboardButton("✅ فك حظر مستخدم", callback_data="admin_unban",
            style='success', icon_custom_emoji_id=EMOJI_IDS[0])
    )
    markup.add(
        types.InlineKeyboardButton("📋 قائمة المحظورين", callback_data="admin_banned_list",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[1]),
        types.InlineKeyboardButton("⚡ ردود جاهزة", callback_data="admin_quick_replies",
            style='success', icon_custom_emoji_id=EMOJI_IDS[20])
    )
    markup.add(types.InlineKeyboardButton("━━━━ 📊 الإحصائيات ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("📊 إحصائيات عامة", callback_data="admin_stats",
            style='primary', icon_custom_emoji_id=E_STATS),
        types.InlineKeyboardButton("📈 إحصائيات تفصيلية", callback_data="admin_detailed_stats",
            style='success', icon_custom_emoji_id=EMOJI_IDS[22])
    )
    markup.add(types.InlineKeyboardButton("📊 إحصائيات الأقسام", callback_data="admin_section_stats",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[8]))
    markup.add(types.InlineKeyboardButton("━━━━ 🛡 الصلاحيات والأدوات ━━━━", callback_data="noop"))
    markup.add(
        types.InlineKeyboardButton("💲 تغيير سعر الخدمة", callback_data="admin_change_price",
            style='danger', icon_custom_emoji_id=EMOJI_IDS[16]),
        types.InlineKeyboardButton("🛡 أدمن كامل", callback_data="admin_admins",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[11])
    )
    markup.add(
        types.InlineKeyboardButton("🗂 أدمن قسم معين", callback_data="admin_section_admin",
            style='success', icon_custom_emoji_id=EMOJI_IDS[8]),
        types.InlineKeyboardButton("✨ إيموجي مميزة", callback_data="admin_emoji_guide",
            style='primary', icon_custom_emoji_id=EMOJI_IDS[21])
    )
    markup.add(types.InlineKeyboardButton("💾 نسخ احتياطي DB", callback_data="admin_db_backup",
        style='success', icon_custom_emoji_id=EMOJI_IDS[10]))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
        style='success', icon_custom_emoji_id=E_BACK))
    return markup

def confirm_order_markup(service_key, remaining=59):
    secs = remaining % 60
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(f"⏱ 00:{secs:02d}", callback_data="noop",
        style='primary', icon_custom_emoji_id=EMOJI_IDS[19]))
    markup.add(
        types.InlineKeyboardButton("✅ تأكيد", callback_data=f"confirm_order_{service_key}",
            style='success', icon_custom_emoji_id=E_CONFIRM),
        types.InlineKeyboardButton("❌ رفض", callback_data="cancel_order",
            style='danger', icon_custom_emoji_id=E_CANCEL)
    )
    return markup

def send_main_menu(chat_id, user_id):
    ann = get_announcement()
    if ann:
        try:
            bot.send_message(chat_id, f"📣 <b>إعلان هام</b>\n\n{ann}", parse_mode='HTML')
        except Exception:
            pass

    name = f'<a href="tg://user?id={user_id}">العميل</a>'
    welcome_text = get_setting('welcome_text', '').replace('{name}', name)
    welcome_image = get_setting('welcome_image', 'https://j.top4top.io/p_3793scp9c0.png')
    markup = main_menu_markup(user_id)
    try:
        bot.send_photo(chat_id, welcome_image, caption=welcome_text,
                       reply_markup=markup, parse_mode='HTML')
    except Exception:
        bot.send_message(chat_id, welcome_text, reply_markup=markup, parse_mode='HTML')

def send_subscription_screen(chat_id, user_id, not_subscribed):
    set_state(user_id, 'awaiting_subscription')
    text = (
        "👑 الاشتراك الإجباري\n\n"
        "عذراً، يجب الاشتراك في القنوات التالية أولاً:\n\n"
        "✨ بعد الاشتراك اضغط زر التحقق."
    )
    markup = subscription_markup(not_subscribed)
    bot.send_message(chat_id, text, reply_markup=markup)

def start_service_flow(chat_id, user_id, service_key):
    service = dict(SERVICES[service_key])
    dynamic_price = get_service_price(service_key)
    service['price'] = dynamic_price
    transfer_num = get_transfer_num(service['section'])
    custom_welcome = get_setting(f'service_welcome_{service_key}', '')
    set_state(user_id, 'await_quantity', service_key=service_key, service=service)

    if custom_welcome:
        text = custom_welcome
    else:
        text = (
            f"انت الآن داخل قسم: {service['emoji']} {service['name']}\n"
            f"سعر الخدمة لكل {service['quantity_label']}: {dynamic_price} جنيه\n"
            f"رقم التحويل: {transfer_num}\n\n"
            f"🎯 كم {service['quantity_label']} تريد تطبيق الخدمة عليه؟\n"
            f"✏️ أرسل العدد (أرقام فقط):"
        )
    bot.send_message(chat_id, text)

def send_captcha(chat_id, user_id):
    a = random.randint(1, 20)
    b = random.randint(5, 30)
    answer = a + b
    captcha_data[user_id] = {'answer': answer, 'attempts': 0}
    set_state(user_id, 'captcha')
    bot.send_message(
        chat_id,
        f"👑 مرحباً في البوت\n\n"
        f"✅ للتحقق من هويتك، يرجى حل المسألة التالية:\n\n"
        f"<b>{a} + {b} = ؟؟</b>",
        parse_mode='HTML'
    )

def is_section_disabled(section_key: str) -> bool:
    return get_setting(f'section_disabled_{section_key}', '0') == '1'

STOP_IMAGE_URL = 'https://j.top4top.io/p_3793scp9c0.png'

def send_section_with_image(chat_id, msg_id, section_key, text, markup):
    if is_section_disabled(section_key):
        back_m = types.InlineKeyboardMarkup()
        back_m.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main",
            style='success', icon_custom_emoji_id=E_BACK))
        try:
            bot.delete_message(chat_id, msg_id)
        except Exception:
            pass
        try:
            bot.send_photo(
                chat_id, STOP_IMAGE_URL,
                caption=(
                    f"🛡️ قسم {SECTION_ARABIC_NAMES.get(section_key, section_key)} متوقف مؤقتاً\n\n"
                    "سيعود قريباً."
                ),
                reply_markup=back_m, parse_mode='HTML'
            )
        except Exception:
            bot.send_message(
                chat_id,
                f"🛡️ قسم {SECTION_ARABIC_NAMES.get(section_key, section_key)} متوقف مؤقتاً\n\nسيعود قريباً.",
                reply_markup=back_m, parse_mode='HTML'
            )
        return

    img = get_section_image(section_key)
    try:
        bot.delete_message(chat_id, msg_id)
    except Exception:
        pass
    try:
        bot.send_photo(chat_id, img, caption=text, reply_markup=markup, parse_mode='HTML')
    except Exception:
        bot.send_message(chat_id, text, reply_markup=markup, parse_mode='HTML')

def _ban_user(chat_id, user_id):
    conn = get_db_connection()
    conn.execute('UPDATE users SET is_banned = 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    captcha_data.pop(user_id, None)
    clear_state(user_id)
    bot.send_message(chat_id, "❌ تم حظرك من البوت بسبب الإجابات الخاطئة المتكررة.")

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def handle_all_messages(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text or message.caption or ''

    if is_maintenance_mode() and not is_admin(user_id) and not is_section_admin_any(user_id):
        bot.send_message(chat_id, get_maintenance_msg())
        return

    if message.content_type == 'text' and text.startswith('/start'):
        if check_user_banned(user_id):
            bot.send_message(chat_id, "❌ أنت محظور من استخدام البوت.")
            return

        username = message.from_user.username
        first_name = message.from_user.first_name or ''
        referred_by = None
        parts = text.split()
        if len(parts) > 1:
            try:
                ref_id = int(parts[1])
                if ref_id != user_id:
                    referred_by = ref_id
            except Exception:
                pass

        is_new = add_user(user_id, username, first_name, referred_by)

        if is_new:
            try:
                bot.send_message(
                    DEVELOPER_ID,
                    f"مستخدم جديد في البوت\n\n"
                    f"اليوزر: @{username or 'بدون'}\n"
                    f"الايدي: {user_id}"
                )
            except Exception:
                pass
            if referred_by:
                try:
                    bot.send_message(
                        referred_by,
                        f"تم دخول شخص عبر رابطك\n\n"
                        f"اليوزر: @{username or 'بدون'}\n"
                        f"الايدي: {user_id}"
                    )
                except Exception:
                    pass

        cancel_countdown(user_id)
        clear_state(user_id)
        if has_passed_captcha(user_id) or is_admin(user_id) or is_section_admin_any(user_id):
            is_ok, not_subscribed = check_subscription(user_id)
            if not is_ok:
                send_subscription_screen(chat_id, user_id, not_subscribed)
            else:
                send_main_menu(chat_id, user_id)
        else:
            send_captcha(chat_id, user_id)
        return

    if check_user_banned(user_id) and not is_admin(user_id):
        bot.send_message(chat_id, "❌ أنت محظور من استخدام البوت.")
        return

    state = get_state(user_id)

    if state == 'captcha':
        if user_id not in captcha_data:
            send_captcha(chat_id, user_id)
            return
        if message.content_type != 'text':
            bot.send_message(chat_id, "❌ أرسل رقماً صحيحاً فقط.")
            return
        try:
            answer = int(text.strip())
        except Exception:
            captcha_data[user_id]['attempts'] += 1
            remaining = 3 - captcha_data[user_id]['attempts']
            if remaining <= 0:
                _ban_user(chat_id, user_id)
                return
            bot.send_message(chat_id, f"❌ إجابة خاطئة! المحاولات المتبقية: {remaining}")
            return

        if answer == captcha_data[user_id]['answer']:
            captcha_data.pop(user_id, None)
            clear_state(user_id)
            mark_captcha_passed(user_id)
            is_ok, not_subscribed = check_subscription(user_id)
            if not is_ok:
                send_subscription_screen(chat_id, user_id, not_subscribed)
            else:
                send_main_menu(chat_id, user_id)
        else:
            captcha_data[user_id]['attempts'] += 1
            remaining = 3 - captcha_data[user_id]['attempts']
            if remaining <= 0:
                _ban_user(chat_id, user_id)
                return
            bot.send_message(chat_id, f"❌ إجابة خاطئة! المحاولات المتبقية: {remaining}")
        return

    if state == 'await_quantity':
        if message.content_type != 'text':
            bot.send_message(chat_id, "❌ يرجى إرسال رقم صحيح أكبر من صفر")
            return
        try:
            quantity = int(text.strip())
            if quantity <= 0:
                raise ValueError
        except Exception:
            bot.send_message(chat_id, "❌ يرجى إرسال رقم صحيح أكبر من صفر")
            return
        service = get_data(user_id, 'service')
        price = round(service['price'] * quantity, 2)
        set_state(user_id, 'await_receipt', quantity=quantity, price=price)
        bot.send_message(
            chat_id,
            f"✅ تم تحديد العدد: {quantity}\n"
            f"💰 السعر الإجمالي: {price} جنيه\n\n"
            f"📤 أرسل صورة إيصال التحويل:"
        )
        return

    if state == 'await_receipt':
        if message.content_type != 'photo':
            bot.send_message(chat_id, "❌ يرجى إرسال صورة الإيصال")
            return
        file_id = message.photo[-1].file_id
        set_state(user_id, 'await_wallet_num', receipt_file_id=file_id)
        bot.send_message(
            chat_id,
            "✅ تم استلام الإيصال!\n\n"
            "📱 أرسل رقم المحفظة التي تم التحويل منها:"
        )
        return

    if state == 'await_wallet_num':
        if message.content_type != 'text':
            bot.send_message(chat_id, "❌ يرجى إرسال رقم المحفظة")
            return
        set_state(user_id, 'await_wallet_name', wallet_num=text.strip())
        bot.send_message(chat_id, "✅ تم استلام رقم المحفظة!\n\n🏦 أرسل اسم المحفظة:")
        return

    if state == 'await_wallet_name':
        if message.content_type != 'text':
            bot.send_message(chat_id, "❌ يرجى إرسال اسم المحفظة")
            return
        service = get_data(user_id, 'service')
        set_state(user_id, 'await_target', wallet_name=text.strip())
        bot.send_message(chat_id, f"✅ تم استلام اسم المحفظة!\n\n{service['target_prompt']}")
        return

    if state == 'await_target':
        if message.content_type != 'text':
            bot.send_message(chat_id, "❌ يرجى إرسال الرقم المطلوب")
            return
        target_num = text.strip()
        service_key = get_data(user_id, 'service_key')
        service = get_data(user_id, 'service')
        quantity = get_data(user_id, 'quantity')
        price = get_data(user_id, 'price')
        wallet_num = get_data(user_id, 'wallet_num')
        wallet_name = get_data(user_id, 'wallet_name')
        receipt_file_id = get_data(user_id, 'receipt_file_id')

        daily_limit = get_daily_order_limit()
        if daily_limit > 0 and not is_admin(user_id):
            today_count = get_user_daily_orders(user_id)
            if today_count >= daily_limit:
                bot.send_message(chat_id,
                    f"🚦 <b>وصلت للحد اليومي من الطلبات</b>\n\n"
                    f"الحد المسموح: {daily_limit} طلب/يوم\n"
                    f"طلباتك اليوم: {today_count}\n\n"
                    f"يمكنك إرسال طلبات جديدة غداً ✅",
                    parse_mode='HTML')
                clear_state(user_id)
                return

        order_id, section_id = save_order(
            user_id, service_key, service['name'], service['service_code'],
            quantity, price, wallet_num, wallet_name, target_num, receipt_file_id,
            section=service.get('section', '')
        )

        summary_text = (
            f"📋 ملخص الطلب:\n\n"
            f"📱 الخدمة: {service['name']}\n"
            f"📱 رقم المحفظة: {wallet_num}\n"
            f"🏦 اسم المحفظة: {wallet_name}\n"
            f"📞 الرقم المستهدف: {target_num}\n"
            f"💰 المبلغ: {price} جنيه\n\n"
            f"⏳ لديك 59 ثانية لتأكيد البيانات\n"
            f"💎 اضغط تأكيد للإرسال أو إلغاء للخروج"
        )
        markup = confirm_order_markup(service_key, 59)
        has_photo = True
        try:
            sent = bot.send_photo(chat_id, receipt_file_id,
                                  caption=summary_text, reply_markup=markup)
        except Exception:
            has_photo = False
            sent = bot.send_message(chat_id, summary_text, reply_markup=markup)

        order_data = {
            'service_key': service_key,
            'service': service,
            'quantity': quantity,
            'price': price,
            'wallet_num': wallet_num,
            'wallet_name': wallet_name,
            'target_num': target_num,
            'receipt_file_id': receipt_file_id,
            'order_id': order_id,
            'section_id': section_id,
        }
        set_state(user_id, 'await_confirm',
                  confirm_msg_id=sent.message_id,
                  has_photo=has_photo,
                  target_num=target_num,
                  order_id=order_id,
                  section_id=section_id,
                  order_data=order_data)
        start_countdown(chat_id, user_id, sent.message_id, has_photo, order_data)
        return

    if state == 'support_message':
        ticket_type = get_data(user_id, 'ticket_type')
        support_photos = get_data(user_id, 'support_photos') or []

        if message.content_type == 'text' and text.strip() == 'تم':
            support_text = get_data(user_id, 'support_text') or ''
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('INSERT INTO tickets (user_id, ticket_type, message) VALUES (?, ?, ?)',
                      (user_id, ticket_type, support_text))
            ticket_id = c.lastrowid
            for ph in support_photos:
                c.execute('INSERT INTO ticket_photos (ticket_id, file_id) VALUES (?, ?)', (ticket_id, ph))
            conn.commit()
            conn.close()

            bot.send_message(
                chat_id,
                f"✅ تم إرسال التذكرة بنجاح!\n\n"
                f"📋 رقم التذكرة: #{ticket_id}\n"
                f"📌 النوع: {ticket_type}\n\n"
                f"✨ سيتم الرد عليك قريباً"
            )

            dev_text = (
                f"🎫 <b>تذكرة جديدة #{ticket_id}</b>\n\n"
                f"👤 المستخدم: <a href='tg://user?id={user_id}'>{user_id}</a>\n"
                f"📌 النوع: {ticket_type}\n"
                f"💬 الرسالة:\n{support_text}"
            )
            t_markup = developer_ticket_markup(ticket_id)
            try:
                if support_photos:
                    bot.send_photo(DEVELOPER_ID, support_photos[0],
                                   caption=dev_text, reply_markup=t_markup, parse_mode='HTML')
                    for ph in support_photos[1:]:
                        bot.send_photo(DEVELOPER_ID, ph)
                else:
                    bot.send_message(DEVELOPER_ID, dev_text, reply_markup=t_markup, parse_mode='HTML')
            except Exception:
                pass

            clear_state(user_id)
            send_main_menu(chat_id, user_id)

        elif message.content_type == 'photo':
            file_id = message.photo[-1].file_id
            support_photos.append(file_id)
            set_state(user_id, 'support_message', support_photos=support_photos)
            bot.send_message(chat_id, "📝 تم حفظ الصورة. أرسل صوراً أخرى أو اكتب \"تم\" للإنهاء")

        elif message.content_type == 'text':
            current = get_data(user_id, 'support_text') or ''
            new_text = (current + '\n' + text).strip()
            set_state(user_id, 'support_message', support_text=new_text)
            bot.send_message(chat_id, "📝 تم حفظ الرسالة. أرسل صوراً أو اكتب \"تم\" للإنهاء")
        return

    if not is_admin(user_id) and not is_section_admin_any(user_id):
        return

    user_sections = get_user_sections(user_id)

    if state == 'admin_broadcast':
        if not is_admin(user_id):
            return
        conn = get_db_connection()
        users = conn.execute('SELECT user_id FROM users').fetchall()
        conn.close()
        success = 0
        for u in users:
            try:
                if message.content_type == 'text':
                    bot.send_message(u['user_id'],
                                     f"📢 إذاعة من الإدارة\n\n{text}")
                elif message.content_type == 'photo':
                    bot.send_photo(u['user_id'], message.photo[-1].file_id,
                                   caption=f"📢 إذاعة من الإدارة\n\n{message.caption or ''}")
                elif message.content_type == 'video':
                    bot.send_video(u['user_id'], message.video.file_id,
                                   caption=f"📢 إذاعة من الإدارة\n\n{message.caption or ''}")
                success += 1
                time.sleep(0.04)
            except Exception:
                pass
        bot.send_message(chat_id, f"✅ تم إرسال الإذاعة لـ {success} مستخدم")
        clear_state(user_id)
        return

    if state == 'admin_edit_welcome':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            set_setting('welcome_text', text)
            bot.send_message(chat_id, "✅ تم تحديث رسالة الترحيب")
        clear_state(user_id)
        return

    if state == 'admin_edit_image':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            set_setting('welcome_image', text.strip())
            bot.send_message(chat_id, "✅ تم تحديث صورة الترحيب")
        clear_state(user_id)
        return

    if state == 'admin_trust_channel':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            channel_id = text.strip()
            set_setting('trust_channel_id', channel_id)
            current = get_setting('trust_channel_id', '')
            bot.send_message(chat_id,
                f"✅ تم حفظ قناة الثقة\n"
                f"📡 الـ ID: <code>{current}</code>",
                parse_mode='HTML')
        clear_state(user_id)
        return

    if state == 'admin_set_section_image':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            section_key = get_data(user_id, 'section_image_key')
            image_url = text.strip()
            set_setting(f'image_{section_key}', image_url)
            section_names = {
                'vodafone': 'فودافون', 'we': 'وي', 'natera': 'النترا',
                'orange': 'أورنج', 'etisalat': 'اتصالات', 'tamween': 'تموين',
                'main': 'الرئيسية'
            }
            sname = section_names.get(section_key, section_key)
            bot.send_message(chat_id, f"✅ تم تحديث صورة قسم {sname}")
        clear_state(user_id)
        return

    if state == 'admin_support_account':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            set_setting('support_username', text.strip())
            bot.send_message(chat_id, "✅ تم حفظ حساب الدعم")
        clear_state(user_id)
        return

    if state == 'admin_add_sub_telegram':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            channel = text.strip()
            if not channel.startswith('@'):
                channel = '@' + channel
            try:
                chat_info = bot.get_chat(channel)
                name = chat_info.title or channel
            except Exception:
                name = channel
            conn = get_db_connection()
            conn.execute('INSERT INTO subscriptions (channel_id, channel_name, sub_type) VALUES (?, ?, ?)',
                         (channel, name, 'telegram'))
            conn.commit()
            conn.close()
            bot.send_message(chat_id, f"✅ تم إضافة قناة {name} للاشتراك الإجباري")
        clear_state(user_id)
        return

    if state == 'admin_add_sub_link':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            url = text.strip()
            conn = get_db_connection()
            conn.execute('INSERT INTO subscriptions (channel_id, channel_name, sub_type) VALUES (?, ?, ?)',
                         (url, 'رابط', 'url'))
            conn.commit()
            conn.close()
            bot.send_message(chat_id, "✅ تم إضافة الرابط للاشتراك الإجباري")
        clear_state(user_id)
        return

    if state == 'admin_add_admin':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            identifier = text.strip().lstrip('@')
            try:
                if identifier.isdigit():
                    new_uid = int(identifier)
                    uname = identifier
                else:
                    info = bot.get_chat(f'@{identifier}')
                    new_uid = info.id
                    uname = identifier
                conn = get_db_connection()
                conn.execute('INSERT OR REPLACE INTO admins (user_id, username) VALUES (?, ?)', (new_uid, uname))
                conn.commit()
                conn.close()
                bot.send_message(chat_id, f"✅ تم إضافة المشرف {uname}")
            except Exception as e:
                bot.send_message(chat_id, f"❌ خطأ: {e}")
        clear_state(user_id)
        return

    if state == 'admin_add_section_name':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            section_name = text.strip()
            set_state(user_id, 'admin_add_section_pos', new_section_name=section_name)
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("⬆️ فوق الأزرار", callback_data="admin_sec_pos_above",
                    style='primary', icon_custom_emoji_id=EMOJI_IDS[22]),
                types.InlineKeyboardButton("⬇️ تحت الأزرار", callback_data="admin_sec_pos_below",
                    style='success', icon_custom_emoji_id=EMOJI_IDS[12])
            )
            bot.send_message(chat_id, f"📍 أين تريد إضافة قسم '{section_name}'؟", reply_markup=markup)
        return

    if state == 'admin_add_section_welcome':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            section_name = get_data(user_id, 'new_section_name')
            position = get_data(user_id, 'section_position', 'after')
            welcome_text_val = text.strip() if text.strip() != '-' else ''
            conn = get_db_connection()
            conn.execute('INSERT INTO dynamic_sections (section_name, welcome_text, position) VALUES (?, ?, ?)',
                         (section_name, welcome_text_val, position))
            conn.commit()
            conn.close()
            bot.send_message(chat_id, f"✅ تم إضافة قسم '{section_name}'")
            clear_state(user_id)
        return

    if state == 'admin_edit_sec_welcome':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            section = get_data(user_id, 'editing_section')
            set_setting(f'section_welcome_{section}', text)
            bot.send_message(chat_id, f"✅ تم تحديث رسالة ترحيب قسم {section}")
        clear_state(user_id)
        return

    if state == 'admin_edit_btn_welcome':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            skey = get_data(user_id, 'editing_service')
            set_setting(f'service_welcome_{skey}', text)
            bot.send_message(chat_id, f"✅ تم تحديث رسالة الخدمة")
        clear_state(user_id)
        return

    if state == 'admin_change_cash':
        section = get_data(user_id, 'cash_section')
        if user_sections and section not in user_sections:
            bot.send_message(chat_id, "لا يمكنك تغيير كاش هذا القسم 🛡️")
            clear_state(user_id)
            return
        if message.content_type == 'text':
            new_num = text.strip()
            set_setting(f'cash_{section}', new_num)
            bot.send_message(chat_id, f"✅ تم تحديث رقم الكاش لقسم {section} إلى {new_num}")
        clear_state(user_id)
        return

    if state == 'admin_ban_id':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            try:
                target = int(text.strip())
                conn = get_db_connection()
                conn.execute('UPDATE users SET is_banned = 1 WHERE user_id = ?', (target,))
                conn.commit()
                conn.close()
                bot.send_message(chat_id, f"✅ تم حظر المستخدم {target}")
                try:
                    bot.send_message(target, "🚫 تم حظرك من البوت.")
                except Exception:
                    pass
            except Exception:
                bot.send_message(chat_id, "❌ يرجى إرسال ID رقمي صحيح.")
        clear_state(user_id)
        return

    if state == 'admin_unban_id':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            try:
                target = int(text.strip())
                conn = get_db_connection()
                conn.execute('UPDATE users SET is_banned = 0 WHERE user_id = ?', (target,))
                conn.commit()
                conn.close()
                bot.send_message(chat_id, f"✅ تم فك حظر المستخدم {target}")
                try:
                    bot.send_message(target, "✅ تم رفع الحظر، يمكنك استخدام البوت مجدداً.")
                except Exception:
                    pass
            except Exception:
                bot.send_message(chat_id, "❌ يرجى إرسال ID رقمي صحيح.")
        clear_state(user_id)
        return

    if state == 'admin_msg_user_id':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            try:
                target = int(text.strip())
                set_state(user_id, 'admin_msg_user_text', msg_target_id=target)
                bot.send_message(chat_id, f"✏️ أرسل الرسالة للمستخدم {target}:")
            except Exception:
                bot.send_message(chat_id, "❌ يرجى إرسال ID رقمي صحيح.")
                clear_state(user_id)
        return

    if state == 'admin_msg_user_text':
        if not is_admin(user_id):
            return
        target = get_data(user_id, 'msg_target_id')
        if target:
            try:
                if message.content_type == 'text':
                    bot.send_message(target, f"📨 رسالة من الإدارة:\n\n{text}")
                elif message.content_type == 'photo':
                    bot.send_photo(target, message.photo[-1].file_id,
                                   caption=f"📨 رسالة من الإدارة:\n\n{message.caption or ''}")
                elif message.content_type == 'video':
                    bot.send_video(target, message.video.file_id,
                                   caption=f"📨 رسالة من الإدارة:\n\n{message.caption or ''}")
                bot.send_message(chat_id, f"✅ تم إرسال الرسالة للمستخدم {target}")
            except Exception as e:
                bot.send_message(chat_id, f"❌ فشل الإرسال: {e}")
        clear_state(user_id)
        return

    if state == 'admin_search_user_id':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            try:
                target = int(text.strip())
                row, orders_cnt = get_user_info(target)
                if row:
                    ref_cnt = get_referral_count(target)
                    status_text = "🚫 محظور" if row['is_banned'] else "✅ نشط"
                    info = (
                        f"🔍 <b>بيانات المستخدم</b>\n\n"
                        f"👤 ID: <code>{row['user_id']}</code>\n"
                        f"👤 الاسم: {row['first_name']}\n"
                        f"🌐 اليوزر: @{row['username'] or 'بدون'}\n"
                        f"📅 تاريخ الانضمام: {row['joined_at']}\n"
                        f"📊 الحالة: {status_text}\n"
                        f"📦 عدد الطلبات: {orders_cnt}\n"
                        f"👥 عدد الإحالات: {ref_cnt}"
                    )
                    markup = types.InlineKeyboardMarkup()
                    if row['is_banned']:
                        markup.add(types.InlineKeyboardButton("✅ فك الحظر", callback_data=f"admin_quick_unban_{target}"))
                    else:
                        markup.add(types.InlineKeyboardButton("🚫 حظر", callback_data=f"admin_quick_ban_{target}"))
                    markup.add(types.InlineKeyboardButton("📨 إرسال رسالة", callback_data=f"admin_quick_msg_{target}"))
                    bot.send_message(chat_id, info, reply_markup=markup, parse_mode='HTML')
                else:
                    bot.send_message(chat_id, "❌ لم يتم العثور على المستخدم.")
            except Exception:
                bot.send_message(chat_id, "❌ يرجى إرسال ID رقمي صحيح.")
        clear_state(user_id)
        return

    if state == 'admin_announcement_text':
        if not is_admin(user_id):
            return
        if message.content_type == 'text':
            set_announcement(text.strip())
            bot.send_message(chat_id, "✅ تم تعيين الإعلان المثبت بنجاح.")
        clear_state(user_id)
        return

    if state == 'admin_set_price_value':
        if message.content_type == 'text':
            skey = get_data(user_id, 'price_service_key')
            try:
                new_price = float(text.strip())
                conn = get_db_connection()
                conn.execute('INSERT OR REPLACE INTO service_prices (service_key, price) VALUES (?, ?)',
                             (skey, new_price))
                conn.commit()
                conn.close()
                bot.send_message(chat_id, f"✅ تم تحديث سعر الخدمة {skey} إلى {new_price} جنيه.")
            except Exception:
                bot.send_message(chat_id, "❌ يرجى إرسال سعر رقمي صحيح.")
        clear_state(user_id)
        return

    if state.startswith('dev_reply_text_'):
        order_id = state.replace('dev_reply_text_', '')
        conn = get_db_connection()
        order = conn.execute('SELECT * FROM orders WHERE id=?', (order_id,)).fetchone()
        conn.close()
        if order:
            try:
                if message.content_type == 'text':
                    bot.send_message(order['user_id'], f"💬 رسالة من الإدارة حول طلبك #{order_id}:\n\n{text}")
                elif message.content_type == 'photo':
                    bot.send_photo(order['user_id'], message.photo[-1].file_id,
                                   caption=f"💬 رسالة من الإدارة حول طلبك #{order_id}:\n\n{message.caption or ''}")
                bot.send_message(chat_id, f"✅ تم إرسال الرد للعميل للطلب #{order_id}")
            except Exception as e:
                bot.send_message(chat_id, f"❌ فشل الإرسال: {e}")
        clear_state(user_id)
        return

    if state.startswith('ticket_reply_text_'):
        ticket_id = state.replace('ticket_reply_text_', '')
        conn = get_db_connection()
        ticket = conn.execute('SELECT * FROM tickets WHERE id=?', (ticket_id,)).fetchone()
        conn.close()
        if ticket:
            try:
                if message.content_type == 'text':
                    bot.send_message(ticket['user_id'], f"💬 رد الدعم الفني على تذكرتك #{ticket_id}:\n\n{text}")
                elif message.content_type == 'photo':
                    bot.send_photo(ticket['user_id'], message.photo[-1].file_id,
                                   caption=f"💬 رد الدعم الفني على تذكرتك #{ticket_id}:\n\n{message.caption or ''}")
                conn = get_db_connection()
                conn.execute("UPDATE tickets SET status='closed' WHERE id=?", (ticket_id,))
                conn.commit()
                conn.close()
                bot.send_message(chat_id, f"✅ تم الرد وإغلاق التذكرة #{ticket_id}")
            except Exception as e:
                bot.send_message(chat_id, f"❌ فشل الإرسال: {e}")
        clear_state(user_id)
        return

    if state.startswith('sec_deliver_file_'):
        order_id = state.replace('sec_deliver_file_', '')
        conn = get_db_connection()
        order = conn.execute('SELECT * FROM orders WHERE id=?', (order_id,)).fetchone()
        conn.close()
        if order:
            try:
                client_id = order['user_id']
                if message.content_type == 'photo':
                    bot.send_photo(client_id, message.photo[-1].file_id,
                                   caption=f"📦 تم تسليم طلبك #{order_id}:\n\n{message.caption or ''}")
                elif message.content_type == 'document':
                    bot.send_document(client_id, message.document.file_id,
                                      caption=f"📦 تم تسليم طلبك #{order_id}:\n\n{message.caption or ''}")
                elif message.content_type == 'text':
                    bot.send_message(client_id, f"📦 تم تسليم طلبك #{order_id}:\n\n{text}")

                conn = get_db_connection()
                conn.execute("UPDATE orders SET status='accepted' WHERE id=?", (order_id,))
                conn.commit()
                conn.close()

                rate_markup = types.InlineKeyboardMarkup()
                rate_markup.add(
                    types.InlineKeyboardButton("⭐ 1", callback_data=f"dev_rate_1_{order_id}"),
                    types.InlineKeyboardButton("⭐ 2", callback_data=f"dev_rate_2_{order_id}"),
                    types.InlineKeyboardButton("⭐ 3", callback_data=f"dev_rate_3_{order_id}"),
                    types.InlineKeyboardButton("⭐ 4", callback_data=f"dev_rate_4_{order_id}"),
                    types.InlineKeyboardButton("⭐ 5", callback_data=f"dev_rate_5_{order_id}")
                )
                bot.send_message(client_id, "🌟 يرجى تقييم الخدمة المدمة لك:", reply_markup=rate_markup)
                bot.send_message(chat_id, f"✅ تم تسليم الطلب #{order_id} وإشعار العميل.")
            except Exception as e:
                bot.send_message(chat_id, f"❌ فشل تسليم الطلب: {e}")
        clear_state(user_id)
        return

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    data = call.data

    if is_maintenance_mode() and not is_admin(user_id) and not is_section_admin_any(user_id):
        bot.answer_callback_query(call.id, get_maintenance_msg(), show_alert=True)
        return

    if check_user_banned(user_id) and not is_admin(user_id):
        bot.answer_callback_query(call.id, "❌ أنت محظور من استخدام البوت.", show_alert=True)
        return

    if data == "noop":
        bot.answer_callback_query(call.id)
        return

    if data == "check_subscription":
        is_ok, not_subscribed = check_subscription(user_id)
        if is_ok:
            bot.answer_callback_query(call.id, "✅ شكراً لاشتراكك!")
            clear_state(user_id)
            try:
                bot.delete_message(chat_id, msg_id)
            except Exception:
                pass
            send_main_menu(chat_id, user_id)
        else:
            bot.answer_callback_query(call.id, "❌ لم تشترك في كافة القنوات بعد!", show_alert=True)
        return

    if data == "back_main":
        cancel_countdown(user_id)
        clear_state(user_id)
        try:
            bot.delete_message(chat_id, msg_id)
        except Exception:
            pass
        send_main_menu(chat_id, user_id)
        return

    # User main menu navigation
    if data == "section_vodafone":
        text = "📱 <b>قسم خدمات فودافون</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'vodafone', text, vodafone_markup())
        return

    if data == "section_we":
        text = "🌐 <b>قسم خدمات وي</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'we', text, we_markup())
        return

    if data == "section_natera":
        text = "🧙 <b>قسم خدمات نترا</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'natera', text, natera_markup())
        return

    if data == "section_orange":
        text = "✨ <b>قسم خدمات أورنج</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'orange', text, orange_markup())
        return

    if data == "section_etisalat":
        text = "📡 <b>قسم خدمات اتصالات</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'etisalat', text, etisalat_markup())
        return

    if data == "section_tamween":
        text = "🌾 <b>قسم خدمات تموين</b>\nاختر الخدمة المطلوبة:"
        send_section_with_image(chat_id, msg_id, 'tamween', text, etisalat_markup())
        return

    if data.startswith("service_"):
        service_key = data.replace("service_", "")
        if service_key in SERVICES:
            try:
                bot.delete_message(chat_id, msg_id)
            except Exception:
                pass
            start_service_flow(chat_id, user_id, service_key)
        else:
            bot.answer_callback_query(call.id, "الخدمة غير متاحة حالياً.")
        return

    if data == "we_cards_section":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📱 وي - فودافون", callback_data="service_we_cards_vodafone"))
        markup.add(types.InlineKeyboardButton("🌐 وي - وي", callback_data="service_we_cards_we"))
        markup.add(types.InlineKeyboardButton("📡 وي - اتصالات", callback_data="service_we_cards_etisalat"))
        markup.add(types.InlineKeyboardButton("✨ وي - أورنج", callback_data="service_we_cards_orange"))
        markup.add(types.InlineKeyboardButton("🧙 وي - نترا", callback_data="service_we_cards_natera"))
        markup.add(types.InlineKeyboardButton("🌾 وي - تموين", callback_data="service_we_cards_tamween"))
        markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="section_we"))
        try:
            bot.edit_message_caption("🔑 اختر نوع بطاقات وي:", chat_id=chat_id, message_id=msg_id, reply_markup=markup)
        except Exception:
            bot.edit_message_text("🔑 اختر نوع بطاقات وي:", chat_id=chat_id, message_id=msg_id, reply_markup=markup)
        return

    if data.startswith("confirm_order_"):
        cancel_countdown(user_id)
        order_data = get_data(user_id, 'order_data')
        if order_data:
            notify_developer_order(chat_id, user_id, order_data)
            clear_state(user_id)
            bot.answer_callback_query(call.id, "✅ تم تأكيد طلبك وإرساله للإدارة!")
            try:
                bot.edit_message_caption("✅ <b>تم تأكيد إرسال الطلب بنجاح!</b>\nسيتم مراجعته والتنفيذ قريباً.",
                                         chat_id=chat_id, message_id=msg_id)
            except Exception:
                bot.edit_message_text("✅ <b>تم تأكيد إرسال الطلب بنجاح!</b>\nسيتم مراجعته والتنفيذ قريباً.",
                                      chat_id=chat_id, message_id=msg_id)
        else:
            bot.answer_callback_query(call.id, "حدث خطأ أو انتهت الجلسة.", show_alert=True)
        return

    if data == "cancel_order":
        cancel_countdown(user_id)
        order_id = get_data(user_id, 'order_id')
        if order_id:
            delete_order_by_id(order_id)
        clear_state(user_id)
        bot.answer_callback_query(call.id, "❌ تم إلغاء الطلب.")
        try:
            bot.delete_message(chat_id, msg_id)
        except Exception:
            pass
        send_main_menu(chat_id, user_id)
        return

    if data == "section_orders":
        conn = get_db_connection()
        orders = conn.execute("SELECT * FROM orders WHERE user_id=? ORDER BY id DESC LIMIT 10", (user_id,)).fetchall()
        conn.close()
        if not orders:
            try:
                bot.edit_message_text("📭 ليس لديك طلبات سابقة.", chat_id=chat_id, message_id=msg_id, reply_markup=orders_markup())
            except Exception:
                bot.send_message(chat_id, "📭 ليس لديك طلبات سابقة.", reply_markup=orders_markup())
        else:
            text = "📋 <b>طلباتك الأخيرة:</b>\n\n"
            for o in orders:
                st = "⏳ قيد المراجعة" if o['status'] == 'pending' else ("✅ مقبول" if o['status'] == 'accepted' else "❌ مرفوض")
                text += f"▪️ طلب #{o['id']} - {o['service_name']} | الحالة: {st}\n"
            try:
                bot.edit_message_text(text, chat_id=chat_id, message_id=msg_id, reply_markup=orders_markup(), parse_mode='HTML')
            except Exception:
                bot.send_message(chat_id, text, reply_markup=orders_markup(), parse_mode='HTML')
        return

    if data == "section_referrals":
        ref_cnt = get_referral_count(user_id)
        bot_username = bot.get_me().username
        link = f"https://t.me/{bot_username}?start={user_id}"
        last_ref = get_last_referral(user_id)
        text = (
            f"👥 <b>نظام الإحالات الخاص بك</b>\n\n"
            f"🔗 رابط الإحالة:\n<code>{link}</code>\n\n"
            f"📊 عدد الأشخاص المنضمين عبرك: {ref_cnt}\n"
            f"📅 آخر انضمام: {last_ref}"
        )
        try:
            bot.edit_message_text(text, chat_id=chat_id, message_id=msg_id, reply_markup=referrals_markup(), parse_mode='HTML')
        except Exception:
            bot.send_message(chat_id, text, reply_markup=referrals_markup(), parse_mode='HTML')
        return

    if data == "section_support":
        try:
            bot.edit_message_text("🛠 <b>قسم الدعم الفني</b>\nاختر نوع التذكرة:", chat_id=chat_id, message_id=msg_id, reply_markup=support_markup())
        except Exception:
            bot.send_message(chat_id, "🛠 <b>قسم الدعم الفني</b>\nاختر نوع التذكرة:", reply_markup=support_markup())
        return

    if data.startswith("support_"):
        ttype = data.replace("support_", "")
        type_names = {'withdrawal': 'مشكلة في السحب', 'inquiry': 'استفسار عام', 'suspicious': 'بيانات مشكوك بها'}
        tname = type_names.get(ttype, ttype)
        set_state(user_id, 'support_message', ticket_type=tname, support_photos=[], support_text='')
        bot.send_message(chat_id, f"📝 أرسل التفاصيل والجمَل أو الصور لتذكرة ({tname}).\nعند الانتهاء اكتب كلمة \"تم\".")
        return

    # Admin Control Handlers
    if data == "section_admin":
        if is_admin(user_id):
            try:
                bot.edit_message_text("⚙️ <b>لوحة تحكم الأدمن الكامل</b>", chat_id=chat_id, message_id=msg_id, reply_markup=admin_markup())
            except Exception:
                bot.send_message(chat_id, "⚙️ <b>لوحة تحكم الأدمن الكامل</b>", reply_markup=admin_markup())
        elif is_section_admin_any(user_id):
            try:
                bot.edit_message_text("⚙️ <b>لوحة تحكم أدمن القسم</b>", chat_id=chat_id, message_id=msg_id, reply_markup=section_admin_markup())
            except Exception:
                bot.send_message(chat_id, "⚙️ <b>لوحة تحكم أدمن القسم</b>", reply_markup=section_admin_markup())
        return

    # Developer/Admin Order actions
    if data.startswith("dev_accept_") or data.startswith("sec_accept_"):
        order_id = data.split("_")[-1]
        conn = get_db_connection()
        conn.execute("UPDATE orders SET status='accepted' WHERE id=?", (order_id,))
        order = conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()
        conn.commit()
        conn.close()

        bot.answer_callback_query(call.id, "✅ تم قبول الطلب!")
        if order:
            try:
                bot.send_message(order['user_id'], f"✅ تم قبول طلبك #{order_id} وجاري تنفيذه!")
            except Exception:
                pass
        return

    if data.startswith("dev_reject_") or data.startswith("sec_reject_"):
        order_id = data.split("_")[-1]
        conn = get_db_connection()
        conn.execute("UPDATE orders SET status='rejected' WHERE id=?", (order_id,))
        order = conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()
        conn.commit()
        conn.close()

        bot.answer_callback_query(call.id, "❌ تم رفض الطلب!")
        if order:
            try:
                bot.send_message(order['user_id'], f"❌ للأسف تم رفض طلبك #{order_id}.")
            except Exception:
                pass
        return

    if data.startswith("dev_reply_"):
        order_id = data.replace("dev_reply_", "")
        set_state(user_id, f"dev_reply_text_{order_id}")
        bot.send_message(chat_id, f"✏️ اكتب الرسالة للرد على العميل لطلب #{order_id}:")
        return

    if data.startswith("dev_ticket_reply_"):
        ticket_id = data.replace("dev_ticket_reply_", "")
        set_state(user_id, f"ticket_reply_text_{ticket_id}")
        bot.send_message(chat_id, f"✏️ اكتب الرسالة للرد على التذكرة #{ticket_id}:")
        return

    if data.startswith("sec_deliver_"):
        order_id = data.replace("sec_deliver_", "")
        set_state(user_id, f"sec_deliver_file_{order_id}")
        bot.send_message(chat_id, f"📦 أرسل الملف/الصورة أو النص المراد تسليمه للعميل للطلب #{order_id}:")
        return

    if data.startswith("dev_rate_"):
        parts = data.split("_")
        rating = parts[2]
        order_id = parts[3]
        conn = get_db_connection()
        order = conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()
        user_row = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
        conn.close()

        client_name = user_row['first_name'] if user_row else "عميل"
        star_map = {'1': '⭐', '2': '⭐⭐', '3': '⭐⭐⭐', '4': '⭐⭐⭐⭐', '5': '⭐⭐⭐⭐⭐'}
        post_to_trust_channel(order, client_name, star_map.get(rating, '⭐'))
        bot.answer_callback_query(call.id, "شكراً لتقييمك! ❤️")
        try:
            bot.delete_message(chat_id, msg_id)
        except Exception:
            pass
        return

    if data == "admin_maintenance_toggle":
        if not is_admin(user_id):
            return
        curr = is_maintenance_mode()
        set_setting('maintenance_mode', '0' if curr else '1')
        bot.answer_callback_query(call.id, "تم تغيير حالة الصيانة")
        try:
            bot.edit_message_reply_markup(chat_id, msg_id, reply_markup=admin_markup())
        except Exception:
            pass
        return

    if data == "admin_broadcast":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_broadcast')
        bot.send_message(chat_id, "📢 أرسل الرسالة/الصورة لتوزيعها على الجميع:")
        return

    if data == "admin_announcement":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_announcement_text')
        bot.send_message(chat_id, "📣 أرسل نص الإعلان المثبت الجديد:")
        return

    if data == "admin_stats":
        if not is_admin(user_id):
            return
        u_cnt = get_user_count()
        o_cnt = get_all_orders_count()
        a_cnt = get_accepted_orders_count()
        d_inc = get_daily_income()
        m_inc = get_monthly_income()
        stats_text = (
            f"📊 <b>إحصائيات البوت العامة</b>\n\n"
            f"👥 عدد المستخدمين: {u_cnt}\n"
            f"📦 إجمالي الطلبات: {o_cnt}\n"
            f"✅ الطلبات المقبولة: {a_cnt}\n"
            f"💰 دخل اليوم: {d_inc} جنيه\n"
            f"💰 دخل الشهر: {m_inc} جنيه"
        )
        bot.send_message(chat_id, stats_text, parse_mode='HTML')
        return

    if data == "admin_change_cash":
        markup = types.InlineKeyboardMarkup()
        for k, name in SECTION_ARABIC_NAMES.items():
            markup.add(types.InlineKeyboardButton(f"تغيير كاش {name}", callback_data=f"admin_change_cash_sec_{k}"))
        bot.send_message(chat_id, "اختر القسم لتغيير رقم الكاش:", reply_markup=markup)
        return

    if data.startswith("admin_change_cash_sec_"):
        sec = data.replace("admin_change_cash_sec_", "")
        set_state(user_id, 'admin_change_cash', cash_section=sec)
        bot.send_message(chat_id, f"💰 أرسل رقم الكاش الجديد لقسم {SECTION_ARABIC_NAMES.get(sec, sec)}:")
        return

    if data == "admin_change_price":
        markup = types.InlineKeyboardMarkup()
        for skey, sdata in SERVICES.items():
            markup.add(types.InlineKeyboardButton(f"تعديل {sdata['name']}", callback_data=f"admin_set_price_{skey}"))
        bot.send_message(chat_id, "اختر الخدمة لتعديل سعرها:", reply_markup=markup)
        return

    if data.startswith("admin_set_price_"):
        skey = data.replace("admin_set_price_", "")
        set_state(user_id, 'admin_set_price_value', price_service_key=skey)
        bot.send_message(chat_id, f"💲 أرسل السعر الجديد لـ {skey}:")
        return

    if data == "admin_search_user":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_search_user_id')
        bot.send_message(chat_id, "🔍 أرسل ID المستخدم للبحث عنه:")
        return

    if data == "admin_ban":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_ban_id')
        bot.send_message(chat_id, "🚫 أرسل ID المستخدم المراد حظره:")
        return

    if data == "admin_unban":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_unban_id')
        bot.send_message(chat_id, "✅ أرسل ID المستخدم المراد فك حظره:")
        return

    if data == "admin_msg_user":
        if not is_admin(user_id):
            return
        set_state(user_id, 'admin_msg_user_id')
        bot.send_message(chat_id, "📨 أرسل ID المستخدم المراد مراسلته:")
        return

    if data.startswith("admin_quick_ban_"):
        if not is_admin(user_id):
            return
        target = int(data.replace("admin_quick_ban_", ""))
        conn = get_db_connection()
        conn.execute('UPDATE users SET is_banned = 1 WHERE user_id = ?', (target,))
        conn.commit()
        conn.close()
        bot.answer_callback_query(call.id, "✅ تم حظر المستخدم!")
        return

    if data.startswith("admin_quick_unban_"):
        if not is_admin(user_id):
            return
        target = int(data.replace("admin_quick_unban_", ""))
        conn = get_db_connection()
        conn.execute('UPDATE users SET is_banned = 0 WHERE user_id = ?', (target,))
        conn.commit()
        conn.close()
        bot.answer_callback_query(call.id, "✅ تم فك الحظر!")
        return

    if data.startswith("admin_quick_msg_"):
        if not is_admin(user_id):
            return
        target = int(data.replace("admin_quick_msg_", ""))
        set_state(user_id, 'admin_msg_user_text', msg_target_id=target)
        bot.send_message(chat_id, f"✏️ أرسل الرسالة للمستخدم {target}:")
        return


if __name__ == '__main__':
    print("⏳ جاري تشغيل البوت...")
    init_database()
    print("✅ تم تجهيز قاعدة البيانات وتطبيق التغييرات بنجاح.")
    bot.infinity_polling(skip_pending=True)
