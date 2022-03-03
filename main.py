import random
import itertools
import threading
import time
import sys

done = False
print(f"\n \nThis program utilizes python ANSI codes to display color, color might not be\nshown"
      f" when program is executed in terminal \n")

print(f"\033[1;32m********************************************************************\n"
      f"Do you have what it takes to beat the Mighty Toad?\n"
      f"You can be a caring Mage whose given extra health\n"
      f"Or a Knight..Stronger than the others,prideful in his Strength\n"
      f"Or...A thief..whose path is strictly luck!\n"
      f"By Deshawn Battle\n"
      f"********************************************************************\n\n")

PATH_LENGTH = 10

final_boss_help = {1: "More Health", 2: "More Strength", 3: "Give up"}


# Player attributes such as health, attack etc..

class Player:
    def __init__(self, name="John", warrior_type=1):
        self.name = name
        self.warrior_type = warrior_type
        self.gold = 0
        self.health = 350
        self.strength = 20
        self.position = 0

    def set_player_name(self):
        self.name = input("What is your name warrior: ")
        if self.name.strip() == '':
            self.name = 'John'

    def set_player_health(self, damage_done):
        self.health = self.health - damage_done

    def add_gold(self, amount_found):
        self.gold = self.gold + amount_found

    def add_position(self):
        self.position = self.position + 1

    def add_health(self, health):
        self.health = self.health + health

    def add_strength(self, power):
        self.health = self.strength + power

    def set_warrior_type(self):
        warrior_types = {1: "Mage", 2: "Knight", 3: "Thief"}

        try:
            self.warrior_type = int(input("What kind of warrior are you: 1 for Mage, 2 for Knight, 3 for Thief: "))
        except ValueError:
            print("Not a Valid entry ...nerd...NOW YOUR A MAGE\n\n")
            self.warrior_type = 1

        while self.warrior_type not in warrior_types:
            print("That wasn't a correct selection")
            self.warrior_type = int(input("What kind of warrior are you: 1 for Mage, 2 for Knight, 3 for Thief: "))

        if self.warrior_type == 1:
            print(f"\033[1;36mYou are a caring {warrior_types[self.warrior_type]}!")
            self.health = self.health + 200
            self.strength = self.strength - 5
        elif self.warrior_type == 2:
            print(f"\033[1;36mYou are a strong {warrior_types[self.warrior_type]}!")
            self.strength = self.strength + 15
        elif self.warrior_type == 3:
            print(f"\033[1;36mYou are a sneaky {warrior_types[self.warrior_type]}!")
            self.strength = random.randint(0, 100)
            self.health = random.randint(1, 400)

        return warrior_types[self.warrior_type]

    def get_name(self):
        return self.name

    def get_warrior_type(self):
        print(self.warrior_type)

    def get_gold(self):
        return self.gold

    def get_health(self):
        return self.health

    def get_position(self):
        return self.position

    def attack(self):
        return self.strength


# Toad attributes such as health, attack etc..
class Toad:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.name = "Baby Toad"
        self.gold = random.randint(5, 10)
        self.introduction = random.randint(1, 3)

    def get_introduction(self):
        if self.introduction == 1:
            print("\n\033[1;31mTOAD: HAHA you've licked your last Toad!\n\n")
        elif self.introduction == 2:
            print("\n\033[1;31mTOAD: You will Never Reach the Mighty Toad!\n\n")
        else:
            print("\n\033[1;31mTOAD: HAHAHAHAHA prepare to die!\n\n")

    def get_health(self):
        return self.health

    def set_health(self, attack):
        self.health = self.health - attack

    def attack_damage(self):
        return self.strength

    def get_name(self):
        return self.name

    def give_gold(self):
        return self.gold

    def print_death_cry(self):
        print("\033[1;31mToad: Uhhhh ahhhh... Master.... I let you down!!")


# Baby toad using parent attributes of Toad
class BabyToad(Toad):
    def __init__(self):
        super().__init__()
        self.introduction = "\033[1;31mBABY TOAD: *wimper* *wimper* I may be small but i hit hard\n"
        self.health = 20
        self.strength = 5
        self.gold = random.randint(1, 5)

        Toad.get_health(self)
        Toad.give_gold(self)
        Toad.get_name(self)
        Toad.attack_damage(self)

    def get_intro(self):
        print(self.introduction)

    def set_health(self, attack):
        self.health = self.health - attack

    def print_death_cry(self):
        print("\033[1;31m BabyToad: No..spare me im just a baby...\n")


