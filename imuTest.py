from robotpi_movement import Movement
from robotpi_serOp import serOp
from WitSensor import ImuSensor
import serial
import time

class Adjustment():
    def __init__(self):
        self.ser = serOp()
        self.mv = Movement()
        self.sensor = ImuSensor()

    def run(self):
        while True:
            datahex = self.sensor.ser.read(33)
            self.sensor.DueData(datahex)
            print("Angle Y = {:.3f}".format(self.sensor.Angle[1]))


if __name__ == '__main__':
    my = Adjustment()
    my.run()

