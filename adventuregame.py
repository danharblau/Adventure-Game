import time
import random


def print_pause(message_to_print, ):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a locked")
    print(random.choice(["hotel room", "basement", "garage", "surgical room"]))
    print_pause("You don't remember a thing, and have trouble "
                "with short term memory")
    print_pause("You look around to search for any clues, and "
                "the only things you notice are:")
    print_pause("A locked door, with no keys around")
    print_pause("A safe with a 3 digit passcode")
    print_pause("A fire alarm")
    print_pause("You have to escape, but first "
                "you have to figure out how.")                                


def pull_alarm(items):
    print_pause("You pull the fire alarm.")
    print_pause("After a few moments, a secret door "
                "opens and reveals a huge mural of the letter pi")
    if "mural" in items:
        print_pause("You had already opened the secret door "
                    "revealing the mural, there's nothing"
                    "more to investigate.")
    else:
        print_pause("You make sure to remember the letter pie because "
                    "you're sure it's a clue.")
        items.append("mural")
    print_pause("You continue to try to escape.")
    decision_making(items)


def open_safe(items):
    print_pause("You head to the safe to see if you have "
                "any information to open it.")
    if "password" in items:
        print_pause("You remember you'd already opened it and found the keys")
        print_pause("There doesn't seem to be much to do here.")
    else:
        if "mural" in items:
            print_pause("You remember the mural and notice that the password "
                        "for the safe is three digits long, so you try 314")
            print_pause("IT OPENS! Inside there's a keychain, "
                        "presumably with the keys to open the door!")
            items.append("password")
        else:
            print_pause("You approach the safe, and try a few combinations, "
                        "but none work, so you go back to finding clues.")
    print_pause("You continue to plan your escape.")
    decision_making(items)


def open_door(items):
    print_pause("You walk towards the door with the hopes of opening it.")
    print_pause("Open this, and you're free!")
    if "mural" in items:
        print_pause("You remember the mural, but "
                    "you need more to open the door.")
        if "password" in items:
            print_pause("Fortunately, you had found the keychain!")
            print_pause("Congratulatons! After a few "
                        "tries to manage to open the door!"
                        "You have successfully freed yourself!!!")
        else:
            print_pause("You're better than this, you need more clues!"
                        "Try to open the safe to find more hints.")
            decision_making(items)
    else:
        print_pause("Unfortunately, the door is locked "
                    "and you can't get out.")
        print_pause("It looks like you need some kind of "
                    "keys to open the door.")
        print_pause("You continue to plan your escape.")
        decision_making(items)


def decision_making(items):
    while True:
        print_pause("What's your next move? (Choose a number)")
        decision = input("1. Pull the fire alarm\n"
                         "2. Try to open the safe\n"
                         "3. Try to open the door\n")
        if decision == '1':
            pull_alarm(items)
            break
        elif decision == '2':
            open_safe(items)
            break
        elif decision == '3':
            open_door(items)
            break
        else:
            print_pause("Sorry! I don't understand. Please try again!")
    return decision


def play_again():
    while True:
        repeat = input("Would you like to play again? (Write 'yes' or 'no')")
        if repeat == 'yes':
            items = []
            intro()
            decision_making(items)
            break
        elif repeat == 'no':
            print_pause("Thank you for playing, hope to see you soon!")
            break
        else:
            print_pause("Sorry! I don't understand. Please try again!")
    return repeat


def play_game():
    items = []
    intro()
    decision_making(items)
    play_again()


play_game()
