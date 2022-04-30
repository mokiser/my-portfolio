import random as rn


def in_game():
    print("Welcome to logic game Bagels.\n"
          " I am thinking of a __-digit number with no repeated digits.\n"
          "Try to guess what it is. Here are some clues\n"
          "When I say    That means\n"
          "Pico         One digit is correct but in the wrong position.\n"
          "Fermi        One digit is correct and in the right position.\n"
          "Bagels       No digit is correct.\n"
          "For example, if the secret number was 248 and your guess was 843,\n"
          "the clues would be Fermi Pico.")

    max_digit = int(input("How much digits in numbers you want: "))
    number = rn.randint(10 ** (max_digit - 1), 10 ** max_digit - 1)
    max_guesses = int(input("How much guesses you want to have: "))
    print(number)
    print("I've thought up a number.")
    guess_count = 0

    while guess_count < max_guesses:
        guess_number = int(input("Guess " + str(guess_count + 1)+"\n"))
        if guess_number == number:
            print("You got it!")
            break
        else:
            print(check(guess_number, number))
            guess_count += 1


def check(guess_number, number):
    recovery = ""
    guess_number = str(guess_number)
    number = str(number)
    for j in range(len(number)):
        if guess_number[j] in number:
            if guess_number[j] == number[j]:
                recovery += "Fermi "
            else:
                recovery += "Pico "
    if recovery == "":
        recovery += "Bagles"
    return recovery


while True:
    if input("Do you want to play Bagels y/n: ").lower() == "y":
        in_game()
    else:
        print("(╯°□°）╯︵ ┻━┻")