# Final Boss
class MightyToad:
    def __init__(self):
        self.health = 325
        self.strength = 40
        self.name = "Baby Toad"
        self.gold = random.randint(50, 100)
        self.introduction = "\033[1;31mWell you managed to kill every one of my Killer Toads...BUT NOW it's TIME you " \
                            "DIE!!!!\nHAHAAHAHAHAHAHAHAHA\nHAHAAHAHAHAHAHAHAHA\n\n"

    def introduction(self):
        print(self.introduction)

    def set_health(self, attack):
        self.health = self.health - attack

    def get_health(self):
        return self.health

    def attack_damage(self):
        return self.strength

    def get_name(self):
        return self.name

    def get_gold(self):
        return self.gold

    def get_intro(self):
        print(self.introduction)


# Check if player dead to end or continue game
def is_player_alive(player):
    if player1.get_health() <= 0:
        print(f"\033[1;31m Noooooo {player1.get_name()} get up please!!! \n\n GAME OVER")
        print(f"\033[1;32m---STATS----\n Health: {player1.get_health()} Steps Made: {player.get_position()}"
              f" Gold: {player1.get_gold()} \n")
        return False

    else:
        print(f"\033[1;31m!{player.get_name()} You have {player.get_health()} "
              f"Health points left! be careful!\n")
    return True


# check if toad dead to resume adventure
def is_toad_dead(toad, player):
    toad_gold = toad.give_gold()
    if toad.get_health() <= 0:
        player.add_gold(toad_gold)
        toad.print_death_cry()
        print(f"\033[1;33m {player.get_name()}...You killed Him!\n It dropped {toad_gold} "
              f" Gold \n Total GOLD: "
              f"{player.get_gold()}\n")
        return True
    return False


# loading animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        global done
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


# check if Boss dead to end game
def is_mighty_toad_dead(mighty, player):
    if mighty_toad.get_health() <= 0:
        mighty_toad_gold = mighty.get_gold()
        player1.add_gold(mighty_toad_gold)
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(2)
        global done
        done = True

        print("\033[1;31m\nMighty Toad: Uh.. I can't believe i lost.. *cough* I will see you... *cough*  in hades..\n")
        print(f"\033[1;33m{player.get_name()}...You really DID IT!! After 500 years!!\nHe dropped {mighty_toad_gold} "
              f"Gold \nTotal GOLD: "
              f"{player1.get_gold()}\n")
        print(f"\033[1;32m---STATS----\nHealth: {player.get_health()} Steps Made: {player.get_position()} "
              f"Gold: {player1.get_gold()}\n")
        return True
    return False


# random encounter
def random_int():
    return random.randint(1, 3)


# random encounter from baby toad
def random_baby_toad(baby_toad, player):
    baby_toad.get_intro()
    player.set_player_health(baby_toad.attack_damage())
    attackdmg = baby_toad.attack_damage()
    print(f"CAREFUL {player.get_name()} THERE'S BABY TOADS THAT REACHOUT AND BITE YOU!\n")
    print(f"Damage done: {attackdmg} Current Health {player.get_health()}")
    print(f"---------------------------------------------------------------------\n")

# Creating player and assigning player name & type


player1 = Player()

player1.set_player_name()
player1.set_warrior_type()
# Player Intro
print(f"\033[1;32mWelcome! {player1.get_name()} we need your help slaying the MightyToad! "
      f"this adventure will be long and dangerous\n\n")

# Creating The Boss


mighty_toad = MightyToad()
# Like a die roll, if you land on 2  you fight Toad, 3 you get bitten
baby_bite = 3
toad_fight = 2

# Create Baby Toad
babyToad = BabyToad()

