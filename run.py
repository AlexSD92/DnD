import random
import time
import sys
import os
# https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
# https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
# https://pypi.org/project/prettytable/
from prettytable import PrettyTable
from colorama import Fore, Style

player_itm_inv = {"Potion": 0, "Ether": 0}


class FontStyle():
    """
    used to bold and underline text
    https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
    """
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class EnemyType():
    """
    template for enemy types, object methods for attack
    """
    def __init__(self, job, lvl, exp, h_p, mhp, m_p, mmp, atk, blk, spd):
        self.job = job
        self.lvl = lvl
        self.exp = exp
        self.h_p = h_p
        self.mhp = mhp
        self.m_p = m_p
        self.mmp = mmp
        self.atk = atk
        self.blk = blk
        self.spd = spd

    def full_stats(self):
        """
        prints full enemy stats
        """
        table = PrettyTable(["Attribute", "Value"])

        table.add_row(["JOB", round(self.job)])
        table.add_row(['LEVEL', round(self.lvl)])
        table.add_row(['EXP', round(self.exp)])
        table.add_row(['HEALTH', round(self.h_p)])
        table.add_row(['MAGIC', round(self.m_p)])
        table.add_row(['ATTACK', round(self.atk)])
        table.add_row(['BLOCK', round(self.blk)])
        table.add_row(['SPEED', round(self.spd)])

        table.align["Attribute"] = "l"
        table.align["Value"] = "r"

        print(table)

    def health_bar(self):
        """
        prints health bar
        https://stackoverflow.com/questions/48035367/python-text-game-health-bar
        """
        unit_convert = int(self.mhp/100)
        current_unit = int(self.h_p/unit_convert)
        remaining_health = 100 - current_unit

        remaining_hp = "¦" * current_unit
        empty_hp = " " * remaining_health
        # percent = str(int((self.h_p/self.mhp)*100)) + "%"

        print("\nEnemy HP:    {" + remaining_hp + empty_hp + "}")
        # print("     " + percent)

    def attack(self):
        """
        calculation for physical attack
        """
        STATS.h_p -= self.atk - STATS.blk
        if STATS.h_p <= 0:
            STATS.h_p = 0


class PlayerJob():
    """
    template for player types, object methods for attack
    """
    def __init__(self, name, lvl, exp, mny, job, itm,
                 h_p, mhp, m_p, mmp, atk, blk, spd):
        self.name = name
        self.job = job
        self.lvl = lvl
        self.exp = exp
        self.mny = mny
        self.itm = itm
        self.h_p = h_p
        self.mhp = mhp
        self.m_p = m_p
        self.mmp = mmp
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
        table.add_row(['LEVEL', self.lvl])
        table.add_row(['EXP', round(self.exp)])
        table.add_row(['MONEY', self.mny])
        table.add_row(['WEAPON', self.itm])
        table.add_row(['HEALTH', round(self.h_p)])
        table.add_row(['MAGIC', round(self.m_p)])
        table.add_row(['ATTACK', round(self.atk)])
        table.add_row(['BLOCK', round(self.blk)])
        table.add_row(['SPEED', round(self.spd)])

        table.align["Attribute"] = "l"
        table.align["Value"] = "r"

        print(table)

    def levelup(self):
        """
        calculation for the player to level up
        """

        self.exp += EST.exp
        experience_required = 500 * self.lvl
        current_experience = self.exp - experience_required
        mult = (self.lvl - (self.lvl * .975)) + 1

        if self.exp > experience_required:

            print("You leveled up!")

            self.lvl += 1
            self.exp = current_experience
            self.h_p = self.h_p * mult
            self.mhp = self.mhp * mult
            self.m_p = self.m_p * mult
            self.mmp = self.mmp * mult
            self.atk = self.atk * mult
            self.blk = self.blk * mult
            self.spd = self.spd * mult

    def health_bar(self):
        """
        prints health bar
        https://stackoverflow.com/questions/48035367/python-text-game-health-bar
        """
        unit_convert = int(self.mhp/25)
        current_unit = int(self.h_p/unit_convert)
        remaining_health = 25 - current_unit

        remaining_hp = "¦" * current_unit
        empty_hp = " " * remaining_health
        # percent = str(int((self.h_p/self.mhp)*100)) + "%"

        print("\nYour HP:     {" + remaining_hp + empty_hp + "}")
        # print("     " + percent)

    def magic_bar(self):
        """
        prints magic bar
        https://stackoverflow.com/questions/48035367/python-text-game-health-bar
        """
        unit_convert = int(self.mmp/25)
        current_unit = int(self.m_p/unit_convert)
        remaining_magic = 25 - current_unit

        remaining_mp = "¦" * current_unit
        empty_mp = " " * remaining_magic
        # percent = str(int((self.h_p/self.mhp)*100)) + "%"

        print("\nYour MP:     {" + remaining_mp + empty_mp + "}")
        # print("     " + percent)

    def attack(self):
        """
        calculation for physical attack
        """
        EST.h_p -= self.atk - EST.blk
        if EST.h_p <= 0:
            EST.h_p = 0

    def heal(self):
        """
        calculation and condition for healing
        """

        if self.m_p > 0:
            self.m_p -= 1
            self.h_p += 200

            if self.h_p > self.mhp:
                self.h_p = self.mhp


