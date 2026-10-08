### -- Словари для команд --
COMMANDS = {}
COMMANDSWARGS = {}
COMMANDS_META = {}

### -- Декоратор --
def command(name:str, desc:str="описание не указано", args:bool=False, aliases:list=None):
    """**Декоратор который автоматически добавляет команды в словари**
    
    :param name: имя команды
    :type name: str
    :param desc: описание команды
    :type desc: str
    :param args: принимает ли аргументы
    :type args: bool
    :param aliases: алиасы команд
    :type aliases: list

    Как использовать:
    - Перед функцией добавьте `@command()`
    - Необходимо передать аргументы:
        - `name` - название команды, по этому слову она вызывается в оболочке
        - `desc` - описание команды, используется в `gen_help()`
        - `args` - нужны ли аргументы, в зависимости от значения ставит в разные словари:
            - Если `True` - кидает в `COMMANDSWARGS` (команды в которые передаются аргументы)
            - Если `False` - кидает в `COMMANDS` (команды в которые никогда не передаются аргументы)
        - `aliases` - ссылки указывающие на ту же функцию, но с другим именем
    .. note::
        Если ваша функция стоит с args=True, то необходимо принятие аргументов. Неправильно: `my_command(): ...` Правильно: `my_command(args): ...`

    Как он это делает:
    - Кидает по нужный словарям команды
    - Также про алиасы не забывает
    - Создаёт мета-теги для `gen_help()`
    

    :raises ValueError: если команда с таким именем уже есть"""
    def decorator(func):
        cmd_name = name
        if cmd_name in COMMANDS_META or cmd_name in COMMANDSWARGS or cmd_name in COMMANDS:
            raise ValueError(f"{cmd_name} already exists")
        if args:
            COMMANDSWARGS[cmd_name] = func
        else:
            COMMANDS[cmd_name] = func
        if aliases:
            for alias in aliases:
                if args:
                    COMMANDSWARGS[alias] = func
                else:
                    COMMANDS[alias] = func
        COMMANDS_META[cmd_name] = {
            'aliases': aliases or [],
            'desc': desc,
            'args': args
        }
        
        return func
    return decorator