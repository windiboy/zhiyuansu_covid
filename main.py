from robotpi_movement import Movement
from robotpi_serOp import serOp


class Covid():
    def __init__(self):
        self.ser = serOp()
        self.movement = Movement()

    def test(self):
        self.movement.wave_hands()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    covid = Covid()
    covid.test()

