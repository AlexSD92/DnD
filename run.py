import random

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


class player_job():
    def __init__(self, name, job, hp, mp, atk, blk, matk, mblk, spd):
        self.name = name
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
        \n NAME - {}\n JOB - {}\n HEALTH - {}\n MAGIC - {}\n ATTACK - {}\n BLOCK - {}\n M. ATTACK - {}\n M. DEFENSE - {}\n SPEED - {}\n
        """.format(self.name, self.job, self.hp, self.mp, self.atk, self.blk, self.matk, self.mblk, self.spd)

    def hp_boost(self):
        self.hp += 100

def enemy_approaches():
    """
    randomly generates 1, 2 or 3 and pushes forward an enemy type
    """

    global goblin
    global witch
    global striga

    global ENEMY
    ENEMY = random.randint(1,3)

    if ENEMY == 1:
        goblin = enemy_type("Goblin", 300, 100, 5, 5, 1, 1, 3)
        print(goblin.full_stats())
    elif ENEMY == 2:
        witch = enemy_type("Witch", 100, 300, 1, 1, 5, 5, 3)
        print(witch.full_stats())
    elif ENEMY == 3:
        striga = enemy_type("Striga", 200, 200, 3, 3, 3, 3, 3)
        print(striga.full_stats())

def enemy_encounter():
    """
    randomly generates 1 or 2 as an integer; will be used to determine if there is an enemy encounter
    """

    global ENCOUNTER
    ENCOUNTER = random.randint(1,2)

    if ENCOUNTER == 2:
        print("you encountered an ememy")
        print(ENCOUNTER)
        enemy_approaches()
    else:
        print("no enemy encounter")
        print(ENCOUNTER)
    

def story_arc_1():
    """
    inital story setup; currently a test function
    """

    print(stats.name + ", you wake up next to a dying fire. It's cold, wet and dark.")
    stats.hp_boost()
    print(stats.hp)
    enemy_encounter()


def player_job_selection():
    """
    player choice of class and name input
    """
    global stats

    player_choice = input("What class would you like to be? (warrior / assassin / mage) ")

    if player_choice == "warrior":
        pname = input("What is your name, warrior? ")
        pjob = "Warrior"
        stats = player_job(pname, pjob, 300, 100, 5, 5, 1, 1, 3)
        print(stats.full_stats())

    elif player_choice == "assassin":
        pname = input("What is your name, assassin? ")
        pjob = "Assassin"
        stats = player_job(pname, pjob, 200, 200, 3, 1, 3, 1, 5)
        print(stats.full_stats())

    elif player_choice == "mage":
        pname = input("What is your name, mage? ")
        pjob = "Mage"
        stats = player_job(pname, pjob, 100, 300, 1, 1, 5, 5, 1)
        print(stats.full_stats())

    story_arc_1()

while True:
    player_job_selection()
    