import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import Config, load_config
from core.handlers.main_menu_handlers import router


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    config: Config = load_config(".env")
    bot: Bot = Bot(token=config.bot.token, parse_mode="HTML")
    dp: Dispatcher = Dispatcher()

    dp.include_routers(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
