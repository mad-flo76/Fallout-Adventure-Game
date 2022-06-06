import random
import time


def print_pause(message):
    print(message)
    time.sleep(2)


def displayintro():
    print_pause("Greetings fellow vault dweller!")
    print_pause("You've been awaken from the cryolab alarm system")
    print_pause("you exit your cryogentic cell")
    print_pause("one path leads home to your neighborhood")
    print_pause("and the other path leads to a cave of people talking")


def choosepath():
    while True:
        response = input("do you want your path chosen for you?(yes or no):")

        if response == 'yes':
            checkpath()
            break
        elif response == 'no':
            playagain()
            break
        else:
            print_pause("invalid response")


def checkpath():
    print_pause("you head down the path")
    print_pause("you are greeted by your family members")
    print_pause("they tell you to keep calm and they explain.")
    print_pause("soon you find out your city has been nuked..")
    print_pause("now it's up to you to discover")
    print_pause("and walk around the wasteland that was once a town..")

    while True:
        response = input("to start the adventure,please type enter")
        if response == "enter":
            path = random.choice(["one", "two"])
            if path == "one":
                pathone()
                break
            elif path == "two":
                pathtwo()
                break
        else:
            print_pause("invalid response,please try again")


def pathone():
    print_pause("You have been given a Fat-Boy stored in your Pip-Boy 3000")
    print_pause("And you are about to drink a Nuka-Cola")

    while True:
        response = input("Do you want to fast travel? (Yes or No")
        if response == "yes":
            fight()
            break
        elif response == "no":
            playagain()
            break
        else:
            print_pause("invalid response. please try again")


def pathtwo():
    print_pause("You are greeted by a bot,name Codsworth")
    print_pause("He tells you about what happended to the nucular fallout")
    print_pause("He then ask to follow him to help random strangers")
    print_pause("do you wish to follow him?")
    while True:
        response = input("please enter yes or no")
        if response == 'yes':
            fight()
            break
        elif response == 'no':
            playagain()
            break
        else:
            print_pause("invalid answer,please try again")


def fight():
    print_pause("You are attacked by group of people!")

    while True:

        response = input("fight or surrender? (1 fight,2  surrender)")

        if response == "1":
            knife()
            break
        elif response == "2":
            leave()
            break
        else:
            print_pause("Invalid response. Please try again.")


def knife():
    print_pause("you enter towards the cave")
    print_pause("you find a kitchen knife on the floor")
    print_pause("you picked up the knife,and use it for self defense.")

    while True:
        response = input("do you want to pick up kitchen knife on the floor?")
        if response == 'yes':
            feralghoul()
            break
        elif response == 'no':
            leave()
            break
        else:
            print_pause("invalid response try again")


def feralghoul():
    print_pause("you take out your rifle,and enter towards the cave.")
    print_pause("you see a bunch radroaches around")
    print_pause("a feral ghoul comes by about to eat your flesh.")

    while True:
        valid = input("would you like to fight or surrender?")

        if valid == 'surrender':
            leave()
            break
        elif valid == 'fight':
            print_pause("you are bitten,your health is damaged")
            print_pause("you also get radiation poising")
            playagain()
            break


def leave():
    print_pause("you enter towards the cave")
    print_pause("you find a kitchen knife on the floor")

    while True:
        valid = input("Do yesyou shoot the feral ghoul yes or no")
        if valid == 'yes':
            print_pause("It's a critical hit!")
            playagain()
            break
        elif valid == 'no':
            print_pause("you died")
            exit(0)


def playagain():
    while True:
        valid = input("continue?(yes or no to continue playing:)")
        if valid == 'yes':
            playgame()
            break
        elif valid == 'no':
            print_pause("Game Over")
            exit(0)

        else:
            print_pause("invalid respsonse")


def playgame():
    displayintro()
    choosepath()
    checkpath()
    playagain()
    feralghoul()
    leave()
    fight()
    pathone()
    pathtwo()


playgame()
