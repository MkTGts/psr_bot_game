import logging
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.kyboards import yes_no_kb, game_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_bot_choice, get_winner, _key_user_choice, pars_wb
from services.db import create_db, verification, insert_datas
from data.user_config import users


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

create_db()

router = Router()  # инициализация роутера


# хэндрел на команду старт
@router.message(Command(commands="start"))
async def process_command_start(message: Message):
    '''#if str(message.from_user.id) not in users:
    users[str(message.from_user.id)] = users.get(str(message.from_user.id), {
        "in_pars": False,  # режим парсинга или нет
        "id_wb": 0,  # последний подаваемый id
        "count": 0  # общее количество запросов на парсинг
    })'''

    create_db()  # создает базу данных

    # проверка есть ли пользователь в базе и если нет, то занесение в базу
    if not verification(tg_id=message.from_user.id):
        insert_datas("false", str(message.from_user.id), '0', 0)

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
    

# хэндлер на запуск парсера
@router.message(F.text == LEXICON_RU["but_pars_wb"])
async def start_parser(message: Message):

    #users[str(message.from_user.id)]["in_pars"] = True  # выставляет значение запуска парсера


    await message.answer(
        text=LEXICON_RU["if_pars_wb"],  # просит юзера ввести id товара
    )
    logger.info(f'Start parser user id - {message.from_user.id}')  # запись в лог


# хэндлер работы парсера
@router.message(lambda x: x.text and x.text.isdigit() and len(x.text) == 9)  # проверка что id соответсвует требованию
async def working_parser(message: Message):
    if users[str(message.from_user.id)]["in_pars"] == True:  # если запущен редим парсера wb
        users[str(message.from_user.id)]["id_wb"] = message.text  # присваевает запрозенный id
        res = pars_wb(message.text)  # парсит данные по id через класс парсера
        await message.answer(
            text=res #LEXICON_RU["if_pars_wb"],
        )
        users[str(message.from_user.id)]["in_pars"] = False  # закрывает режим парсинга wb
        users[str(message.from_user.id)]["count"] += 1
        logger.info(f'Working parser user id - {message.from_user.id}')  # лог запущенного парсера
    else:
        await message.answer(
            text=LEXICON_RU["incorrect_id"],
        )
        users[str(message.from_user.id)]["in_pars"] = False  # закрывает режим парсинга wb
