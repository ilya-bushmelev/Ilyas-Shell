from decorator import command
### -- Размещайте свои команды здесь --
@command(name='chizhik_says',desc='чижик говорит: ...', args=True)
def chizhik_says(arg):
    text = ' '.join(arg)
    print(f"Чижик говорит: {text}")