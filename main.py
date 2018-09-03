from random import randint
import time

print("===== What Are The Odds? =====")


def ask_int(upper_bound_given):
    print("Say a number between 1 and " + upper_bound_given)
    odds = input()
    try:
        result = int(odds)
        return result
    except ValueError:
        print("It must be an integer!")
        return ask_int(upper_bound_given)


def quit_or_play():
    print("Want to play again? (y/n)")
    end = input()
    if end[0] == 'y':
        print("Awesome, lets do it again!")
        return 1
    elif end[0] == 'n':
        print("It was fun playing. Bye!")
        time.sleep(2)
        quit()
    else:
        print("Sorry, I didn't understand.")
        quit_or_play()


while True:
    print("What are the odds, 1 to ...?")
    upper_bound = input()

    try:
        upper_bound_int = int(upper_bound)
    except ValueError:
        print("It must be an integer")
        continue

    print("Okay, what are the odds, 1 to " + upper_bound)
    print("Ready?")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    odds_int = ask_int(upper_bound)

    within_bounds = 1 <= odds_int <= upper_bound_int

    while not within_bounds:
        print("It must be between 1 and " + upper_bound)
        odds_int = ask_int(upper_bound)
        within_bounds = 1 <= odds_int <= upper_bound_int

    random_number = randint(1, upper_bound_int)

    print(str(random_number) + "!")

    if odds_int == random_number:
        print("We said the same number! You have to do it now.")
    elif odds_int + random_number == upper_bound_int:
        print("Our numbers added up to the upper bound! You have to do it now.")
    else:
        print("Whew, you got lucky!")

    if quit_or_play() == 1:
        continue

