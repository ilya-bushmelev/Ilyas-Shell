#!/usr/bin/env python3
# ^^^ шебанг ^^^

#           / - IlyasShell.py ------------- [-][0][X] \
#           |   ### ---------------------------- ###  |
#           |   ### -----<( Ilya's:Shell )>----- ###  |
#           |   ### -------- ( v2.1 ) ---------- ###  |
#           |   ### ---------------------------- ###  |
#           \ --------------------------------------- /

#   Приветствую в коде оболочки! Код полностью читаемый и понятный.
#   Задумка была чтобы быть улучшенной версией ilya's:cmd_, которая работает через модули.
#   Кстати, посмотри configShell.py там находится конфиг оболочки! 
#   Пожалуйста, не удаляй его. Без него оболочка не будет работать.
#   Оболочка поддерживает пользовательские команды, создавай их в userCommands.py,
#   гайд по настройке кастомных команд есть в README.md.

#   Ссылки проекта:
#     GitHub Репозиторий: https://github.com/ilya-bushmelev/Ilyas-Shell
#     Сайт (GitHub Pages): https://ilya-bushmelev.github.io/Ilyas-Shell
#     Автор проекта: https://github.com/ilya-bushmelev
#
#   С юбилейной 600-й строкой? 

### -- Импорты --
import os
import random
import time
import readline
import traceback
import sys
from datetime import datetime
import getpass
from typing import Callable
from decorator import command, COMMANDS, COMMANDSWARGS, COMMANDS_META

### -- Импорт конфига --
CFG_TEMPLATE = r'''
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
INCLUDE_CALC1 = False
INCLUDE_PIFAGOR = False
USER_COMMANDS_ENABLED = False
'''

try:
    import configShell
except ModuleNotFoundError:
    confirm_create_new_cfg = input('Файл конфига не найден. Создать новый? [Д/Y] ')
    if confirm_create_new_cfg.lower() in ['y','д','yes','да']:
        with open('configShell.py', 'w', encoding='utf-8') as f:
            f.write(CFG_TEMPLATE)
        try:
            import configShell
        except Exception:
            raise SystemExit("Произошла повторная ошибка. Проверьте конфиг")
    else:
        print("Без конфига оболочка не может работать.")

### -- Низкоуровневое логирование --
DEBUG_MODE = False
if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    DEBUG_MODE = True
def log(msg:str, lvl:int=0) -> None:
    if not DEBUG_MODE:
        return
    else:
        colors = {
            0: col.g,
            1: col.y, 
            2: col.r,
            3: col.r + stl.bd,
        }
        color = colors.get(lvl, col.w)
        print(f'{color}│ [{lvl}]{rs.all} {msg}')

### -- Переменные --
__version__ = 'v2.1'

col = configShell.col
bg = configShell.bg
stl = configShell.stl
rs = configShell.rs
prompt = configShell.PROMPT
dead_list = configShell.DEAD_LIST
dont_dare = configShell.KILL_BLACK_LIST
log("loaded many things from config (styles, prompt, dead_list, dont_dare)")

USER = getpass.getuser()
log(f"define user name ({USER})")

ilya = f'{col.g}{stl.bd}Илья:{rs.all}'

log("loaded dont_dare")
dont_dare.extend(['чижик', 'chizhik', 'илья', 'ilya', "пыжуля", 'pyzhulya', "чыжык", USER])
history_file = os.path.expanduser('~/.history_file')

log('trying to open history file...')
try:
    readline.read_history_file(history_file)
    log('succesfully readed history file')
except FileNotFoundError:
    log("history file doesn't exist, creating a new one", 1)
    open(history_file, 'w').close()
    readline.read_history_file(history_file)
    log('succesfully readed history file')
### -- ??? --
if any(YOU_HAD_IT_COMING in dont_dare for YOU_HAD_IT_COMING in dead_list):
    at = 0
    log("something gone wrong", 3)
    log('YOU HAD IT COMING', 3)
    while at < 10:
        try:
            
            for ayli in range(3):
                print('.', end='', flush=True)
                time.sleep(1)
            print('\b\b\b' + ' ' * 3 + '\b\b\b', end='', flush=True)
            time.sleep(1)
            at += 1
        except (KeyboardInterrupt, EOFError):
            raise SystemExit("\rYOU HAD IT COMING")
    raise SystemExit("\rYOU HAD IT COMING")


log("commands decorator loaded")

