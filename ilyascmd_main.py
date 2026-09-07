#!/usr/bin/env python3

'''Здарова, весь код ниже. Он полностью читаемый, если конечно понимаешь пайтон.
Оболочка называется ilya's:cmd_ (в коде используется переменная).
В разработке помогал Дипсик, он не писал код, он обьяснял фишки.
короч не порти код и всё такое, изменяй чё хочешь только если знаешь чё делаешь
Код создан на линуксе(быть точнее на arch).
Соответственно код может либо криво, либо вообще не работать на винде или где ты сидишь'''

## $#####{ -<( Python )>- }#####$
# ilyascmd_main.py
import time
import os
import random
import readline

try:
    import configCMD
except ModuleNotFoundError:
    raise SystemExit('ModuleNotFoundError: Файл configCMD.py не найден. Работа оболочки невозможна.')

class IlyaDoesNotExistError(Exception):
    pass

dont_dare = configCMD.KILL_BLACK_LIST
dead_list = configCMD.DEAD_LIST
WHY = 'You shouldn\'t do that. Return him.'
if 'ilya' in dead_list:
    raise IlyaDoesNotExistError(WHY) # YOU DO THAT?

HISTORY_FILE = os.path.expanduser('~/.history_file')

try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    open(HISTORY_FILE, 'w').close()
    readline.read_history_file(HISTORY_FILE)

col = configCMD.col
rng = configCMD.rng

# используется для определения имя компьютера, не путать с юзернеймом(он чуть пониже)
HOSTNAME = os.uname().nodename

# используется для определения юзернэйма, не удивляйся что в оболочке находишься ТЫ
USER = os.getlogin()
if USER.lower() == 'ilya':
    USER = f'{col.b}{col.bd}Илья [🛠️]'
# это для диалогов(ещё проще: чтоб мне пальцы не сломать)
ilya = f"{col.g}{col.bd}ilya:{col.w}"

ilyascmd = f"{col.g}{col.bd}ilya's{col.v}:{col.c}cmd_{col.w}"

prompt = configCMD.PROMPT

# приветствие
print(
    f"{col.rbd}[!!! ДАННАЯ ОБОЛОЧКА В ОЧЕНЬ РАННОЙ РАЗРАБОТКЕ, БАГИ ЛАГИ ПРИКОЛЫ В КОМПЛЕКТЕ !!!]{col.w}",
    f"\n{USER}, {col.w}добро пожаловать в оболочку {ilyascmd}! {col.b}[сделанно на Arch Linux]{col.w}",
    f"\nЭта оболочка написана на {col.y}{col.bd}Python 3! {col.v} v???? (Без версии, обновляется часто){col.w}",
    f"\nНапишите {col.g}help{col.w} для вывода помощи.",
    f'Вы используете устаревшую версию оболочки, соответствено, новых команд тут нету. \nПерейдите на Ilya\'s:Shell для нормальной работы'
    )

# импорт calc1.py если неудача то ошибка при запуске
is_calc_exist = True
try:
    import calc1
except ModuleNotFoundError:
    is_calc_exist = False
    print(f"{col.rbd}Файл «calc1.py» не был найден.{col.w}")
    print(f"{col.rbd}Проверьте целостность файла. (может быть он переименован?){col.w}")
# except ImportError:
#     is_calc_exist = False
#     print(f"{col.rbd}Модуль «calcdotpy» в файле «calc1.py» не был найден.{col.w}")
#     print(f"{col.rbd}Проверьте целостность файла и модуля. (может быть он переименован?){col.w}")

is_pif_exists = True
try:
    import pifagor
except ModuleNotFoundError:
    is_pif_exists = False
    print(f"{col.rbd}Файл «pifagor.py» не был найден.{col.w}")
    print(f"{col.rbd}Проверьте целостность файла. (может быть он переименован?){col.w}")
# except ImportError:
#     is_pif_exists = False
#     print(f"{col.rbd}Модуль «pifagorpy» в файле «pifagor.py» не был найден.{col.w}")
#     print(f"{col.rbd}Проверьте целостность файла и модуля. (может быть он переименован?){col.w}")

# список мёртвых, используется в kill, revive и dead_list

class KillAttemptError(Exception):
    pass
