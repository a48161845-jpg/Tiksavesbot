"""
Инлайн-клавиатуры и текстовые константы, которые показываются пользователю.
Здесь нет бизнес-логики — только разметка интерфейса.
"""
import urllib.parse
from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import SUPPORT_USERNAME, CRYPTO_DONATE_URL, BOT_SHARE_URL, STARS_MIN, STARS_MAX
from helpers import html_escape, code

# ================== STATS / TOP KEYBOARDS ==================
def stats_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📅 День", callback_data="ad:stats:d"),
                InlineKeyboardButton(text="🗓 Неделя", callback_data="ad:stats:n"),
                InlineKeyboardButton(text="🗓 Месяц", callback_data="ad:stats:m"),
            ],
            [
                InlineKeyboardButton(text="📆 Год", callback_data="ad:stats:y"),
                InlineKeyboardButton(text="📊 Всё время", callback_data="ad:stats:all"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Назад", callback_data="ad:back"),
                InlineKeyboardButton(text="❌ Закрыть", callback_data="ad:close"),
            ],
        ]
    )

def top_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📅 День", callback_data="ad:top:d"),
                InlineKeyboardButton(text="🗓 Неделя", callback_data="ad:top:n"),
                InlineKeyboardButton(text="🗓 Месяц", callback_data="ad:top:m"),
            ],
            [
                InlineKeyboardButton(text="📆 Год", callback_data="ad:top:y"),
                InlineKeyboardButton(text="📊 Всё время", callback_data="ad:top:all"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Назад", callback_data="ad:back"),
                InlineKeyboardButton(text="❌ Закрыть", callback_data="ad:close"),
            ],
        ]
    )

# ================== START ==================
START_TEXT = (
    "👋 Привет!\n\n"
    "Я скачиваю видео, фото (слайдшоу) и музыку из TikTok.\n"
    "📎 Просто отправь ссылку — остальное сделаю сам.\n\n"
    "🧾 Помощь: /help\n"
    "💛 Поддержать бота: /donate\n"
    "🆘 Поддержка: /support\n"
    "📊 Моя статистика: /stats"
)

# ================== DONATE ==================
def donate_main_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⭐ Донат звёздами", callback_data="donate:stars")],
            [InlineKeyboardButton(text="💲 Донат криптой", url=CRYPTO_DONATE_URL)],
            [InlineKeyboardButton(text="🆘 Поддержка", callback_data="donate:support")],
        ]
    )

def stars_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⭐ 10", callback_data="stars:10"),
                InlineKeyboardButton(text="⭐ 50", callback_data="stars:50"),
                InlineKeyboardButton(text="⭐ 100", callback_data="stars:100"),
            ],
            [
                InlineKeyboardButton(text="⭐ 250", callback_data="stars:250"),
                InlineKeyboardButton(text="⭐ 500", callback_data="stars:500"),
                InlineKeyboardButton(text="⭐ 1000", callback_data="stars:1000"),
            ],
            [InlineKeyboardButton(text="✍️ Другая сумма", callback_data="stars:custom")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="donate:back")],
        ]
    )

DONATE_TEXT = (
    "📌 <b>Поддержать бота</b>\n\n"
    "Спасибо, что пользуешься ботом! Донат помогает держать всё стабильно и быстро:\n"
    "• хостинг и трафик 24/7\n"
    "• поддержка прокси/апи\n"
    "• новые функции и улучшения\n\n"
    "Выбери удобный способ 👇"
)
STARS_MENU_TEXT = (
    "⭐ <b>Telegram Stars</b>\n\n"
    "Самый быстрый способ поддержки прямо в Telegram.\n"
    f"Выбери сумму ({STARS_MIN}-{STARS_MAX} ⭐) или введи свою:"
)
SUPPORT_TEXT = (
    "🆘 <b>Поддержка</b>\n\n"
    f"Если есть вопросы/проблемы - пиши сюда: {html_escape(SUPPORT_USERNAME)}\n"
    "Сразу укажи ссылку и что именно не работает 🙌"
)
SHARE_TEXT = "Нашел топового бота для скачивания видео и фото из TikTok. Переходи ☝️"

