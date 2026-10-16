from decorator import command
### -- Размещайте свои команды здесь --
@command(name='chizhik_says',desc='чижик говорит: ...', args=True)
def chizhik_says(arg):
    text = ' '.join(arg)
    print(f"Чижик говорит: {text}")
@command(name='hangman', desc='виселица: угадай слово по буквам', args=False)
def hangman():
    import random
    import time

    words = ['python', 'арч', 'чижик', 'пыжуля', 'терминал', 'декоратор',
             'оболочка', 'гитхаб', 'клавиатура', 'монитор', 'кофе', 'код']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    used = []

    print("🎮 Игра: ВИСЕЛИЦА")
    print(f"Слово из {len(word)} букв. У тебя {tries} попыток.")
    print("Пиши по одной букве. 'выход' — сдаться.\n")

    while tries > 0 and '_' in guessed:
        print('  ' + ' '.join(guessed))
        letter = input("Буква: ").lower().strip()

        if letter == 'выход':
            print(f"Сдался. Слово было: {word}")
            return

        if len(letter) != 1 or not letter.isalpha():
            print("Одна буква, пожалуйста.")
            continue

        if letter in used:
            print(f"'{letter}' уже была!")
            continue

        used.append(letter)

        if letter in word:
            for i, ch in enumerate(word):
                if ch == letter:
                    guessed[i] = ch
            print(f"✅ Есть! '{letter}' в слове.")
            time.sleep(0.5)
        else:
            tries -= 1
            print(f"❌ Нет. Осталось попыток: {tries}")
            time.sleep(0.5)

    print()
    if '_' not in guessed:
        print(f"🎉 Победа! Слово: {word}")
    else:
        print(f"💀 Проиграл. Слово было: {word}")
        time.sleep(1)
        print("Илья: ну ты и лох 🙂")