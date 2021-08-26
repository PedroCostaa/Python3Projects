from random import randrange


def play():
    print("""
Welcome to the guessing game!
You can choose between 3 levels of difficulty, easy/medium/hard.
You always start with 100 points, and lose depending on the level of difficulty each time you guess the wrong number
Easy: You have 5 guesses and the secret number is between 1 and 10
Medium: You have 4 guesses and the secret number is between 1 and 12
Hard: You have 3 guesses and the secret number is between 1 and 15
    """)

    guess_limit = 0
    secret_number = 0
    difficulty = ""
    total_points = 100
    points_lost_per_round = 0
    while True:
        difficulty = input("Choose the game level of difficulty (easy,medium,hard): ").upper()
        if difficulty == "EASY":
            guess_limit = 5
            secret_number = randrange(1, 11)
            points_lost_per_round = total_points / 5
            print("EASY MODE ON")
            print("")
            break
        elif difficulty == "MEDIUM":
            guess_limit = 4
            secret_number = randrange(1, 13)
            points_lost_per_round = total_points / 4
            print("MEDIUM MODE ON")
            print("")
            break
        elif difficulty == "HARD":
            guess_limit = 3
            secret_number = randrange(1, 16)
            points_lost_per_round = total_points / 3
            print("HARD MODE ON")
            print("")
            break
        else:
            print("CHOOSE A VALID OPTION")

    for guess_count in range(guess_limit):
        guess = int(input(f"Your {guess_count + 1}º Guess: "))
        if guess <= 0:
            print("Only permitted numbers above 0, and 0 not included")
            continue
        elif guess < secret_number:
            print("Guessed number is less than the secret number!")
            total_points -= points_lost_per_round
        elif guess > secret_number:
            print("Guessed number is bigger than the secret number!")
            total_points -= points_lost_per_round
        elif guess == secret_number:
            print("")
            print("You Win (͡°͜ʖ͡°)")
            print(f"Total points: {round(total_points)}")
            break
        print(f"Current points: {round(total_points)}")
    else:
        print("")
        print(f"You lose!, The secret number was {secret_number} ¯\_(ツ)_/¯")


if __name__ == "__main__":
    play()
