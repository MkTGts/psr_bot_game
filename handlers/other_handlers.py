from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


router = Router()  # подключение роутера

# хэндлер для сообщений не подходящих не под какуб категорию
@router.message()
async def other_all_mess(message: Message):
    await message.answer(
        text=LEXICON_RU["other"]
    )