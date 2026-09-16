#!/usr/bin/env python3
# ^^^ шебанг ^^^

                ### ---------------------- ###  
                ### --<( Ilya's:Shell )>-- ### 
                ### ---------------------- ###

#   Приветствую в коде оболочки! Код полностью читаемый и понятный.
#   Задумка была чтобы быть улучшенной версией ilya's:cmd_, которая работает через модули.
#   Кстати, посмотри configShell.py там находится конфиг оболочки! 
#   Пожалуйста, не удаляй его. Без него оболочка не будет работать

### -- Импорты --
import os
import random
import time
import readline
import traceback
import sys

# -- Импорт конфига --
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
DEAD_LIST = []
COMMAND_NOT_FOUND = f'{col.r}{stl.bd}Илья: Команда не найдена!{rs.all}'
KILL_BLACK_LIST = []

# -- Пользовательские команды --
class USER_COMMANDS:
    enabled = False

    # -- Команды --
    def chizhik_says(arg):
        text = ' '.join(arg)
        print(f"Чижик говорит: {text}")
    # -- Ссылки на команды --
    list_with_args = {
        'chizhik_says': chizhik_says
    }; list_ = {
        # пока здесь пусто ;(
    }
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
try:
    import calc1
    import pifagor
except ModuleNotFoundError:
    pass

### -- Переменные --
__version__ = 'v1.2'

col = configShell.col
bg = configShell.bg
stl = configShell.stl
rs = configShell.rs
prompt = configShell.PROMPT
dead_list = configShell.DEAD_LIST
dont_dare = configShell.KILL_BLACK_LIST

USER = os.getlogin()

ilya = f'{col.g}{stl.bd}Илья:{rs.all}'

dont_dare.extend(['чижик', 'chizhik', 'илья', 'ilya', "пыжуля", 'pyzhulya' "чыжык", USER])
history_file = os.path.expanduser('~/.history_file')

try:
    readline.read_history_file(history_file)
except FileNotFoundError:
    open(history_file, 'w').close()
    readline.read_history_file(history_file)

INTERACTIVE = False
### -- ??? --
if any(YOU_HAD_IT_COMING in dont_dare for YOU_HAD_IT_COMING in dead_list):
    at = 0
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
        
### -- Команды --
def shelp(): # к сожалению help() нельзя использовать, он зарезервирован
    if INTERACTIVE == True:
        print(f"{ilya} Вот тебе список:\n",
            'kill <цель>                        - убить кого-нибудь, убивать мертвого нельзя\n',
            'revive <цель>                      - возродить кого-нибудь, возрождать живого тоже нельзя\n',
            'dead_list                          - список мёртвых\n',
            'help                               - показать это меню\n',
            'whoami                             - показать юзернейм\n',
            'version                            - показать версию оболочки',
            'exit/quit/break                    - выйти из оболочки ;(\n',
            'calc/calculator                    - запуск скрипта calc1.py (через вызов функции, напрямую невозможно)\n',
            'rng/random/randomizer <min> <max>  - вывести рандомное число в заданом диапазоне\n',
            'pif/pifagor                        - запуск скрипта pifagor.py (через вызов функции, напрямую невозможно)\n',
            'guess <максимальное число>         - игра в угадай число\n',
            'echo <текст>                       - вывести текст\n',
        )
    elif INTERACTIVE == False:
        print(f"{ilya} Вот тебе список:\n",
            f"{stl.bd}StartShell()              - запустить оболочку в интерактивном режиме{rs.all}\n",
            "kill(['<цель>'])           - убить кого-нибудь, убивать мертвого нельзя\n",
            "revive(['<цель>'])         - возродить кого-нибудь, возрождать живого тоже нельзя\n",
            "fdead_list()               - список мёртвых\n",
            "shelp()                    - показать это меню\n",
            "whoami()                   - показать юзернейм\n"
            "calcdotpy()                - запуск скрипта calc1.py, импортировать перед запуском\n",
            "rng([<min>, <max>])        - вывести рандомное число в заданном диапазоне\n",
            "pifagorpy()                - запуск скрипта pifagor.py, импортировать перед запуском\n",
            "guess([<макс. число>])     - игра в угадай число\n",
            "echo(['<текст>'])          - вывести текст, конкретно здесь это бесполезно, используйте лучше print()"
        )

class KillAttemptError(Exception):
    pass
