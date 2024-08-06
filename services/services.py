import random
from lexicon.lexicon import LEXICON_RU


# функция выбора ботом
def get_bot_choice() -> str:
    return random.choice(["rock", "paper", "scissors"])


# функция приобразует данное пользователем значение в ключ из словаря лексикона
def _key_user_choice(user_answer) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
        

# функция определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    win = [
        ["rock", "scissors"], ["scissors", "paper"], ["paper", "rock"]
        ]
    
    if [user_choice, bot_choice] in win:
        return "user_win"
    elif [bot_choice, user_choice] in win:
        return "bot_win"
    else:
        return "no_winner"