### -- Генератор списка помощи по командам (просто читает COMMANDS_META) --
def gen_help() -> str:
    lines = []
    for cmd,meta in COMMANDS_META.items():
        desc = meta.get('desc','без описания')
        aliases = meta.get('aliases',[])
        args = meta.get('args',False)
        name_part = stl.bd + col.g + cmd + ("/" + "/".join(aliases) if aliases else "") + rs.all
        pre_result = name_part + (" <аргументы> " if args else "")
        padding = max(1, 50 - len(pre_result))
        result = pre_result + " " * padding + f"{col.c} - {desc}{rs.all}"
        lines.append(result)
    return "\n".join(lines)
   

### -- Команды --
@command(name='help',desc="показать это меню")
def shelp() -> None: # к сожалению help() нельзя использовать, он зарезервирован
    print(f"{ilya} Вот тебе список:\n{gen_help()}")

class KillAttemptError(Exception):
    pass
@command(name='kill',desc='убить кого-нибудь',args=True)
def kill(target:str='Null') -> None:
    if target == 'Null' or not target:
        log('no args were given', 1)
        target = input(f'{ilya} Кого хочешь {col.r}{stl.bd}убить? {rs.all}{col.y}')
    else:
        target = ' '.join(target)
    target_ls = target.lower().strip()
    global dead_list
    if any(bad_name in target_ls for bad_name in dont_dare):
        log("DO NOT", 3)
        raise KillAttemptError(f"{col.r}{stl.bd}{random.choice([
            'don\'t dare',
            'не смей',
            'Молодец! Ты сломал оболочку!!!',
            'something is coming',
            '???',
            'nosey, aren\'t we?',
            'не убивай меня',
            'зачем меня убивать?',
            'проверь шкаф',
            'бибизяка! 🐦 (это моя оболочка, я имею право писать всё что угодно)',
            'НЕ УБИВАЙ ПОЖАЖА'
        ])}{col.w}") #! передаю привет дипсику
    elif target_ls not in dead_list:
        confirm = input(f'{ilya}Ты уверен? [y/N] ').lower().strip()
        if confirm in ['y', 'yes', 'д', 'да']:
            dead_list.append(target_ls)
            log(f'added {target_ls} to dead_list')
            print(f'{ilya}{target} УБИТ!')
        else:
            print(f'{ilya}{col.v}{target} остаётся в живых!{rs.all}')
    else:
        log("target already in dead_list", 1)
        print(f'{ilya} как я смогу убить мёртвого?')
@command(name='revive',desc='возродить кого-нибудь',args=True,aliases=['rebirth','respawn'])
def revive(target:str='Null') -> None:
    global dead_list
    if target == 'Null' or not target:
        log("no args were given", 1)
        target = input(f'{col.r}{stl.bd}???: {col.y}target to revive: {stl.bd}')
    else:
        target = ' '.join(target)
    print('...')
    time.sleep(4)
    if target.lower().strip() in dead_list:
        dead_list.remove(target.lower().strip())
        print(f"{ilya} Кто это?{rs.all}")
        time.sleep(3)
        print(f"{USER}: Где?{rs.all}")
        time.sleep(2)
        print(f"{ilya} Там! Наверху!!{rs.all}")
        time.sleep(2)
        print('...')
        time.sleep(3)
        print(f"{col.r}{stl.bd}???: {rs.stl}{col.y}It is {target}...{rs.all}")
        time.sleep(3)
        print(f"{col.y}{stl.bd}{target}: {rs.stl}{col.y}Я..{rs.all}")
        time.sleep(1)
        print(f"{col.y}{stl.bd}{target}: {rs.stl}{col.y}Я снова в живых??{rs.all}")
        time.sleep(3)
        print(f"{col.y}{stl.bd}{target}: {rs.stl}{col.y}Спасибо, тебе {USER}.{rs.all}")
        time.sleep(2)
        print(f"{col.y}{stl.bd}{target}: {rs.stl}{col.y}Ты спас меня..{rs.all}")
        time.sleep(5)
    else:
        print(f"{col.r}{stl.bd}???: {col.y}{target} is already alive.{rs.all}")
        time.sleep(2)
@command(name='version',desc='показать версию')
def version() -> None:
    print(f'{col.g}{stl.bd}💚 Ilya\'s{col.c}:Shell{col.y} Версия оболочки: {__version__}')