def shop():
    """
    function determining store, stock and cost
    """

    while True:

        inv = {
            "Ptn": 100,
            "Eth": 200
        }

        store = PrettyTable(["Item", "Price"])
        store.add_row(["Potion", inv.get("Ptn")])
        store.add_row(["Ether", inv.get("Eth")])

        clear_console()

        print("----STORE----\n")
        print(store)

        print("\nWelcome to the store, what would you like to buy? ")
        print("""
        1. Potion
        2. Ether
        0. Exit
        """)

        print("Your Wallet: " + str(STATS.mny) + "\n")

        choice = input("1 / 2:\n\n")

        if choice == "1":
            if STATS.mny >= 100:
                print("\nYou bought a potion for 100 coins.")
                STATS.mny -= 100
                player_inventory_add(choice)
                input("\nPress Enter to continue...")
            else:
                print("\nYou don't have enough money!")
                input("\nPress Enter to continue...")

        elif choice == "2":
            if STATS.mny >= 200:
                print("\nYou bought an ether for 200 coins.")
                STATS.mny -= 200
                player_inventory_add(choice)
                input("\nPress Enter to continue...")
            else:
                print("\nYou don't have enough money!")
                input("\nPress Enter to continue...")
        elif choice == "0":
            print("\nExiting the store...")
            input("\nPress Enter to continue...")
            player_controls("6")
            break
        else:
            print("\nPlease make a valid choice.")
            input("\nPress Enter to continue...")


def player_inventory_add(choice):
    """
    pushes items bought from the shop in to a dictionery for the player
    """

    if choice == "1":
        player_itm_inv["Potion"] += 1
    elif choice == "2":
        player_itm_inv["Ether"] += 1


def player_inventory_use():
    """
    determines what happens when potions and ethers are used
    """

    clear_console()

    print("""
          1. Potion
          2. Ether
          0. Exit
    """)
    decision = input("\nWhich item would you like to use? ")

    if decision == "1":
        if player_itm_inv["Potion"] > 0:
            clear_console()
            print("\nYou used a potion, hp restored by 200.")
            player_itm_inv["Potion"] -= 1
            STATS.h_p += 200
            if STATS.h_p > STATS.mhp:
                STATS.h_p = STATS.mhp
            input("\nPress Enter to continue...")
            player_inventory_use()
        else:
            clear_console()
            print("\nYou don't have any potions in stock!")
            input("\nPress Enter to continue...")
            player_inventory_use()

    elif decision == "2":
        if player_itm_inv["Ether"] > 0:
            clear_console()
            print("\nYou used an ether, mp restored by 100.")
            player_itm_inv["Ether"] -= 1
            STATS.m_p += 100
            if STATS.m_p > STATS.mmp:
                STATS.m_p = STATS.mmp
            input("\nPress Enter to continue...")
            player_inventory_use()
        else:
            clear_console()
            print("\nYou don't have any ether in stock!")
            input("\nPress Enter to continue...")
            player_inventory_use()

    elif decision == "0":
        clear_console()
        display_inventory()

    else:
        clear_console()
        print("\nPlease make a valid choice.")
        input("\nPress Enter to continue...")
        player_inventory_use()


