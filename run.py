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


def enemy_action():
    """
    randomly selects enemy attack as object method
    """

    global _ENEMY_STATS

    if _ENEMY_STATS.hp > 0:

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
        print("You defeated the enemy!")


def player_action():
    """
    allows for user input during combat, calls object methods
    """

    if STATS.hp > 0:

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
            combi_table()
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
        print("You were felled by the enemy!")
        print("GAME OVER")


def combat():
    """
    decides who takes the turn first based on the speed object
    """
    while _ENEMY_STATS.hp > 0 and STATS.hp > 0:
        if _ENEMY_STATS.spd < STATS.spd:
            print("player goes first")
            player_action()
        else:
            print("enemy goes first")
            enemy_action()


def enemy_approaches():
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global _ENEMY_STATS

    ENEMY = random.randint(1, 3)

    if ENEMY == 1:
        _ENEMY_STATS = EnemyType("Goblin", 300, 100, 50, 5, 3)
        print(_ENEMY_STATS.full_stats())
        combat()
    elif ENEMY == 2:
        _ENEMY_STATS = EnemyType("Witch", 100, 300, 50, 1, 3)
        print(_ENEMY_STATS.full_stats())
        combat()
    elif ENEMY == 3:
        _ENEMY_STATS = EnemyType("Striga", 200, 200, 50, 3, 3)
        print(_ENEMY_STATS.full_stats())
        combat()


def boss_approaches(boss):
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global _ENEMY_STATS

    if boss == 1:
        _ENEMY_STATS = EnemyType("Dragon", 300, 100, 50, 5, 3)
        print(_ENEMY_STATS.full_stats())
        combat()
    elif boss == 2:
        _ENEMY_STATS = EnemyType("Titan", 100, 300, 50, 1, 3)
        print(_ENEMY_STATS.full_stats())
        combat()
    elif boss == 3:
        _ENEMY_STATS = EnemyType("Demon", 200, 200, 50, 3, 3)
        print(_ENEMY_STATS.full_stats())
        combat()


def enemy_encounter():
    """
    randomly generates 1 or 2 as an integer; determines enemy encounter
    """

    ENCOUNTER = random.randint(2, 2)

    if ENCOUNTER == 2:
        print("you encountered an ememy")
        print(ENCOUNTER)
        enemy_approaches()
    else:
        print("no enemy encounter")
        print(ENCOUNTER)


def story_arc_4():
    """
    story arc 4
    """
    clear_console()
    print("story arc 4")


def story_arc_3():
    """
    story arc 3
    """
    clear_console()
    print("story arc 3")


def story_arc_2():
    """
    story arc 2
    """
    clear_console()
    boss_approaches(1)
    # enemy_encounter()
    print("story arc 2")


def story_arc_1():
    """
    story arc 1
    """
    clear_console()
    enemy_encounter()
    print("story arc 1")


def story_arc_0():
    """
    inital story setup; currently a test function
    """

    clear_console()

    print("\n\n" + STATS.name + ", you wake up next to a dying fire.")
    print("It's cold, wet and dark. You look around and can't see anything...")
    print("...or for that matter...remember anything...except...")
    print(STATS.full_stats())
    time.sleep(1)
    print("Your mind is as clouded as the dense fog that is surrounding you.")
    print("You hear the noises of the night, muffled by the thick fog.")
    print("You stand up, look around and decide the following: ")
    print("""
    1. Follow the dirt path into the thick fog.
    2. Go through the tall grass and investigate the shiny object.
    3. Go down the steps to your right.
    4. Throw a stone at whatever is making that noise.
    """)

    path = input("Please input '1' or '2' to decide: ")

    if path == "1":
        story_arc_1()
    elif path == "2":
        story_arc_2()
    elif path == "3":
        story_arc_3()
    elif path == "4":
        story_arc_4()
    else:
        print("Please make a valid choice.")


def player_job_selection():
    """
    player choice of class and name input
    """
    global STATS

    print("What class would you like to be?")
    player_choice = input("(warrior / assassin / mage) ")

    if player_choice == "warrior":
        pname = input("What is your name, warrior? ")
        pjob = "Warrior"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 300, 100, 100, 5, 3)
        story_arc_0()
        # print(STATS.full_stats())

    elif player_choice == "assassin":
        pname = input("What is your name, assassin? ")
        pjob = "Assassin"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 200, 200, 100, 1, 5)
        story_arc_0()
        # print(STATS.full_stats())

    elif player_choice == "mage":
        pname = input("What is your name, mage? ")
        pjob = "Mage"
        STATS = player_job(pname, 1, 0, 0, pjob, "None", 100, 300, 100, 1, 1)
        story_arc_0()
        # print(STATS.full_stats())

    else:
        print("Please make a valid choice: \n")
        player_job_selection()


while True:

    player_job_selection()

# player_job_selection()