def kill(target='Null'):
    if target == 'Null' or not target:
        target = input(f'{ilya} Кого хочешь {col.r}{stl.bd}убить? {rs.all}{col.y}')
    else:
        target = ' '.join(target)
    target_ls = target.lower().strip()
    global dead_list
    if any(bad_name in target_ls for bad_name in dont_dare):
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
            dead_list.append(target)
            print(f'{ilya}{target} УБИТ!')
        else:
            print(f'{ilya}{col.v}{target} остаётся в живых!{rs.all}')
    else:
        print(f'{ilya} как я смогу убить мёртвого?')

def revive(target='Null'):
    global dead_list
    if target == 'Null' or not target:
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
def version():
    print(f'{col.g}{stl.bd}💚 Ilya\'s{col.c}:Shell{col.y} Версия оболочки: {__version__}')
def whoami():
    # омг посхалко
    if USER == f'ilya':
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

def guess(arg='Null'):
    if arg == 'Null' or not arg:
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
def echo(arg):
    echout = ' '.join(arg)
    print(f'{echout}')
def rng(arg):
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
def fdead_list():
    global dead_list
    if dead_list:
        print(f"{col.r}{stl.bd}Илья: Убитые: {', '.join(dead_list)}{col.w}")
    else:
        print(f"{col.g}{stl.bd}Илья: Все живы.{col.w}")
def binary_code(arg):
    try:
        flag = arg[0]
        num = int(arg[1])
        binstr = arg[1]
        if flag == '-e':
            bin_num = []
            while num > 0:
                ostatok = num % 2
                if ostatok == 1:
                    bin_num.append(str(1))
                else:
                    bin_num.append(str(0))
                num //= 2
            print(f'{ilya} Результат: {''.join(reversed(bin_num))}')
        elif flag == '-d':
            print(f'{ilya} Результат: {int(binstr, 2)}')
    except ValueError:
        print(f'{ilya} error')
    except IndexError:
        print(f'{ilya} error')
### -- Словарики команд --
COMMANDSWARGS = {
    'kill':kill,
    'revive':revive,
    'rspawn':revive,
    'rebirth':revive,
    'echo':echo,
    'rng':rng,
    'random':rng,
    'randomizer':rng,
    'binary':binary_code,
    'guess':guess
}
COMMANDS = {
    'help':shelp,
    'whoami':whoami,
    'calc':calc1.calcdotpy,
    'calc1':calc1.calcdotpy,
    'calc1.py':calc1.calcdotpy,
    'calculator':calc1.calcdotpy,
    'pif':pifagor.pifagorpy,
    'pifagor':pifagor.pifagorpy,
    'dead_list':fdead_list,
    'version':version
}

#  -- Основной цикл --
def StartShell(mode='normal'):
    global INTERACTIVE
    INTERACTIVE = True
    if mode == 'debug':
        debug = True
    # приветствие при запуске StartShell()
    print(f'{stl.bd}Добро пожаловать в оболочку {col.g}{stl.bd}💚 Ilya\'s{col.c}:Shell 🐚,{col.w}')
    print(f'улучшенную версию {col.g}{stl.bd}ilya\'s{col.v}:{col.c}cmd_{col.w} написаную на {col.y}Python 3.14!{rs.all}')
    if configShell.USER_COMMANDS.enabled == True:
        COMMANDS.update(configShell.USER_COMMANDS.list_ )
        COMMANDSWARGS.update(configShell.USER_COMMANDS.list_with_args)
        print(f'{stl.bd}{col.g}Включенны пользовательские команды.{rs.all}')
    while True:
        try:
            if debug: print('waiting for user input')
            inp = input(f'{prompt} > ').split()
            cmd = inp[0]
            arg = inp[1:]
        except KeyboardInterrupt:
            if debug: print('exit because interupt')
            INTERACTIVE = False
            print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except EOFError:
            if debug: print('exit because eof')
            INTERACTIVE = False
            print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except IndexError:
            if debug: print('IndexError')
            continue
        if debug: print('write history file')
        readline.write_history_file(history_file)
        try:
            if cmd in COMMANDSWARGS:    
                COMMANDSWARGS[cmd](arg)
            elif cmd in COMMANDS:
                COMMANDS[cmd]()
            elif cmd in ['exit', 'break', 'quit']:
                INTERACTIVE = False
                # raise SystemExit(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
                print(f'{col.r}{stl.bd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
                break
            else:
                print(configShell.COMMAND_NOT_FOUND)
        except Exception as e:
            if debug:
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
    mode_for_load = sys.argv[1] if len(sys.argv) else 'normal'
    StartShell(mode_for_load)
