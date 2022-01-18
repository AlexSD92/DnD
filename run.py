def player_details():
    """
    prompts the user to select their class and enter name and age
    """
    pclass = input("What are you? (Warrior / Mage / Assassin) ")

    if pclass == "Warrior":

        class Warrior:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            HP = 300
            ST = 5
            DF = 5
            MA = 1
            MD = 1
            SP = 3

        p1 = Warrior(input("Your name: "), int(input("Your age: ")))

        print("Name:..." + p1.name)
        print("Age:...." + str(p1.age))
        print("HP:....." + str(p1.HP))
        print("ST:....." + str(p1.ST))
        print("DF:....." + str(p1.DF))
        print("MA:....." + str(p1.MA))
        print("MD:....." + str(p1.MD))
        print("SP:....." + str(p1.SP))


    elif pclass == "Mage":

        class Mage:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            HP = 100
            ST = 1
            DF = 3
            MA = 5
            MD = 5
            SP = 1

        p1 = Mage(input("Your name: "), int(input("Your age: ")))

        print("Name:..." + p1.name)
        print("Age:...." + str(p1.age))
        print("HP:....." + str(p1.HP))
        print("ST:....." + str(p1.ST))
        print("DF:....." + str(p1.DF))
        print("MA:....." + str(p1.MA))
        print("MD:....." + str(p1.MD))
        print("SP:....." + str(p1.SP))


    elif pclass == "Assassin":

        class Assassin:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            HP = 200
            ST = 3
            DF = 1
            MA = 3
            MD = 1
            SP = 5

        p1 = Assassin(input("Your name: "), int(input("Your age: ")))

        print("Name:..." + p1.name)
        print("Age:...." + str(p1.age))
        print("HP:....." + str(p1.HP))
        print("ST:....." + str(p1.ST))
        print("DF:....." + str(p1.DF))
        print("MA:....." + str(p1.MA))
        print("MD:....." + str(p1.MD))
        print("SP:....." + str(p1.SP))

player_details()