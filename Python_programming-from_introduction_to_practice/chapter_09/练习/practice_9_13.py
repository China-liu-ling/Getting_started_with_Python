from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print("\n")
        for x in range(0, 10):
            print(f"{randint(1, self.sides)}")

dice_1 = Die()
dice_1.roll_die()

dice_2 = Die(sides=10)
dice_2.roll_die()

dice_3 = Die(sides=20)
dice_3.roll_die()