# ================== HELP ==================
HELP_TEXT = (
    "🧾 <b>Помощь по боту</b>\n\n"
    "📎 Просто отправь ссылку на TikTok — бот предложит варианты.\n\n"
    "Кнопки и что они делают:\n"
    "• 🎬 Скачать видео — пришлю видео без водяных знаков (если доступно)\n"
    "• 🖼️ Скачать фото — выбор фото или всё сразу (слайдшоу)\n"
    "• 🎵 Скачать музыку — скачивание звука/музыки\n"
    "• 💛 Донат — поддержка проекта\n"
    "• 🆘 Поддержка — связь с админом\n\n"
    "⚠️ Лимиты:\n"
    "• Частые запросы ограничены кулдауном\n"
    "• Много фото за раз — лимит объёма"
)

def help_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎬 Скачать видео", callback_data="help:video"),
                InlineKeyboardButton(text="🖼️ Скачать фото", callback_data="help:photo"),
            ],
            [
                InlineKeyboardButton(text="🎵 Скачать музыку", callback_data="help:music"),
            ],
            [
                InlineKeyboardButton(text="⚠️ Лимиты", callback_data="help:limits"),
            ],
            [
                InlineKeyboardButton(text="💛 Донат", callback_data="help:donate"),
                InlineKeyboardButton(text="🆘 Поддержка", callback_data="help:support"),
            ],
            [
                InlineKeyboardButton(text="❌ Закрыть", callback_data="help:close"),
            ],
        ]
    )

def help_section_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬅️ Назад", callback_data="help:back"),
                InlineKeyboardButton(text="❌ Закрыть", callback_data="help:close"),
            ]
        ]
    )

HELP_SECTIONS = {
    "video": (
        "🎬 <b>Скачать видео</b>\n\n"
        "1) Отправь ссылку на TikTok\n"
        "2) Выбери «Скачать видео»\n"
        "3) Получишь видео в чате"
    ),
    "photo": (
        "🖼️ <b>Скачать фото</b>\n\n"
        "1) Отправь ссылку на TikTok с слайдшоу\n"
        "2) Выбери фото по номерам или скачай всё\n"
        "3) Получишь альбом с фото"
    ),
    "music": (
        "🎵 <b>Скачать музыку</b>\n\n"
        "Нажми «Скачать музыку» после обработки ссылки — пришлю аудио файл."
    ),
    "limits": (
        "⚠️ <b>Лимиты</b>\n\n"
        "Слишком частые запросы ограничены кулдауном — подожди немного и попробуй снова.\n"
        "При систематическом флуде возможна временная блокировка."
    ),
    "donate": (
        "💛 <b>Донат</b>\n\n"
        "Поддержка проекта через Stars или крипту. Спасибо!"
    ),
    "support": (
        "🆘 <b>Поддержка</b>\n\n"
        f"Пиши: {html_escape(SUPPORT_USERNAME)}\n"
        "Укажи ссылку и что не работает."
    ),
}

# ================== POST-DOWNLOAD / VIDEO KEYBOARDS ==================
def _share_url() -> str:
    """Ссылка «Поделиться»: в шаре подставляется url, текст — про бота (ссылка вставляется сама)."""
    share_url = urllib.parse.quote_plus(BOT_SHARE_URL)
    share_text = urllib.parse.quote_plus(SHARE_TEXT)
    return f"https://t.me/share/url?url={share_url}&text={share_text}"

def post_download_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💛 Донат", callback_data="donate:open"),
                InlineKeyboardButton(text="🔗 Поделиться", url=_share_url()),
            ]
        ]
    )

