### -- Словари для команд --
COMMANDS = {}
COMMANDSWARGS = {}
COMMANDS_META = {}

### -- Декоратор --
def command(name:str, desc:str="null", args:bool=False, aliases:list=None):
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