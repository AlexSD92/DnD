import random
import time
import os
# https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
# https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
# https://pypi.org/project/prettytable/
from prettytable import PrettyTable


class EnemyType():
    """
    template for enemy types, object methods for attack
    """
    def __init__(self, job, hp, mp, atk, blk, spd):
        self.job = job
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.blk = blk
        self.spd = spd

    def full_stats(self):
        """
        prints full enemy stats
        """
        table = PrettyTable(["Attribute", "Value"])

        table.add_row(["JOB", self.job])
        table.add_row(['HEALTH', self.hp])
        table.add_row(['MAGIC', self.mp])
        table.add_row(['ATTACK', self.atk])
        table.add_row(['BLOCK', self.blk])
        table.add_row(['SPEED', self.spd])

        table.align["Attribute"] = "l"
        table.align["Value"] = "r"

        print(table)

    def attack(self):
        """
        calculation for physical attack
        """
        STATS.hp -= self.atk - STATS.blk


class player_job():
    """
    template for player types, object methods for attack
    """
    def __init__(self, name, lvl, exp, mny, job, itm, hp, mp, atk, blk, spd):
        self.name = name
        self.job = job
        self.lvl = lvl
        self.exp = exp
        self.mny = mny
        self.itm = itm
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.blk = blk
        self.spd = spd

    def full_stats(self):
        """
        prints full player stats
        """
        table = PrettyTable(["Attribute", "Value"])

        table.add_row(["NAME", self.name])
        table.add_row(["JOB", self.job])
        table.add_row(['Level', self.lvl])
        table.add_row(['Exp', self.exp])
        table.add_row(['Money', self.mny])
        table.add_row(['WEAPON', self.itm])
        table.add_row(['HEALTH', self.hp])
        table.add_row(['MAGIC', self.mp])
        table.add_row(['ATTACK', self.atk])
        table.add_row(['BLOCK', self.blk])
        table.add_row(['SPEED', self.spd])

        table.align["Attribute"] = "l"
        table.align["Value"] = "r"

        print(table)

    def attack(self):
        """
        calculation for physical attack
        """
        _ENEMY_STATS.hp -= self.atk - _ENEMY_STATS.blk

    def heal(self):
        """
        calculation and condition for healing
        """
        if self.mp > 0:
            self.mp -= 50
            self.hp += 50

    def sword(self):
        """
        what happens when user selects sword
        """
        STATS.atk += 5

    def dagger(self):
        """
        what happens when user selects dagger
        """
        STATS.atk += 1
        STATS.spd += 1


def combi_table():
    """
    combined table for combat so player can compare user stats and enemy stats
    """

    c_s = PrettyTable(["Attribute", "Player Value", "  ", "Enemy Value"])

    c_s.add_row(["NAME", STATS.name, "     ", " "])
    c_s.add_row(["JOB", STATS.job, "     ", _ENEMY_STATS.job])
    c_s.add_row(['WEAPON', STATS.itm, "     ", " "])
    c_s.add_row(['HEALTH', STATS.hp, "     ", _ENEMY_STATS.hp])
    c_s.add_row(['MAGIC', STATS.mp, "     ", _ENEMY_STATS.mp])
    c_s.add_row(['ATTACK', STATS.atk, "     ", _ENEMY_STATS.atk])
    c_s.add_row(['BLOCK', STATS.blk, "     ", _ENEMY_STATS.blk])
    c_s.add_row(['SPEED', STATS.spd, "     ", _ENEMY_STATS.spd])

    c_s.align["Player Attr"] = "l"
    c_s.align["Player Value"] = "r"

    print(c_s)