def display_inventory():
    """
    prints table information
    """

    clear_console()

    print("----INVENTORY----\n\n")

    player_inv_tbl = PrettyTable(["Item", "Quantity"])
    player_inv_tbl.add_row(["Potion",  player_itm_inv.get("Potion")])
    player_inv_tbl.add_row(["Ether",  player_itm_inv.get("Ether")])

    print(player_inv_tbl)

    print("\n\nWould you like to use an item?\n")
    choice = input("(yes / no) ").lower()

    if choice == "yes":
        clear_console()
        player_inventory_use()
    elif choice == "no":
        clear_console()
    else:
        clear_console()
        print("Please make a valid choice.")
        input("Press Enter to continue...")
        display_inventory()


def combi_table():
    """
    combined table for combat so player can compare user stats and enemy stats
    """

    c_s = PrettyTable(["Attribute", Fore.GREEN + "Player Value" +
                       Style.RESET_ALL, "  ", Fore.RED + "Enemy Value"
                       + Style.RESET_ALL])

    c_s.add_row(["NAME", Fore.GREEN + STATS.name + Style.RESET_ALL,
                 "     ", Fore.RED + EST.job + Style.RESET_ALL])
    c_s.add_row(['WEAPON', Fore.GREEN + STATS.itm + Style.RESET_ALL,
                 "     ", Fore.RED + "None" + Style.RESET_ALL])
    c_s.add_row(['LEVEL', Fore.GREEN + str(STATS.lvl) + Style.RESET_ALL,
                 "     ", Fore.RED + str(EST.lvl) + Style.RESET_ALL])
    c_s.add_row(['EXP', Fore.GREEN + str(round(STATS.exp)) + Style.RESET_ALL,
                 "     ", Fore.RED + str(round(EST.exp)) + Style.RESET_ALL])
    c_s.add_row(['HEALTH', Fore.GREEN + str(round(STATS.h_p)) +
                 Style.RESET_ALL, "     ", Fore.RED + str(round(EST.h_p))
                 + Style.RESET_ALL])
    c_s.add_row(['MAGIC', Fore.GREEN + str(round(STATS.m_p)) + Style.RESET_ALL,
                 "     ", Fore.RED + str(round(EST.m_p)) + Style.RESET_ALL])
    c_s.add_row(['ATTACK', Fore.GREEN + str(round(STATS.atk)) +
                 Style.RESET_ALL, "     ", Fore.RED + str(round(EST.atk))
                 + Style.RESET_ALL])
    c_s.add_row(['BLOCK', Fore.GREEN + str(round(STATS.blk)) + Style.RESET_ALL,
                 "     ", Fore.RED + str(round(EST.blk)) + Style.RESET_ALL])
    c_s.add_row(['SPEED', Fore.GREEN + str(round(STATS.spd)) + Style.RESET_ALL,
                 "     ", Fore.RED + str(round(EST.spd)) + Style.RESET_ALL])

    c_s.align["Player Attr"] = "l"
    c_s.align["Player Value"] = "r"
    c_s.align["Enemy Value"] = "r"

    print(c_s)

    STATS.health_bar()
    STATS.magic_bar()


