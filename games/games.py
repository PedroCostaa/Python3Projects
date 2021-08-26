import hangmanBeta
import guessing
import time


def loading():
    spaces = 0
    timer = 0
    while timer < 20:
        print("\b " * spaces + ".", end="", flush=False)
        spaces = spaces + 1
        time.sleep(0.1)
        timer += 1
        if spaces > 5:
            print("\b \b" * spaces, end="")
            spaces = 0


print("""
Choose your game:
1 - HANGMAN
2 - GUESSING
""")

while True:
    option = int(input("Your option (1 or 2): "))
    if option == 1:
        print("Loading HANGMAN (͡°͜ʖ͡°)", end="")
        loading()
        print("")
        hangmanBeta.play()
        break
    elif option == 2:
        print("Loading GUESSING (͡°͜ʖ͡°)", end="")
        loading()
        print("")
        guessing.play()
        break
    else:
        print("Invalid Option ¯\_(ツ)_/¯")
