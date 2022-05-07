import random as rn

cube6 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█ o   o   o █  █ ",
         "█           █ █  ",
         "█ o   o   o ██   ",
         "█████████████    "
         ]
cube5 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█ o       o █  █ ",
         "█     o     █ █  ",
         "█ o       o ██   ",
         "█████████████    "
         ]
cube4 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█ o       o █  █ ",
         "█           █ █  ",
         "█ o       o ██   ",
         "█████████████    "
         ]
cube3 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█ o         █  █ ",
         "█     o     █ █  ",
         "█         o ██   ",
         "█████████████    "
         ]
cube2 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█ o         █  █ ",
         "█           █ █  ",
         "█         o ██   ",
         "█████████████    "
         ]
cube1 = ["    █████████████",
         "   █           ██",
         "  █           █ █",
         " █           █  █",
         "█████████████   █",
         "█           █  █ ",
         "█     o     █ █  ",
         "█           ██   ",
         "█████████████    "
         ]

CUBES = [cube1, cube2, cube3, cube4, cube5, cube6]


def check(gen_cubes):
    if (gen_cubes[0] + gen_cubes[1]) % 2 == 0:
        return "CHO"
    elif (gen_cubes[0] + gen_cubes[1]) % 2 == 1:
        return "HAN"


def cubes_generator():
    CUBES = [rn.randint(1, 6), rn.randint(1, 6)]
    return CUBES


def win(BET, BALANCE):
    BET = BET * 2
    BALANCE += BET
    FEE = BET * 0.05
    print("The house took fee: ", FEE)
    BALANCE -= FEE
    return BALANCE


def lose(BALANCE, BET):
    BALANCE -= BET
    return BALANCE


def main():
    BALANCE = 5000
    while True:
        if BALANCE <= 0:
            print("You've lost all your money!")
            break
        print("You have ", BALANCE, " on your balance. \n"
                                    "Please, enter your bet.(or QUIT)")
        BET = input()
        if BET == "QUIT":
            break
        else:
            try:
                BET = int(BET)
                if BET <= 0 or BET > BALANCE:
                    print("WRONG BET!!!!")
                    continue
            except:
                print("(╯°□°）╯︵ ┻━┻ Unknown command! (╯°□°）╯︵ ┻━┻")
                break
        print("Throwing CUBES")
        gen_cubes = cubes_generator()
        reqest = input("Choose CHO(even) or HAN(odd): ").upper()
        for i in range(len(cube1)):
            print(CUBES[gen_cubes[0]-1][i], " ", CUBES[gen_cubes[1]-1][i])
        if check(gen_cubes) == reqest:
            print("You won!!!")
            BALANCE = win(BET, BALANCE)
        else:
            print("You lose :(")
            BALANCE = lose(BALANCE, BET)



if __name__ == '__main__':
    main()
