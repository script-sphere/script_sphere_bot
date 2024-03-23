from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from tg_bot.config import Config, load_config


config: Config = load_config(".env")


keyboard: list = [
    [
        KeyboardButton(
            text="Запустить терминал",
            web_app=WebAppInfo(url=config.bot.app_url),
        )
    ]
]

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
