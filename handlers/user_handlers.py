import logging
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.kyboards import yes_no_kb, game_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner, _key_user_choice


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



router = Router()  # инициализация роутера


# хэндрел на команду старт
@router.message(Command(commands="start"))
async def process_command_start(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=yes_no_kb
    )
    logger.info(f'Start bot user id - {message.from_user.id}')


# хэндлер на команду хелп
@router.message(Command(commands="help"))
async def process_command_help(message: Message):
    await message.answer(
        text=LEXICON_RU["/help"],
        reply_markup=yes_no_kb
    )
    logger.info(f'Help bot user id - {message.from_user.id}')


# хэндлер на согласие пользователя сыграть
@router.message(F.text == LEXICON_RU["but_yes"])
async def but_yes_to_game(message: Message):
    await message.answer(
        text=LEXICON_RU["if_yes"],
        reply_markup=game_kb
    )
    logger.info(f'Start game user id - {message.from_user.id}')


# хэндлер на отказ пользователя сыграть 
@router.message(F.text == LEXICON_RU["but_no"])
async def but_no_to_game(message: Message):
    await message.answer(
        text=LEXICON_RU["if_no"]
    )
    logger.info(f'Cancel game user id - {message.from_user.id}')


# хэндлер на любую из игровых кнопок 
@router.message(F.text.in_([LEXICON_RU["rock"],
                            LEXICON_RU["paper"],
                            LEXICON_RU["scissors"]]))
async def click_any_game_but(message: Message):
    bot_choice = get_bot_choice()
    user_choice = _key_user_choice(message.text)
    await message.answer(
        text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}'
    )
    winner = get_winner(user_choice, bot_choice)
    await message.answer(
        text=LEXICON_RU[winner],
        reply_markup=yes_no_kb
    )
    