# функция kill, используется чтоб два раза не писать код если есть аргументы и если нет
def kill(target): 
    dont_dare.extend(['чижик', 'chizhik', 'илья', 'ilya', "пыжуля", "чыжык", USER])
    target_ls = target.lower().strip()
    # ????
    if any(bad_name in target_ls for bad_name in dont_dare):
        raise KillAttemptError(f"{col.rbd}{random.choice([ # передаю привет дипсику
            'don\'t dare',
            'не смей',
            'Молодец! Ты сломал оболочку!!!',
            'something is coming',
            '???',
            'nosey, aren\'t we?',
            'не убивай меня',
            'зачем меня убивать?',
            'проверь шкаф'
        ])}{col.w}")

    # если жив
    elif target not in dead_list and target:
        confirm = input(f"{ilya} Ты УВЕРЕН? {col.g}[Y/N] {col.w}")
        if confirm in ['y', 'Y', 'д', 'Д']:
            print( f"{col.rbd}ilya: {target} УБИТ!!!{col.w}")
            dead_list.append(target)
        else:
            print(f"{col.g}{col.bd}ilya: {col.v}{target} остаётся в живых!!{col.w}") 
    # если сдох
    elif target_ls in dead_list:
        print(f"{ilya} как я смогу убить мёртвого?") 

# функция revive, используется с той же целью что и kill(см выше)
def revive(target):
    print('...')
    time.sleep(4)
    if target.lower().strip() in dead_list:
        dead_list.remove(target.lower().strip())
        print(f"{ilya} Кто это?{col.w}")
        time.sleep(3)
        print(f"{USER}: Где?{col.w}")
        time.sleep(2)
        print(f"{ilya} Там! Наверху!!{col.w}")
        time.sleep(2)
        print('...')
        time.sleep(3)
        print(f"{col.rbd}???: {col.w}{col.y}It is {target}...{col.w}")
        time.sleep(3)
        print(f"{col.y}{col.bd}{target}: {col.w}{col.y}Я..{col.w}")
        time.sleep(1)
        print(f"{col.y}{col.bd}{target}: {col.w}{col.y}Я снова в живых??{col.w}")
        time.sleep(3)
        print(f"{col.y}{col.bd}{target}: {col.w}{col.y}Спасибо, тебе {USER}.{col.w}")
        time.sleep(2)
        print(f"{col.y}{col.bd}{target}: {col.w}{col.y}Ты спас меня..{col.w}")
        time.sleep(5)
    else:
        print(f"{col.rbd}???: {col.y}{target} is already alive.{col.w}")
        time.sleep(2)