@command(name='whoami',desc="показать имя пользователя")
def whoami() -> None:
    # омг посхалко
    if USER == f'ilya':
        log("you discovered an easter egg!")
        print(f"{ilya} Тебя зовут.. {col.w}")
        time.sleep(2)
        print(f"{ilya} Стоп чё?. {col.w}")
        time.sleep(1)
        print(f"{ilya} Тебя зовут {col.b}{stl.bd}Илья [🛠️]?{col.w}")
        time.sleep(3)
        print(f"{ilya} Это либо совпадение, либо..{col.w}")
        time.sleep(2)
        print(f'{ilya} ..либо ты являешься {col.b}{stl.bd}создателем{col.w}. ')
        time.sleep(2)
        print(f"И да меня зовут {col.b}{stl.bd}Илья [🛠️]{col.w} и я это все пишу в VSCodium(вскод но на линуксе, да я на арче :Р).")
        print('Я думаю что это можно считать за пасхалку!')
        time.sleep(4)
        print('Молодец что нашёл!!')
        time.sleep(2)
    else:
        print(f"{ilya} Тебя зовут {col.y}{stl.bd}{USER}.")
@command(name="guess",desc='игра в "угадай число"',args=True)
def guess(arg:str='Null'):
    if arg == 'Null' or not arg:
        log('no args were given', 1)
        max_num = int(input(f'{ilya} Перед началом, напиши число лимита: '))
    else:
        max_num = int(arg[0])
    guess_num = random.randint(1, max_num)
    guess_out = 0
    print(f'{ilya} Правила: Я загадываю число, а ты отгадываешь.',
        f'\nЧтобы отгадать число тебе нужно будет писать число, а я говорю больше оно или меньше.',
        f'\nИ так до тех пор пока ты не отгадаешь число. Для старта напиши любое число. ')
    ходы = 0
    while True:
        try:
            guess_out = int(input(f'{prompt}{col.v} [GUESS]{col.w} > '))
            ходы += 1
            if guess_out > guess_num:
                print(f'{ilya} {col.r}{stl.bd}Число меньше!{col.w}')
            elif guess_out < guess_num:
                print(f'{ilya} {col.g}{stl.bd}Число больше!{col.w}')
            elif guess_out == guess_num:
                print(f'{ilya} {col.y}{stl.bd}Победа!!{col.w} Ходы: {ходы}.')
                break
        except ValueError:
            print(f'{ilya} {USER}, вводи числа!')
        except KeyboardInterrupt:
            print(f'{ilya} Сдался? Ну, ладно..')
            break
        except EOFError:
            print(f'{ilya} почему?? ;(')
@command(name='echo',desc="вывести текст",args=True)
def echo(arg:str) -> None:
    echout = ' '.join(arg)
    print(f'{echout}')
@command(name='rng',desc="вывод случайного числа",args=True,aliases=['random','randomizer'])
def rng(arg:str) -> None:
    if len(arg) < 2:
        print(f"{ilya} Синтаксис: rng <min> <max>")
        return
    try:
        min_val = int(arg[0])
        max_val = int(arg[1])
        rsult = random.randint(min_val, max_val)
        phrases = ['Твое рандомное число: ', 'тебе выпало: ', 'лох :)))) ', 'Your RNG number: ']
        print(f'{ilya}{random.choice(phrases)}{rsult}')
    except ValueError:
        print(f"{ilya} Вводи только числа! Минимальное число не может быть больше максимального!!")
    except IndexError:
        print(f'{ilya} (илья не придумал сообщение)')
@command(name='dead_list',desc="вывод списка мёртвых")
def fdead_list() -> None:
    global dead_list
    if dead_list:
        print(f"{col.r}{stl.bd}Илья: Убитые: {', '.join(dead_list)}{col.w}")
    else:
        print(f"{col.g}{stl.bd}Илья: Все живы.{col.w}")
@command(name="binary",desc="перевод в двоичную систему и наоборот",args=True)
def binary_code(arg:str) -> None:
    try:
        flag = arg[0]
        raw_num:int = int(arg[1])
        raw_str = arg[1]
        if flag == '-e':
            bin_num = []
            while raw_num > 0:
                ostatok = raw_num % 2
                if ostatok == 1:
                    bin_num.append(str(1))
                else:
                    bin_num.append(str(0))
                raw_num //= 2
            result = ''.join(reversed(bin_num))
            print(f'{ilya} Результат: {result}')
        elif flag == '-d':
            print(f'{ilya} Результат: {int(raw_str, 2)}')
    except ValueError:
        print(f'{ilya} error')
    except IndexError:
        print(f'{ilya} error')