def under_video_kb(has_music: bool = False) -> InlineKeyboardMarkup:
    """Кнопки под скачанным видео: Музыка (если есть), Донат, Поделиться."""
    row: List[InlineKeyboardButton] = []
    if has_music:
        row.append(InlineKeyboardButton(text="🎵 Музыка", callback_data="dl:audio"))
    row.append(InlineKeyboardButton(text="💛 Донат", callback_data="donate:open"))
    row.append(InlineKeyboardButton(text="🔗 Поделиться", url=_share_url()))
    return InlineKeyboardMarkup(inline_keyboard=[row])

def video_choice_kb() -> InlineKeyboardMarkup:
    """Только «Скачать видео» и «Отмена» — кнопка музыки перенесена под видео."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎬 Скачать видео", callback_data="vd:video")],
            [InlineKeyboardButton(text="❌ Отмена", callback_data="vd:cancel")],
        ]
    )

# ================== ADMIN UI ==================
def admin_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📊 Статистика", callback_data="ad:stats"),
                InlineKeyboardButton(text="🏆 Топ", callback_data="ad:top"),
            ],
            [
                InlineKeyboardButton(text="🚫 Бан-лист", callback_data="ad:banlist"),
                InlineKeyboardButton(text="🗄 Дамп БД", callback_data="ad:dbfile"),
            ],
            [
                InlineKeyboardButton(text="📌 Напоминание", callback_data="ad:reminder"),
                InlineKeyboardButton(text="📢 Реклама", callback_data="ad:advert"),
            ],
            [
                InlineKeyboardButton(text="🧾 Команды", callback_data="ad:help"),
                InlineKeyboardButton(text="❌ Закрыть", callback_data="ad:close"),
            ],
        ]
    )

def admin_back_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⬅️ Назад", callback_data="ad:back"),
                InlineKeyboardButton(text="❌ Закрыть", callback_data="ad:close"),
            ]
        ]
    )

ADMIN_MENU_TEXT = (
    "🛠 <b>Админ-панель</b>\n\n"
    "Кнопки ниже:\n"
    "• 📊 Статистика - выбор периода\n"
    "• 🏆 Топ - лидеры по периоду\n"
    "• 🚫 Бан-лист - список активных банов\n"
    "• 🗄 Дамп БД - скачать дамп базы данных\n"
    "• 📌/📢 - рассылки с подтверждением\n"
    "• 🧾 Команды - полный список команд\n"
)

ADMIN_HELP_TEXT = (
    "🧾 <b>Команды администратора</b>\n\n"
    "📊 Статистика\n"
    f"• {code('/stats d')} {code('/stats n')} {code('/stats m')} {code('/stats y')} {code('/stats all')}\n"
    f"• {code('/stats 2026-02-01 2026-02-07')} (диапазон)\n\n"
    "🏆 Топ\n"
    f"• {code('/top d')} {code('/top n')} {code('/top m')} {code('/top y')} {code('/top all')}\n"
    f"• {code('/top 2026-02-01 2026-02-07')} (диапазон)\n\n"
    "🚫 Баны\n"
    f"• {code('/ban ID 2h причина')}\n"
    f"• {code('/unban ID')}\n"
    f"• {code('/banlist')}\n"
    f"• {code('/baninfo ID')}\n\n"
    "🗄 База данных\n"
    f"• {code('/dbfile')} — дамп БД файлом\n"
    f"• {code('/dblog')} — отчёт в лог-канал\n\n"
    "👤 Пользователь\n"
    f"• {code('/info ID')}\n\n"
    "📣 Рассылка\n"
    f"• {code('/broadcast текст')}\n"
    "• /reminder_message\n"
    "• /advertisement_message\n"
)

def admin_broadcast_confirm_kb(kind: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Отправить", callback_data=f"ad:send:{kind}"),
            ],
            [
                InlineKeyboardButton(text="❌ Закрыть", callback_data="ad:close"),
            ],
        ]
    )

def broadcast_cancel_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⛔ Остановить рассылку", callback_data="ad:bcancel")],
        ]
    )
