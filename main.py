import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from data_config.config import Config, load_config
from handlers import user_handlers, other_handlers


# инициализация логгера
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="a",
    encoding="utf-8",
    format= '[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s'
)


# основная функция
async def main():
    logger.info("Старт бота.")  # лог старта бота

    config: Config = load_config()  # загружен конфиг в переменную

    bot = Bot(  # инициализация бота
        token=config.tg_bot.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    dp = Dispatcher()  # инициализация диспетчера

    # регистрация роутеров в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)  # удаление апдейтов в ожидании
    await dp.start_polling(bot)  # запуск поллинга


try:
    asyncio.run(main())
except Exception as err:
    logger.critical(f"Stop! Error {err}")


