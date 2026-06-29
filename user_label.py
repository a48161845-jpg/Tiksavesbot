"""
Резолвер отображаемого имени пользователя (username / имя+фамилия / id)
для логов и админ-команд.
"""
from aiogram import Bot


async def resolve_user_label(bot: Bot, uid: int) -> str:
    try:
        chat = await bot.get_chat(uid)
        username = getattr(chat, "username", None)
        first = getattr(chat, "first_name", None)
        last = getattr(chat, "last_name", None)
        if username:
            return f"@{username} ({uid})"
        name = " ".join([x for x in [first, last] if x]).strip()
        if name:
            return f"{name} ({uid})"
    except Exception:
        pass
    return f"{uid}"
