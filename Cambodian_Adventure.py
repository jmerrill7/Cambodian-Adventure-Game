# CAMBODIAN ADVENTURE TEXT GAME
# Author: James Merrill
# Date: 2/24/2017
''' A text-based game that takes the user on an adventure in which he/she is faced with difficult choices.
***SPOILER*** There are three ways to lose, two of those ways involve death, though it as also possible to lose and survive
One "win" condition contains a bonus for exceptional decision making.''' 

import time

def start(good=0,bad=0,name=""):
    name = describe_game(name)
    good,bad,name = first_event(good,bad,name)

def describe_game(name):
    if name != "":
        print("\nThanks for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("What is your name? ").capitalize()
                if name != "":
                    print("Hey, {}! Welcome to Cambodia. You arrived at Angkor Wat this morning, and decided it was too touristy. Instead of following the tour group to Angkor Thom, you set off alone into the jungle seeking adventure!".format(name))
                    raw_input("Press Enter to continue...")
                    stop = False
    return name

def first_event(good,bad,name):
    stop = True
    while stop:
        pick = raw_input("You come across some odd-smelling native foliage and realize that you haven't eaten since breakfast. Do you: Eat the native foliage? (eat) OR Keep walking and ignore your grumbling stomach (ignore)?").lower()
        if pick == "ignore":
            print("You carry on, satisfied with your choice. Sampling the native foliage might prove to be unwise.")
            raw_input("Press Enter to continue...")
            good = (good + 1)
            stop = False
        if pick == "eat":
            print("You eat the native foliage, it does little to help your appetite and you have a stomachache now too.")
            raw_input("Press Enter to continue...")
            bad = (bad + 1)
            stop = False
    score(good,bad,name)
    second_event(good,bad,name)

def second_event(good,bad,name):
    stop = True
    while stop:
        time.sleep(2)
        print("After several hours of hiking, it begins to rain, lightly at first.")
        time.sleep(3)
        print("Before long, you are in a downpour. You run for cover under a rocky outcropping.")
        raw_input("Press Enter to continue...")
        print("Scurrying into the shelter has revealed that it is more than just a mere outcropping. You have found a mysterious cave!")
        raw_input("Press Enter to continue...")
        pick = raw_input("Do you: Run blindly into the mysterious cave? (fast) OR Enter the mysterious cave slowly and cautiously? (slow)").lower()
        if pick == "slow":
            print("Entering the cave cautiously reveals an exposed tree root near the entrance, You gingerly step over it.")
            raw_input("Press Enter to continue...")
            good = (good + 1)
            stop = False
        if pick == "fast":
            print("Sprinting full speed into the cave, you fail to notice an exposed tree root near the entrance. You trip on the tree root and bruise both knees badly!")
            raw_input("Press Enter to continue...")
            bad = (bad + 1)
            stop = False
    score(good,bad,name)
    third_event(good,bad,name)

def third_event(good,bad,name):
    stop = True
    while stop:
        print("Once inside, you decide to explore. Cracks in the ceiling shed a dim light on the passage. You proceed into the dark...")
        raw_input("Press Enter to continue...")
        print("After a few minutes, you come to a deep chasm. It looks like you could make the jump, but you aren't completely sure. Upon further investigation, you see that a strong vine also hangs from above the chasm.")
        raw_input("Press Enter to continue...")
        pick = raw_input("Do You: Jump! (jump) OR Grab the vine and gracefully swing across the chasm? (swing)").lower()
        if pick == "swing":
            print("....You land on the other side of the chasm, unharmed, and proceed further into the dimly lit and mysterious cave.")
            raw_input("Press Enter to continue...")
            good = (good + 1)
            stop = False
        if pick == "jump":
            time.sleep(4)
            print("....Ouch, that was further than it looked. You tumble down into the darkness!")
            time.sleep(4)
            lose(good,bad,name)
            stop = False
    score(good,bad,name)
    fourth_event(good,bad,name)

def fourth_event(good,bad,name):
    stop = True
    while stop:
        print("The cave narrows out after a few minutes, and you are forced to crawl for a time...")
        time.sleep(5)
        print("You see a bright golden light ahead, and squeeze through the opening...")
        raw_input("Press Enter to continue...")
        print("The cavern you find yourself in is breathtaking!! The walls are intricately carved in ancient Khmer fashion, and at the center of the room a jewel-ecrusted scimitar rests on a raised marble platform!")
        raw_input("Press Enter to continue...")
        pick = raw_input("Do You: Look for a way out of the cavern? (plan) OR Grab the jewel-encrusted scimitar by the hilt and proclaim ownership! (take)").lower()
        if pick == "plan":
            print("You may indeed be able to claim the artifact for yourself, but wisely elect to plot an exit strategy before grabbing the artifact.")
            raw_input("Press Enter to continue...")
            print("Your invesigation reveals a hidden door, leading to an adjacent tunnel.")
            raw_input("Press Enter to continue...")
            print("You snatch up the artifact and rush to the hidden door as a trap fills the main chamber with noxious green gas. You make it to the adjacent tunnel in time to avoid the fumes.")
            raw_input("Press Enter to continue...")
            good = (good + 1)
            stop = False
        if pick == "take":
            print("Hastily grabbing the artifact triggers a trap! The room begins to fill with a noxious green gas, and the heavy sword burdens you as you scramble for a way out. You find that there is none.")
            raw_input("Press Enter to continue...")
            lose(good,bad,name)
            stop = False
    score(good,bad,name)
    fifth_event(good,bad,name)

def fifth_event(good,bad,name):
    stop = True
    while stop:
        print("The hidden tunnel you found prior to grabbing the precious artifact leads back into the jungle. You emerge to find that the rain has stopped")
        raw_input("Press Enter to continue...")
        print("Though still lost, you are now in posession of a priceless artifact. You hear distant voices and elect to wait for rescue.")
        pick = raw_input("Type (wait) to wait for rescue.").lower()
        if pick == "wait":
            print("You hide the artifact and patiently wait for rescue...")
            time.sleep(5)
            good = (good + 1)
            if good == 5:
                bonus(good,bad,name)
                stop = False
            else:
                win(good,bad,name)
                stop = False
    score(good,bad,name)

      
def score(good,bad,name):
    if bad == 2:
        lose2(good,bad,name)
    if good == 5:
        bonus(good,bad,name)

def lose2(good,bad,name):
    print("\n{}, Your stomachache and bruised knees make it too difficult to go on. Your adventure sadly ends before it even begins.".format(name)) #DEFINE A FUNCTION THAT RETURNS A STRING VARIABLE, PRINT THE RESULT TO THE SHELL
    again(good,bad,name)

def win(good,bad,name):
    print("\n{}, You are eventually rescued and keep your secret adventure to yourself. Once home, the local museum buys your prized Khmer jewel-encrusted sword for $1,000,000 cash! You live happily ever after.".format(name))
    again(good,bad,name)
          
def lose(good,bad,name):
    print("\n{}, Your bad choices have led to an untimely death.\nThe local authorities may never recover your body..".format(name))
    again(good,bad,name)

def bonus(good,bad,name):
    print("\n{}, You are eventually rescued and keep your secret adventure to yourself. Once home, the local museum buys your prized Khmer jewel-encrusted sword for $1,000,000 cash! You live happily ever after. As a bonus for world-renowned adventuring and rational decision making, you get to meet the president! The End.".format(name))
    again(good,bad,name)
             
def again(good,bad,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(good,bad,name)
        if choice == "n":
            print("Goodbye, {}!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'... ")

def reset(good,bad,name):
    good = 0
    bad = 0
    start(good,bad,name)


if __name__ == "__main__":
    start()