def clear_console():
    """
    clears the console when called
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


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


def item_money_drop():
    """
    chance of an enemy dropping either an ether or potion
    """

    chance_item = random.randint(0, 1)

    if chance_item == 0:

        item_type = random.randint(0, 1)

        if item_type == 0:
            print("\nThe enemy dropped a potion!")
            player_itm_inv["Potion"] += 1

        elif item_type == 1:
            print("\nThe enemy dropped an ether!")
            player_itm_inv["Ether"] += 1

    chance_money = random.randint(0, 1)

    if chance_money == 0:

        money_amount = random.randint(2, 200)
        print("\nThe enemy dropped " + str(money_amount) + " coins!")
        STATS.mny += money_amount


def combat_menu():
    """
    prints the combat menu
    """

    clear_console()

    combi_table()

    print("""
    1 - Physical Attack
    2 - Magical Attack
    3 - Heal
    4 - Use Items
    """)

    print("+-----------+--------------+-------+-------------+\n")


def enemy_action():
    """
    randomly selects enemy attack as object method
    """

    combat_menu()

    if EST.h_p > 0 and STATS.h_p > 0:

        enemy_choice = random.randint(1, 1)

        if enemy_choice == 1:
            EST.attack()

            combat_menu()

            print("The enemy performed a physical attack!")
            time.sleep(1)
            print("\nYou took " + str(round(EST.atk)) + " damage.")
            time.sleep(2)
            player_action()

    elif EST.h_p <= 0 and STATS.h_p > 0:
        print("\nYou defeated the enemy!")
        time.sleep(2)
        print("\nYou gained " + str(round(EST.exp)) + " exp.\n")
        STATS.levelup()
        item_money_drop()
        input("\nPress Enter to continue...")
        clear_console()
        player_controls("5")


def player_action():
    """
    allows for user input during combat, calls object methods
    """

    combat_menu()

    if STATS.h_p > 0 and EST.h_p > 0:

        print("1 / 2 / 3 / 4")

        player_choice = input("\nWhat will you do? \n\n")

        if player_choice == "1":

            STATS.attack()

            combat_menu()

            print("You performed a physical attack!")
            time.sleep(1)
            print("\nThe enemy took " + str(round(STATS.atk)) + " damage.")
            time.sleep(2)
            enemy_action()

        elif player_choice == "3":

            STATS.heal()

            combat_menu()

            print("You healed 50 HP!")
            time.sleep(2)
            enemy_action()

        elif player_choice == "4":

            display_inventory()

            enemy_action()

        else:

            clear_console()
            print("Please make a valid choice.")
            input("\nPress Enter to continue...")
            player_action()

    elif STATS.h_p <= 0:
        print("You were felled by the enemy!")
        print("\nGAME OVER")

        while True:

            play_again = input("\nPlay again? (Yes / No) ").lower()
            if play_again == "yes":
                player_job_selection()
            elif play_again == "no":
                clear_console()
                print("Exiting program...")
                time.sleep(2)
                clear_console()
                sys.exit()
            else:
                clear_console()
                print("\nPlease make a valid choice.")


def combat():
    """
    decides who takes the turn first based on the speed object
    """

    clear_console()

    combat_menu()

    if EST.spd < STATS.spd:
        print("You spotted the enemy before they spotted you!")
        print("You attack first!")
        input("\nPress Enter to continue...")
        player_action()
    else:
        print("The enemy attacks first!")
        input("\nPress Enter to continue...")
        enemy_action()


def enemy_approaches():
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global EST

    enemy_type = random.randint(1, 1)
    level = STATS.lvl + random.randint(1, 5)
    mult = ((level - (level * .95)) + 1)

    if enemy_type == 1:
        EST = EnemyType("Goblin", level, 458*mult, 300*mult, 300*mult,
                        100*mult, 100*mult, 50*mult, 5*mult, 3*mult)
        # EST = EnemyType("Goblin", 1, 458, 300, 300, 100, 100, 50, 50, 3)
        print("You encountered a " + EST.job)
        combat()
    elif enemy_type == 2:
        EST = EnemyType("Witch", level, 454*mult, 100*mult, 100*mult,
                        300*mult, 300*mult, 50*mult, 1*mult, 3*mult)
        print("You encountered a " + EST.job)
        combat()
    elif enemy_type == 3:
        EST = EnemyType("Striga", level, 456*mult, 200*mult, 200*mult,
                        200*mult, 200*mult, 50*mult, 3*mult, 3*mult)
        print("You encountered a " + EST.job)
        combat()


def enemy_encounter():
    """
    randomly generates 1 or 2 as an integer; determines enemy encounter
    """

    encounter_true = random.randint(2, 2)

    if encounter_true == 2:
        enemy_approaches()
    elif encounter_true == 1:
        clear_console()
        print("\nYou did not encounter an enemy.")


def story_arc_5_cave():
    """
    story_arc_5_cave; dictates what happens in the cave
    """

    print(FontStyle().UNDERLINE + "STORY ARC 5 - CAVE\n" + FontStyle().END)

    print("""You're in the cave.""")
    input("Press Enter to continue...")


