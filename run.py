import random

class boss_type():
    def __init__(self, job, hp, mp, atk, blk, matk, mblk, spd):
        self.job = job
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.blk = blk
        self.matk = matk
        self.mblk = mblk
        self.spd = spd  

    def full_stats(self):
        return """
        \n JOB - {}\n HEALTH - {}\n MAGIC - {}\n ATTACK - {}\n BLOCK - {}\n M. ATTACK - {}\n M. DEFENSE - {}\n SPEED - {}\n
        """.format(self.job, self.hp, self.mp, self.atk, self.blk, self.matk, self.mblk, self.spd)

    def attack(self):
        stats.hp -= self.atk - stats.blk

    def magic_attack(self):
        stats.hp -= self.matk - stats.mblk

DRAGON = boss_type("Seath the Scaleless Dragon", 2000, 2000, 200, 1, 1, 1, 1)

class enemy_type():
    def __init__(self, job, hp, mp, atk, blk, matk, mblk, spd):
        self.job = job
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.blk = blk
        self.matk = matk
        self.mblk = mblk
        self.spd = spd  

    def full_stats(self):
        return """
        \n JOB - {}\n HEALTH - {}\n MAGIC - {}\n ATTACK - {}\n BLOCK - {}\n M. ATTACK - {}\n M. DEFENSE - {}\n SPEED - {}\n
        """.format(self.job, self.hp, self.mp, self.atk, self.blk, self.matk, self.mblk, self.spd)

    def attack(self):
        stats.hp -= self.atk - stats.blk

    def magic_attack(self):
        stats.hp -= self.matk - stats.mblk

class player_job():
    def __init__(self, name, job, itm, hp, mp, atk, blk, matk, mblk, spd):
        self.name = name
        self.job = job
        self.itm = itm
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.blk = blk
        self.matk = matk
        self.mblk = mblk
        self.spd = spd

    def full_stats(self):
        return """
        \n NAME - {}\n JOB - {}\n WEAPON - {}\n HEALTH - {}\n MAGIC - {}\n ATTACK - {}\n BLOCK - {}\n M. ATTACK - {}\n M. DEFENSE - {}\n SPEED - {}\n
        """.format(self.name, self.job, self.itm, self.hp, self.mp, self.atk, self.blk, self.matk, self.mblk, self.spd)

    def hp_boost(self):
        self.hp += 100
    
    def attack(self):
        enemy_stats.hp -= self.atk - enemy_stats.blk

    def magic_attack(self):
        enemy_stats.hp -= self.matk - enemy_stats.mblk

    def heal(self):
        if self.mp > 0:
            self.mp -= 50
            self.hp += 50

    def sword(self):
        stats.atk += 5

    def staff(self):
        stats.matk += 5

    def dagger(self):
        stats.atk += 1
        stats.matk += 1
        stats.spd += 1

def enemy_action():
    """
    produces enemy attack as either a magic or physical attack from random integer
    """
    if enemy_stats.hp > 0:
  
        enemy_choice = random.randint(1,2)

        if enemy_choice == 1:
            print("The enemy performed a physical attack!")
            enemy_stats.attack()
            player_action()
        elif enemy_choice == 2:
            print("The enemy performed a magical attack!")
            enemy_stats.magic_attack()
            player_action()

    else: 
        print("You defeated the enemy!")   

def player_action():

    if stats.hp > 0:

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
            stats.attack()
            print("Remaining enemy health: " + str(enemy_stats.hp))
            enemy_action()
        elif player_choice == "2":
            print("You performed a magical attack!")    
            stats.magic_attack()
            enemy_action()
        elif player_choice == "3":
            print("You healed 50 HP!")
            stats.heal()
            enemy_action()
        elif player_choice == "4":
            print("You unleashed your inner strength!")
            enemy_action()
        elif player_choice == "5":
            print(stats.full_stats())

    else:
        print("You were felled by the enemy!")
        print("GAME OVER")

def combat():
    """
    decides who takes the turn first based on the speed object
    """
    while enemy_stats.hp > 0 and stats.hp > 0:
        if enemy_stats.spd < stats.spd:
            print("player goes first")
            player_action()
        else:
            print("enemy goes first")
            enemy_action()

def enemy_approaches():
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global enemy_stats

    global ENEMY
    ENEMY = random.randint(1,3)

    if ENEMY == 1:
        enemy_stats = enemy_type("Goblin", 300, 100, 50, 5, 1, 1, 3)
        print(enemy_stats.full_stats())
        combat()
    elif ENEMY == 2:
        enemy_stats = enemy_type("Witch", 100, 300, 50, 1, 5, 5, 3)
        print(enemy_stats.full_stats())
        combat()
    elif ENEMY == 3:
        enemy_stats = enemy_type("Striga", 200, 200, 50, 3, 3, 3, 3)
        print(enemy_stats.full_stats())
        combat()

def enemy_encounter():
    """
    randomly generates 1 or 2 as an integer; will be used to determine if there is an enemy encounter
    """

    global ENCOUNTER
    ENCOUNTER = random.randint(2,2)

    if ENCOUNTER == 2:
        print("you encountered an ememy")
        print(ENCOUNTER)
        enemy_approaches()
    else:
        print("no enemy encounter")
        print(ENCOUNTER)

def story_arc_2v2():
    enemy_encounter()
    print("story arc 2")

def story_arc_2v1():
    enemy_encounter()
    print("story arc 2")

def story_arc_1():
    """
    inital story setup; currently a test function
    """

    print("\n\n" + stats.name + ", you wake up next to a dying fire.")
    print("It's cold, wet and dark. You look around and can't see anything...")
    print("...or for that matter...remember anything...except...")
    print(stats.full_stats())
    print("Your mind is as clouded as the dense fog that is surrounding you.")
    print("You hear the noises of the night, muffled by the thick fog.")
    print("You stand up and decide the following: ")
    print("""
    1. Decide to keep the fire alive.
    2. Follow the noises you hear in the distance.
    """)

    path = input("Please input '1' or '2' to decide: ")

    if path == "1":
        story_arc_2v1()
    elif path == "2":
        story_arc_2v2()
    else:
        print("Please make a valid choice.")

def player_job_selection():
    """
    player choice of class and name input
    """
    global stats

    player_choice = input("What class would you like to be? (warrior / assassin / mage) ")

    if player_choice == "warrior":
        pname = input("What is your name, warrior? ")
        pjob = "Warrior"
        stats = player_job(pname, pjob, "None", 300, 100, 100, 5, 1, 1, 3)
        # print(stats.full_stats())

    elif player_choice == "assassin":
        pname = input("What is your name, assassin? ")
        pjob = "Assassin"
        stats = player_job(pname, pjob, "None", 200, 200, 100, 1, 3, 1, 5)
        # print(stats.full_stats())

    elif player_choice == "mage":
        pname = input("What is your name, mage? ")
        pjob = "Mage"
        stats = player_job(pname, pjob, "None", 100, 300, 100, 1, 5, 5, 1)
        # print(stats.full_stats())

    story_arc_1()

while True:
    player_job_selection()
    