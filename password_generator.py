import random


def password_generator():
    print("Welcome to Password Generator!")
    password_length = int(input("How long do you want your password?: "))

    ## List of characters
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SPECIAL_CHARACTERS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '^', '&', '$', '#', '"']
    CHARACTERS = UPPER + LOWER + NUMS + SPECIAL_CHARACTERS

    ## Creating a random password
    password = []
    for i in range(password_length):
        random_character = random.choice(CHARACTERS)
        password.append(random_character)
    
    ## Converting Password List into a String
    password = "".join(password)

    return password


def run():
    program_active = True

    while program_active:
        password = password_generator()
        print("----------------------------")
        print("----------------------------")
        print(password)
        print("----------------------------")
        print("----------------------------")
        user_option = int(input("Do you want to close the password generator? \n 0. Yes \n 1. No \n"))

        if user_option == 0:
            program_active = False
        else:
            program_active = True
        


if __name__ == '__main__':
    run()