def story_arc_5_wood():
    """
    story_arc_5_wood; dictates what happens in the woods
    """

    print(FontStyle().UNDERLINE + "STORY ARC 5 - WOOD\n" + FontStyle().END)

    print("""You're in the woods.""")
    input("Press Enter to continue...")


def story_arc_5():
    """
    story_arc_5()
    """
    clear_console()

    print(FontStyle().UNDERLINE + "STORY ARC 5\n" + FontStyle().END)

    print("""
    - - - STORY ARC 4 - - -
    That was a long battle and you're exhausted.
    Feeling tired, you continue down the path.
    The path splits in two and you have to decide which path to follow.

    The first path leads to a cave, the second into a forest.

    Which way do you proceed?

    1. Hunt for enemies
    2. Scavenge
    3. Heal
    4. Shop
    5. View your stats
    6. Path into the cave
    7. Path through the woods

    """)

    path = input("1 / 2 / 3 / 4 / 5 / 6 / 7: \n\n")

    if path == "7":
        story_arc_5_cave()
        story_arc_5()
    if path == "8":
        story_arc_5_wood()
        story_arc_5()
    else:
        player_controls(path)


def story_arc_4():
    """
    story arc 3
    """
    clear_console()

    print(FontStyle().UNDERLINE + "STORY ARC 4\n" + FontStyle().END)

    print("""
    - - - STORY ARC 3 - - -
    Focused and vigilant, you look in the direction you feel the stare.

    Through the thick fog, you catch the glare of a pair of glowing,
    yellow eyes.

    Whatever it is, it knows you've discovered it and it decides to attack!
    """)
    input("\nYou Enter a defensive stance!")

    global EST
    EST = EnemyType("Goblin", 30, 10000, 1000, 1000, 300, 300, 20, 20, 10)
    combat()

    clear_console()

    story_arc_5()


def story_arc_3():
    """
    story arc 3
    """

    clear_console()

    print(FontStyle().UNDERLINE + "STORY ARC 3\n" + FontStyle().END)

    print("""You keep moving along the path, but you know you're not alone.
    The fog is cool on your skin and you still feel the stare from before.
    You make to to the clearing. You sense you are being hunted.

    If you stay out in the open, a battle is inevitable, but you don't
    see anywhere to take shelter.

    Knowing a battle is inevitable, you:
    """)

    print("""
    1. Hunt for enemies
    2. Scavenge
    3. Heal
    4. Shop
    5. View your stats
    6. View your inventory
    7. Look in the direction you feel the stare
    0. Quit the game
    """)

    path = input("1 / 2 / 3 / 4 / 5 / 6 / 7:\n\n")

    if path == "7":
        story_arc_4()
    else:
        player_controls(path)
        story_arc_3()