@command(name='hex',desc="перевод шестнадцатеричную систему и наоборот",args=True)
def hex_code(arg:str) -> None:
    try:
        flag = arg[0]
        number = arg[1]
        if flag == '-e':
            hex_result = hex(int(number))
        elif flag == '-d':
            number = number.replace('0x', '').replace('0X', '')
            hex_result = int(number, 16)
        print(f'{ilya} Результат: {hex_result}')
    except (ValueError, IndexError):
        print(f'{ilya} error')
@command(name='eval',desc="опасная команда для вызова eval()", args=True)
def ebal(arg:str) -> None:
    if not arg:
        print("ты аргументы забыл")
        return
    if configShell.EVAL_ENABLED == True and arg[0] == '--i-know-what-i-am-doing':
        eval(' '.join(arg[1:]))
    else:
        print(f'{stl.bd + col.r}Данное действие запрещено. Проверьте флаг --i-know-what-i-am-doing и переменную EVAL_ENABLED в конфиге{rs.all}')
@command(name='time',desc="вывод текущего времени и даты",aliases=["date",'timedate','datetime'])
def timedate():
    now = datetime.now()
    time_ = now.strftime("%H:%M:%S")
    date = now.strftime("%d.%m.%Y")
    print(f"{col.c + stl.bd}⌚ Время: {time_} {rs.fg + col.g}📆 Дата: {date}{rs.all}")
@command(name='pwd',desc="вывод текущего пути")
def pwd():
    print(os.getcwd())
@command(name='cd',desc="поменять директорию",args=True)
def cd(arg:str) -> None:
    if not arg:
        target = os.path.expanduser('~')
    else:
        target = ' '.join(arg)
        target = os.path.expanduser(target)
        if not os.path.isabs(target):
            target = os.path.join(os.getcwd(), target)
        target = os.path.normpath(target)
    
    if os.path.isdir(target):
        os.chdir(target)
        print(f'{col.g}Перешёл в: {target}{rs.all}')
    else:
        print(f'{col.r}Директория не найдена: {target}{rs.all}')
@command(name='ls',desc="просмотр файлов в текущей директории",args=True)
def ls(arg:str) -> None:
    path = ' '.join(arg) if arg else '.'
    path = os.path.expanduser(path)
    try:
        items = os.listdir(path)
        for item in sorted(items):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f'{col.b}{item}/{rs.all}')  # синий для папок
            elif os.access(full_path, os.X_OK):
                print(f'{col.g}{item}*{rs.all}')  # зелёный для исполняемых
            else:
                print(item)
    except FileNotFoundError:
        print(f'{col.r}Не найдено: {path}{rs.all}')
    except PermissionError:
        print(f'{col.r}Нет доступа: {path}{rs.all}')
@command(name='touch',desc="создание файла",args=True)
def touch(arg:str) -> None:
    if not arg:
        print("Нет аргументов")
        return
    try:
        for file in arg:
            file = os.path.expanduser(file)
            if os.path.exists(file):
                print(f"{file} уже существует")
                continue
            open(file, 'w').close()
    except FileNotFoundError:
        print(f"Директория не найдена.")
    except PermissionError:
        print(f"Нет прав к директории.")
@command(name="mkdir",desc='создание директории',args=True)
def mkdir(arg:str) -> None:
    if not arg:
        print("Нет аргументов")
        return
    
    for folder in arg:
        folder = os.path.expanduser(folder)
        
        if os.path.exists(folder):
            print(f"{folder} уже существует")
            continue
        
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"Создана директория: {folder}")
        except FileNotFoundError:
            print(f"Не удалось создать: {folder}")
        except PermissionError:
            print(f"Нет прав: {folder}")
@command(name='rm',desc="удаление файлов",args=True)
def rm(arg:str) -> None:
    try:
        if not arg:
            print("Синтаксис: rm <файлы ЧЕРЕЗ ПРОБЕЛ> (rm file1 file2 ...)")
        for file in arg:
            log(f"{file} deleted")
            os.remove(file)
    except IsADirectoryError:
        print(f"Это директория: {file} (подсказка: используйте rmdir)")
    except FileNotFoundError:
        print(f"Не найдена: {file}")
    except PermissionError:
        print(f"Нет прав: {file}")
