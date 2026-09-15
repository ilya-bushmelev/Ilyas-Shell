import sys
import os

class IlyasShell:
    def __init__(self):
        pass
    def cprint(self, *messages, **settings):
        raw_text = ' '.join(messages)
        text = f'{"\033[1m" if settings.get("bold") else ""}{raw_text}{"\033[0m"}'
        print(text)
    def __call__(self):
        print("привет")
        while True:
            raw_input = input("аы аы аы ")
