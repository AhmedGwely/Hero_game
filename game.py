import time
import random

Items =[]
fears =["Pirates ", "Thieves ", "Aliens "]
ev = random.choice(fears)

inp1 =str(input("Please enter your name ??\n"))
print("Hello master "+inp1 +"\n")
def opening():

    for side in["You find yourself standing in an open field, filled with grass and yellow wildflowers.",
                 "Rumor has it that a troll is somewhere around here, and has been terrifying the nearby village.",
                 "In front of you is a house.",
                 "To your right is a dark cave.",
                 "In your hand you hold your trusty (but not very effective) dagger."]:

                 time.sleep(2)
                 print(side)
def q1():

    print("\n")
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    inp2 =str(input("What would you like to do? \n (Please enter 1 or 2.)"))

            
    if inp2 == "1" or inp2 == "one":

        cho1()
    elif inp2 == "2" or inp2 == "two":
        cho2()
        
    else:
        q1()

    


def cho1():
    for side in["You approach the door of the house.",
                "You are about to knock when the door opens and out steps a troll.",
                "Eep! This is the "+ev+"'s house!",
                "The "+ev+" attacks you!",
                "You feel a bit under-prepared for this, what with only having a tiny dagger."]:
                time.sleep(2)
                print(side)
    
    time.sleep(2)
    def q2():

        inp3 =str(input("\n Would you like to (1) fight or (2) run away?"))
    
        if inp3 == "1" or inp3 == "one":

            for side in["You do your best...",
                        "but your dagger is no match for the troll.",
                        "You have been defeated!"]:
                        time.sleep(2)
                        print(side)
                        end()
        elif inp3 == "2" or inp3 == "two":
            time.sleep(2)
            print("You run back into the field. Luckily, you don't seem to have been followed.")
            time.sleep(2)
            q1()
        else:
            q2()
    q2()
     

            
def cho2():

    for side in["You peer cautiously into the cave.",
                "It turns out to be only a very small cave.",
                "Your eye catches a glint of metal behind a rock.",
                "You have found the magical Sword of Ogoroth!",
                "You discard your silly old dagger and take the sword with you.",
                "You walk back out to the field."]:
                time.sleep(2)
                print(side)
    q1()


def end():
    time.sleep(2)
    print("you die \n")
    inp4 =str(input("Would you like to play agan yes/no ??\n"))
    if inp4 == "yes":
        opening()
    elif inp4 == "no":
        exit()
    else:
        end()


def oprator():

    opening()
    q1()

oprator()
    
