# Для аннотаций
from typing import Callable
class col:
    r = '\033[91m'  # красный
    g = '\033[92m'  # зелёный
    y = '\033[93m'  # жёлтый
    b = '\033[94m'  # синий
    c = '\033[96m'  # голубой
    v = '\033[95m'  # фиолетовый
    o = '\033[38;5;214m'  # оранжевый
    w = '\033[37m'  # белый
    gray = '\033[90m'  # серый
    black = '\033[30m'


class bg:
    r = '\033[101m'
    g = '\033[102m'
    y = '\033[103m'
    b = '\033[104m'
    c = '\033[106m'
    v = '\033[105m'
    o = '\033[48;5;214m'
    w = '\033[107m'
    gray = '\033[100m'
    black = '\033[40m'


class stl:
    bd = '\033[1m'
    dim = '\033[2m'
    italic = '\033[3m'
    underl = '\033[4m'
    blink = '\033[5m'
    reverse = '\033[7m'
    hidden = '\033[8m'


class rs:
    all = '\033[0m'
    fg = '\033[39m'
    bg = '\033[49m'
    stl = '\033[22m'


PROMPT = f'{col.g}{stl.bd}Ilya\'s{col.c}:Shell{rs.all}'
DEAD_LIST: list[str] = []
COMMAND_NOT_FOUND = f'{col.r}{stl.bd}Илья: Команда не найдена!{rs.all}'
KILL_BLACK_LIST: list[str] = []
EVAL_ENABLED = False

# -- Пользовательские команды --
class USER_COMMANDS:
    enabled = False

    # -- Команды --
    def chizhik_says(arg):
        text = ' '.join(arg)
        print(f"Чижик говорит: {text}")
    # -- Ссылки на команды --
    list_with_args:dict[str,Callable] = {
        'chizhik_says': chizhik_says
    }; list_:dict[str,Callable] = {
        # пока здесь пусто ;(
    }