@command(name='rmdir',desc="рекурсивное удаление директории", args=True)
def rmdir(arg:str) -> None:
    try:
        if not arg:
            print("Синтаксис: rmdir <путь>")
            return
        folder = arg[0]
        import shutil
        confirm = input(f"Внимание! Папка {folder} будет удалена {stl.bd + col.r}рекурсивно и безвозвратно{rs.all}!\nВы уверены что хотите продолжить? [y/N] ")
        if confirm.lower() in ['y','yes','д','да']:
            shutil.rmtree(folder)
            print(f"Удалена со всем содержимым: {folder}")
        else:
            return
    except FileNotFoundError:
        print(f"Не найдена: {folder}")
    except PermissionError:
        print(f"Нет прав: {folder}")
@command(name='exit',desc='выйти из оболочки :(',aliases=['quit','break','leave','goodbye'])
def shell_exit():
    log('exit because exit command', 1)
    print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
    sys.exit(0)

### -- Импорт кастомных команд --
if configShell.USER_COMMANDS_ENABLED == True:
    try:
        import userCommands
        log('loaded userCommands.py')
    except ModuleNotFoundError:
        log('userCommands.py not found, skipping', 1)
    except Exception as e:
        print(f'{col.y}{stl.bd}Ошибка в userCommands.py:{rs.all} {type(e).__name__}: {e}')

### -- calc1.py и pifagor.py --
try:
    if configShell.INCLUDE_CALC1 == True:
        import calc1
        @command(name='calc',desc='простой калькулятор',aliases=['calculator','calc1.py'])
        def startcalc():
            calc1.calcdotpy()
    if configShell.INCLUDE_PIFAGOR == True:
        import pifagor
        @command(name='pif',desc="простой решатель теоремы пифагора", aliases=['pifagor'])
        def startpif():
            pifagor.pifagorpy()
except (AttributeError, ImportError):
    print("При импорте некоторых дополнений возникла ошибка.")

###  -- Основной цикл --
def StartShell() -> None: 
    # приветствие при запуске StartShell()
    print(f'{stl.bd}Добро пожаловать в оболочку {col.g}{stl.bd}💚 Ilya\'s{col.c}:Shell 🐚,{col.w}')
    print(f'улучшенную версию {col.g}{stl.bd}ilya\'s{col.v}:{col.c}cmd_{col.w} написаную на {col.y}Python 3.14!{rs.all}')
    while True:
        try:
            cwd = os.getcwd()
            home = os.path.expanduser('~')
            if cwd.startswith(home):
                cwd = '~' + cwd[len(home):]
            log('waiting for user input')
            inp = input(f'{prompt} {col.c}{cwd}{rs.all}> ').split()
            cmd = inp[0]
            arg = inp[1:]
            log("input completed")
        except KeyboardInterrupt:
            log('exit because interupt', 1)
            print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except EOFError:
            log('exit because eof', 1)
            print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except IndexError:
            log('IndexError', 1)
            continue
        readline.write_history_file(history_file)
        log('write history file')
        try:
            if cmd in COMMANDSWARGS:   
                log(f"executing {cmd} with args {arg}") 
                COMMANDSWARGS[cmd](arg)
            elif cmd in COMMANDS:
                log(f"executing {cmd}")
                COMMANDS[cmd]()
            else:
                print(configShell.COMMAND_NOT_FOUND)
        except Exception as e:
            if DEBUG_MODE:
                log("an exception has ocurred", 2)
                traceback.print_exc()
            else:
                EType = type(e).__name__
                print(f'{col.y}{stl.bd}{random.choice([
                    f'Опа! Ошибка...',
                    f'Чё? Опять?',
                    f'Ломай! Ломай! Мы же миллионеры!',
                    f'о нет ошыбка',
                    f'404 Error: Message Not Found',
                    f'программисты перед сном вместо овец считают ошибки',
                    f'-1 нервная клетка',
                    f'Удачи разобраться',
                    f'(илья снова не придумал сообщение)'
                ])}{rs.all}')
                print(f'{stl.bd}{col.v if EType != "KillAttemptError" else col.r}{EType}{rs.all}: {e}{rs.all}')
# -- Запуск --
if __name__ == '__main__': # Если файл запущен напрямую, то запускается StartShell() и оболочка начинает работать
    log("starting StartShell()")
    StartShell()