# основной цикл
while True:
    try:
        strout = input(f"{prompt}> ") # {prompt}> <команда> (промпт изменять в файле configCMD.py)
        parts = strout.split()
        cmd = parts[0]
        arg = parts[1:]
        cmd = cmd.lower().strip()
    # при ctrl + c
    except KeyboardInterrupt:
        raise SystemExit(f'\n{col.rbd}ilya: ЗА ЧТО ???!?!?!?!??!ауш;?*:№?*руниаыгаиуиргаыивсицуисты{col.w}')

    except EOFError:
        print(f'\n{col.rbd}ilya: ЗА ЧТО ???!?!?!?!??!ауш;?*:№?*руниаыгаиуиргаыивсицуисты{col.w}')
        break

    # если пусто(да из-за этого ломается код, и я это починил)
    except IndexError:
        continue

    readline.write_history_file(HISTORY_FILE) # для сохранения команд

    # дальше идут команды
    if strout == 'help':
        print(f"{ilya} Вот тебе список:")
        print('kill <цель> - убить кого-нибудь, убивать мертвого нельзя\n',
        'revive <цель> - возродить кого-нибудь, возрождать живого тоже нельзя\n',
        'dead_list - список мёртвых\n',
        'help - показать это меню\n',
        'whoami - показать юзернейм\n'
        'exit/quit/break - выйти из оболочки ;(\n',
        'clear - очистить консоль\n',
        'version - версия оболочки\n',
        'calc/calc1/calc1.py/calculator - запуск скрипта calc1.py (через вызов функции, напряму. невозможно)\n',
        'rng/random/randomizer <min> <max> - вывести рандомное число в заданом диапазоне\n',
        'pif/pifagor - запуск скрипта pifagor.py (через вызов функции, напрямую невозможно)')
    
    elif cmd == 'kill':
        if arg:
            target = ''.join(arg)
            kill(target) 
        else:
            target = input(f"{ilya} Кого ты хочешь {col.r}убить? {col.w}")
            kill(target)

    elif cmd in ['revive','respawn','rebirth']:
        if arg:
            target = ''.join(arg)
            revive(target)
        else:
            target = input(f"{col.rbd}???: {col.y} Enter Their Name: {col.w}")
            revive(target)

    elif strout == 'whoami':

        # омг посхалко
        if USER == f'{col.b}{col.bd}Илья [🛠️]':
            print(f"{ilya} Тебя зовут.. {col.w}")
            time.sleep(2)
            print(f"{ilya} Стоп чё?. {col.w}")
            time.sleep(1)
            print(f"{ilya} Тебя зовут {col.b}{col.bd}Илья [🛠️]?{col.w}")
            time.sleep(3)
            print(f"{ilya} Это либо совпадение, либо..{col.w}")
            time.sleep(2)
            print(f'{ilya} ..либо ты являешься {col.b}{col.bd}создателем{col.w}. ')
            time.sleep(2)
            print(f"И да меня зовут {col.b}{col.bd}Илья [🛠️]{col.w} и я это все пишу в VSCodium(вскод но на линуксе, да я на арче :Р).")
            print('Я думаю что это можно считать за пасхалку!')
            time.sleep(4)
            print('Молодец что нашёл!!')
            time.sleep(2)
        else:
            print(f"{ilya} Тебя зовут {col.y}{col.bd}{USER}.")

    elif cmd == 'dead_list':
        if dead_list:
            print(f"{col.rbd}ilya: Убитые: {', '.join(dead_list)}{col.w}")
        else:
            print(f"{col.g}{col.bd}ilya: Все живы.{col.w}")

    # может криво работать
    elif cmd == 'clear':
        os.system('clear')

    elif cmd == 'version':
        print(f"{ilyascmd} {col.v}{col.bd}v????{col.w} User: {USER}.{col.w}")

    elif cmd in ['exit','quit','break']:
        print(f"{col.rbd}ilya: ЗА ЧТО ???!?!?!?!??!ауш;?*:№?*руниаыгаиуиргаыивсицуисты{col.w}")
        break

    elif cmd in ['calc', 'calculator', 'calc1', 'calc1.py']:
        try:
            calc1.calcdotpy() # см. calc1.py для калькулятора
        except NameError:
            print(f"{col.rbd}Файл «calc1.py» не был найден. Проверьте наличие файла в директории.{col.w}")

    elif cmd in ['rng','random', 'randomizer']:
        if not arg[0] or not arg[1:]:
            print(f"{ilya} Синтаксис: rng <min> <max>")
        else:
            try:
                rng.min = int(arg[0])
                rng.max = int(arg[1])
                rng.result = random.randint(rng.min, rng.max)
                rng.phrase = random.choice(rng.list)
                print(f'{ilya}{rng.phrase}{rng.result}')
            except ValueError:
                print(f"{ilya} Только числа. Минимальное число не может быть больше максимального. Синтаксис: rng <min> <max>")
            except IndexError:
                print(f"{ilya} Строго пробелы. Синтаксис: rng <min> <max>")

    elif cmd in ['pif', 'pifagor']:
        # if is_pif_exists == True:
        pifagor.pifagorpy() # см. pifagor.py для вычисления теоремы пифагора
        # else:
        #     print(f'{col.rbd}')

    elif cmd == 'guess':
        guess_num = random.randint(1, 10000)
        guess_out = 0
        print(f'{ilya} Правила: Я загадываю число, а ты отгадываешь.',
        f'\nЧтобы отгадать число тебе нужно будет писать число, а я говорю больше оно или меньше.',
        f'\nИ так до тех пор пока ты не отгадаешь число. Для старта напиши любое число. (Число от 1 до 10тыс.)')
        while True:
            try:
                guess_out = int(input(f'{ilyascmd}{col.v} [GUESS]{col.w} > '))
                if guess_out > guess_num:
                    print(f'{ilya} {col.rbd}Число меньше!{col.w}')
                elif guess_out < guess_num:
                    print(f'{ilya} {col.g}{col.bd}Число больше!{col.w}')
                elif guess_out == guess_num:
                    print(f'{ilya} {col.y}{col.bd}Победа!!{col.w}')
                    break
            except ValueError:
                print(f'{ilya} {USER}, вводи числа!')
            except KeyboardInterrupt:
                print(f'{ilya} Сдался? Ну, ладно..')
                break
            except EOFError:
                print(f'{ilya} почему?? ;(')
    else:
        print(configCMD.COMMAND_NOT_FOUND)
