from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
# from tg_bot.config import load_config, x


# config = load_config(".env")


keyboard: list = [
    [
        KeyboardButton(
            text="Запустить терминал",
            web_app=WebAppInfo(url='https://serene-halva-5eb619.netlify.app/'),
        )
    ]
]

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True
)
