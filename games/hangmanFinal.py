from random import randrange


def play():
    print(f"""
{"_" * 100}    
                                WELCOME TO HANGMAN (͡°͜ʖ͡°)
            TO START THE GAME JUST TYPE "START" ON THE CONSOLE OR "QUIT" TO QUIT THE GAME
{"_" * 100}
""")

    words = (["DOG", "HAWK", "SHARK"], ["JUPITER", "MARS", "VENUS"], ["COMPUTER", "CHAIR", "PENCIL"])
    secret_word = ""
    word_size_underscore = ["_"]
    guesses = ""
    guessed_letter = ""
    hint = ""
    hint_option = ""
    option = 0
    chances = 5
    wrong_guesses = 0
    right_guesses = 1
    secret_word_len = 0
    x = 0
    y = 0

    while option != "QUIT":
        option = input(">>> ").upper().replace(" ", "")

        if option == "START":
            x = randrange(len(words))
            y = randrange(len(words[x]))
            secret_word = words[x][y]
            secret_word_len = len(secret_word)
            word_size_underscore = ["_" for letra in secret_word]

            if x == 0:
                hint = "Animal"
            elif x == 1:
                hint = "Planet"
            elif x == 2:
                hint = "Object"

            while hint_option != "NO" or hint_option != "YES":
                print("_" * 100)
                print("DO YOU WANT THE HINT (YES, NO)? ")
                hint_option = input(">>> ").upper().replace(" ", "")

                if hint_option == "YES":
                    print(f"THE WORD IS A(AN) {hint}")
                    break
                elif hint_option == "NO":
                    print("¯\_(ツ)_/¯")
                    break
                else:
                    print("NOT A VALID OPTION")

            print("_" * 100)

            while wrong_guesses < chances:
                guessed_letter = input("Your guess >>> ").upper().replace(" ", "")

                if right_guesses == secret_word_len:
                    print("YOU WIN (͡°͜ʖ͡°)")
                    break

                elif guessed_letter in guesses:
                    print("YOU ALREADY GUESSED THAT LETTER")

                elif guessed_letter in secret_word:
                    index = 0

                    for letra in secret_word:
                        if guessed_letter == letra:
                            word_size_underscore[index] = letra
                            right_guesses += 1

                        index += 1
                    print("_" * 100)
                    print("""                                   """, str(word_size_underscore).replace("'", "").replace("[", "").replace(",", "").replace("]", ""))
                    guesses += guessed_letter

                else:
                    wrong_guesses += 1
                    guesses += guessed_letter

            else:
                print("_" * 100)
                print("YOU LOSE ¯\_(ツ)_/¯")
                print(f"THE SECRET WORD WAS: {secret_word}")
                break

        elif option == "QUIT":
            print("Adios")
        else:
            print("CHOOSE A VALID OPTION (START, QUIT)")


if __name__ == "__main__":
    play()