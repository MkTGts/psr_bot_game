from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


# создание кнопока в ответ на поедложение начать игру
button_yes = KeyboardButton(text=LEXICON_RU["but_yes"])
button_no = KeyboardButton(text=LEXICON_RU["but_no"])
button_pars = KeyboardButton(text=LEXICON_RU["but_pars_wb"])

# инициализация биледра 
yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, button_pars, width=3)

yes_no_kb = yes_no_kb_builder.as_markup(  # создание клавиатуры начать игру да нет
    one_time_keyboard=True,
    resize_keyboard=True
)



#создане игровых кнопок
but1 = KeyboardButton(text=LEXICON_RU["rock"])
but2 = KeyboardButton(text=LEXICON_RU["paper"])
but3 = KeyboardButton(text=LEXICON_RU["scissors"])

# инициализация билдера клавиатуры
game_kb_builder = ReplyKeyboardBuilder()
game_kb_builder.row(
    but1,
    but2,
    but3,
    width=1
)

game_kb = game_kb_builder.as_markup(  # создание игровой клавиатуры
    resize_keyboard=True
)