def story_arc_2():
    """
    story arc 2
    """

    clear_console()

    print(FontStyle().UNDERLINE + "STORY ARC 2\n" + FontStyle().END)

    print("""
    You begin to progress on the dirt path.
    Though you're wearing boots, you can feel the unnaturally cold earth.
    You can't help but feel that through the thick fog...someone...
    ...or something...is watching you.

    You trip on something in the dark and you can feel your heart skip.
    You look to see what it was and you find human remains.
    You pick through the remains and decide to take one of the following:

    Sword
    Axe
    Spear
    """)

    print("""
    1. Hunt for enemies
    2. Scavenge
    3. Heal
    4. Shop
    5. View your stats
    6. View your inventory
    7. Select the Sword
    8. Select the Axe
    9. Select the Spear
    0. Quit the game
    """)

    path = input("1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9:\n\n")

    if path == "7":
        STATS.itm = "Sword"
        STATS.atk += 50
        print("\nYou picked the sword, your attack improved by 50.")
        input("\nPress Enter to move to the next area...")
        story_arc_3()
    elif path == "8":
        STATS.itm = "Axe"
        STATS.atk += 100
        STATS.spd -= 2
        print("\nYou picked up the axe, your attack improves by 100.")
        print("\nThe axe feels heavy and your speed decreases by 1.")
        input("\nPress Enter to move to the next area...")
        story_arc_3()
    elif path == "9":
        STATS.itm = "Spear"
        STATS.atk += 25
        STATS.spd += 2
        print("\nYou picked up the speak, your attack improves by 25.")
        print("\nThe spear is light and your speed improves by 2.")
        input("\nPress Enter to move to the next area...")
        story_arc_3()
    else:
        player_controls(path)
        story_arc_2()


def story_arc_1():
    """
    story arc 1
    """

    clear_console()

    print(FontStyle().UNDERLINE + "STORY ARC 1\n" + FontStyle().END)

    print("Your mind is as clouded as the dense fog that surrounds you.")
    print("You hear the noises of the night, muffled by the thick fog.")
    print("You stand up, look around and decide the following: ")

    print("""
    1. Hunt for enemies
    2. Scavenge
    3. Heal
    4. Shop
    5. View your stats
    6. View your inventory
    7. Follow the dirt path into the thick fog
    0. Quit the game
    """)

    path = input("1 / 2 / 3 / 4 / 5 / 6 / 7:\n\n")

    if path == "7":
        story_arc_2()
    else:
        player_controls(path)
        story_arc_1()


def player_controls(path):
    """
    player controls
    """

    if STATS.h_p > 0:

        if path == "1":
            enemy_encounter()
        elif path == "2":
            scavenge()
            input("\nPress Enter to continue...")
        elif path == "3":
            STATS.heal()
            print("\nYou healed hp.")
            input("\nPress Enter to continue...")
        elif path == "4":
            shop()
        elif path == "5":
            clear_console()
            STATS.full_stats()
            input("\nPress Enter to continue...")
        elif path == "6":
            clear_console()
            print("\nYou viewed your inventory.\n")
            display_inventory()
        elif path == "0":
            clear_console()
            print("Exiting program...")
            time.sleep(2)
            clear_console()
            sys.exit()
        else:
            clear_console()
            print("\nPlease make a valid choice.")
            input("\nPress Enter to continue...")

    elif STATS.h_p < 0:
        print("\nYou were felled by the enemy!")
        print("\nGAME OVER")

        while True:

            play_again = input("\nPlay again? (Yes / No) ").lower()
            if play_again == "yes":
                player_job_selection()
            elif play_again == "no":
                clear_console()
                print("Exiting program...")
                time.sleep(2)
                clear_console()
                sys.exit()
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
    print("\nIt's cold and dark. You look around and can't see anything...")
    time.sleep(1)
    print("\n...or for that matter...remember anything...except...\n")
    time.sleep(1)

    while True:

        STATS.full_stats()
        confirm = input("\nIs this how your story begins? (Yes / No) ").lower()

        if confirm == "yes":
            story_arc_1()
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
        STATS = PlayerJob(pname, 1, 0, 600, pjob, "None",
                          300, 300, 100, 100, 200, 100, 150)
        confirm_choice()

    elif player_choice == "assassin":
        pname = input("What is your name, assassin? ")
        pjob = "Assassin"
        STATS = PlayerJob(pname, 1, 0, 1000, pjob, "None",
                          200, 200, 200, 200, 150, 150, 200)
        confirm_choice()

    elif player_choice == "mage":
        pname = input("What is your name, mage? ")
        pjob = "Mage"
        STATS = PlayerJob(pname, 1, 0, 200, pjob, "None",
                          100, 100, 300, 300, 100, 200, 100)
        confirm_choice()

    else:
        print("Please make a valid choice: \n")
        player_job_selection()


while True:

    player_job_selection()