def clear_console():
    """
    clears the console when called
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def store_front():
    """
    store / shop
    """
    clear_console()
    print("Hello, " + STATS.name + " how can we be of service?")

    merch = PrettyTable(["Item", "Description", "Cost"])

    merch.add_row(['Sword', 'A fine blade', '$75'])
    merch.add_row(['Potion', 'Heals you good', '$25'])
    merch.add_row(['Ether', 'Gives you magic', '$35'])


def scavenge():
    """
    1/4 chance of finding coin
    """

    clear_console()

    chance = random.randint(0, 1)

    if chance == 0:

        coin = random.randint(0, 10)

        if coin == 0:
            print("\nYou found nothing.")

        elif coin == 1:
            print("\nYou found 1 coin!")
            STATS.mny += coin

        else:
            print("\nYou found " + str(coin) + " coins!")
            STATS.mny += coin

    else:
        print("\nYou found nothing!")


def enemy_action():
    """
    randomly selects enemy attack as object method
    """

    clear_console()

    global _ENEMY_STATS

    if _ENEMY_STATS.hp > 0:

        combi_table()

        enemy_choice = random.randint(1, 2)

        if enemy_choice == 1:
            print("The enemy performed a physical attack!")
            _ENEMY_STATS.attack()
            player_action()
        elif enemy_choice == 2:
            print("The enemy performed a magical attack!")
            # _ENEMY_STATS.magic_attack()
            player_action()

    else:
        print("\nYou defeated the enemy!")


def player_action():
    """
    allows for user input during combat, calls object methods
    """

    clear_console()

    if STATS.hp > 0:

        combi_table()

        print(
            """
            1 - Physical Attack
            2 - Magical Attack
            3 - Heal
            4 - Boon
            """
        )

        player_choice = input("What will you do?")

        if player_choice == "1":
            print("You performed a physical attack!")
            STATS.attack()
            enemy_action()
        elif player_choice == "2":
            print("You performed a magical attack!")
            enemy_action()
        elif player_choice == "3":
            print("You healed 50 HP!")
            STATS.heal()
            enemy_action()
        elif player_choice == "4":
            print("You unleashed your inner strength!")
            enemy_action()
        elif player_choice == "5":
            print(STATS.full_stats())

    else:
        print("\nYou were felled by the enemy!")
        print("\nGAME OVER")


def combat():
    """
    decides who takes the turn first based on the speed object
    """

    clear_console()
    
    while _ENEMY_STATS.hp > 0 and STATS.hp > 0:
        if _ENEMY_STATS.spd < STATS.spd:
            print("You reflexively attack first!")
            time.sleep(2)
            player_action()
        else:
            print("The enemy attacks first!")
            time.sleep(2)
            enemy_action()


def enemy_approaches():
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global _ENEMY_STATS

    ENEMY = random.randint(1, 3)

    if ENEMY == 1:
        _ENEMY_STATS = EnemyType("Goblin", 300, 100, 50, 5, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()
    elif ENEMY == 2:
        _ENEMY_STATS = EnemyType("Witch", 100, 300, 50, 1, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()
    elif ENEMY == 3:
        _ENEMY_STATS = EnemyType("Striga", 200, 200, 50, 3, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()


def boss_approaches(boss):
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global _ENEMY_STATS

    if boss == 1:
        _ENEMY_STATS = EnemyType("Dragon", 300, 100, 50, 5, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()
    elif boss == 2:
        _ENEMY_STATS = EnemyType("Titan", 100, 300, 50, 1, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()
    elif boss == 3:
        _ENEMY_STATS = EnemyType("Demon", 200, 200, 50, 3, 3)
        print("You encountered a " + _ENEMY_STATS.job)
        combat()


def enemy_encounter():
    """
    randomly generates 1 or 2 as an integer; determines enemy encounter
    """

    ENCOUNTER = random.randint(2, 2)

    if ENCOUNTER == 2:
        enemy_approaches()


def story_arc_1v3():
    """
    story arc 1v3
    """
    print("you have arrived at 1v3")


def story_arc_1v2():
    """
    story arc 1v2
    """
    print("you have arrived at 1v2")


def story_arc_1v1():
    """
    story arc 1v1
    """

    clear_console()
    print("""
          You continue down the dirt path.
          After a few minutes in to your journey,
          you come across an entrance to a cave.

          You decide to:

          1. Enter the cave.
          2. Continue on the path.
          3. Hunt for enemies.
          4. Shop

    """)

    path = input("What would you like to do? ")

    while True:

        if path == "1":
            story_arc_1v2()
            break
        elif path == "2":
            story_arc_1v3()
            break
        elif path == "3":
            enemy_approaches()
        elif path == "4":
            store_front()
        else:
            print("Please make a valid choice.")


def story_arc_1():
    """
    story arc 1
    """
    clear_console()
    enemy_encounter()
    print("- - - STORY ARC 1 - - -")
    print("""
          You begin to progress on the dirt path.
          Though you're wearing boots, you can feel the unnaturally cold earth.
          You can't help but feel that through the thick fog...something...
          ...or someone...is watching you.

          You trip on something in the dark and you can feel your heart skip.
          You look to see what it was and you find human remains.
          You pick through the remains and decide to take one of the following:

          1. Sword
          2. Axe
          3. Spear
          """)


def story_arc_0():
    """
    inital story setup; currently a test function
    """
    clear_console()

    print("Your mind is as clouded as the dense fog that surrounds you.")
    print("You hear the noises of the night, muffled by the thick fog.")
    print("You stand up, look around and decide the following: ")

    while True:

        print("""
        1. Follow the dirt path into the thick fog.
        2. Hunt for enemies.
        3. Scavenge.
        4. View your stats.
        """)

        path = input("(1 / 2 / 3 / 4) ")

        if path == "1":
            story_arc_1()
            break
        elif path == "2":
            enemy_approaches()
            print("\nWhat would you like to do? ")
        elif path == "3":
            scavenge()
            print("\nWhat would you like to do? ")
        elif path == "4":
            clear_console()
            STATS.full_stats()
            print("\nWhat would you like to do? ")
        else:
            clear_console()
            print("\nPlease make a valid choice.")


def confirm_choice():
    """
    checks if player is happy with thir choice
    """
    clear_console()

    print(STATS.name + ", you wake up next to a dying fire.")
    time.sleep(1)
    print("It's cold and dark. You look around and can't see anything...")
    time.sleep(1)
    print("...or for that matter...remember anything...except...\n")
    time.sleep(1)

    while True:

        STATS.full_stats()
        confirm = input("\nIs this how your story begins? (Yes / No) ").lower()

        if confirm == "yes":
            story_arc_0()
            break
        elif confirm == "no":
            player_job_selection()
            break
        else:
            clear_console()
            print("Please make a valid choice.")


def player_job_selection():
    """
    player choice of class and name input
    """

    clear_console()

    global STATS

    print("What class would you like to be?")
    player_choice = input("(warrior / assassin / mage) ").lower()

    if player_choice == "warrior":
        pname = input("\nWhat is your name, warrior? ")
        pjob = "Warrior"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 300, 100, 100, 5, 3)
        confirm_choice()

    elif player_choice == "assassin":
        pname = input("What is your name, assassin? ")
        pjob = "Assassin"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 200, 200, 100, 1, 5)
        confirm_choice()

    elif player_choice == "mage":
        pname = input("What is your name, mage? ")
        pjob = "Mage"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 100, 300, 100, 1, 1)
        confirm_choice()

    else:
        print("Please make a valid choice: \n")
        player_job_selection()


while True:

    player_job_selection()

# player_job_selection()