# Keep game in loop until Player is dead or Boss is Dead
while player1.get_position() <= PATH_LENGTH:
    # check if Player or Boss Dead if so End Game, DON'T DELETE LINE
    if player1.get_health() <= 0 or mighty_toad.get_health() <= 0:
        break

    input("\n\033[1;32mPress Enter/Return to move forward!\n")
    player1.add_position()
    random_int()
    # execute Baby Toad Bite
    if random_int() == baby_bite:
        random_baby_toad(babyToad, player1)
        is_player_alive(player1)
    # Progress tracker
    if player1.get_position() != 10:
        print(f"\033[1;32mYour {10 - player1.get_position()} away from the Mighty Toad!")
    # Execute Boss Fight
    if player1.get_position() == 10:
        mighty_toad.get_intro()
        if player1.get_health() <= 220:
            try:
                help_player = int(input(
                    f"\033[1;32m{player1.get_name()} I've been saving this special potion for when you fight the MIGHTY"
                    f"TOAD: ENTER 1 for +150 health, ENTER 2: +40 strength, ENTER 3: Give Up: "))
            except ValueError:
                help_player = 1
                print("Invalid..Enjoy THE HEALTH\n")

            if help_player not in final_boss_help:
                help_player = 1
                print("Invalid..Enjoy THE HEALTH\n")

            if help_player in final_boss_help:
                if help_player == 1:
                    player1.add_health(150)
                    print("EXTRA HEALTH GIVEN...GOOD-LUCK!!")
                elif help_player == 2:
                    player1.add_strength(40)
                    print("EXTRA STRENGTH GIVEN...GOOD-LUCK!!")
                elif help_player == 3:
                    print(f"\033[1;31m{player1.get_name()} You tried your best..sadly it wasn't enough!")
                    print(
                        f"\033[1;32m---STATS----\n Health: {player1.get_health()} Steps Made: {player1.get_position()} "
                        f" Gold: {player1.get_gold()}\n")
                    player1.set_player_health(0)
                    break

        while mighty_toad.get_health() > 0 and player1.get_health() > 0:
            if mighty_toad.get_health() < 200:
                print("\033[1;31m MIGHTY TOAD: *cough* *bleeding*....")
            if mighty_toad.get_health() < 100:
                print("\033[1:31m Mighty TOAD: Please....spare me...")

            input("\033[1;32mPress Enter/Return to Attack! \n")

            player_attack = random.randint(5, player1.attack())

            mighty_toad.set_health(player_attack)
            print(f"\033[1;32m-----You did {player_attack} damage!-----\n")
            player_attack = player1.attack()

            if is_mighty_toad_dead(mighty_toad, player1):
                break

            print(f"\033[1;31m---Mighty Toad Have {mighty_toad.get_health()} Health points left!---\n")
            mighty_toad_attack = random.randint(15, mighty_toad.strength)
            player1.set_player_health(mighty_toad_attack)

            print(f"\033[1;31m-----The Mighty Toad did {mighty_toad_attack} Damage!-----")
            toad_attack = random.randint(15, mighty_toad.strength)

            if not is_player_alive(player1):
                break
    # check if Player or Boss Dead if so End Game, DON'T DELETE LINE
    if player1.get_health() <= 0 or mighty_toad.get_health() <= 0:
        break
    # Execute random Toad fight
    if random_int() == toad_fight:
        toad = Toad()
        while toad.get_health() > 0:
            if toad.get_health() == 100:
                print("\033[1;31m----------------------------------------------\n")
                print("\033[1;31mYou have ran into a Killer Toad... Good-luck!!\n")
                toad.get_introduction()

            input("\033[1;32mPress Enter/Return to Attack! \n")

            player_attack = random.randint(5, player1.attack())
            toad.set_health(player_attack)

            print(f"\033[1;32m-----You did {player_attack} damage!-----\n")
            player_attack = player1.attack()

            if is_toad_dead(toad, player1):
                fight = random.randint(1, 3)
                break

            print(f"\033[1;31m---Toad Have {toad.get_health()} Health points left!---\n")
            toad_attack = random.randint(5, toad.strength)
            player1.set_player_health(toad_attack)

            print(f"\033[1;31m-----the Toad did {toad_attack} Damage!-----")
            toad_attack = random.randint(5, toad.strength)

            if not is_player_alive(player1):
                break
# Thanks for playing, editing or looking at this program
input("Press Enter to Close.. Thanks for Playing!")
