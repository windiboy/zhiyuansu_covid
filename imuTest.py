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

        self.mv.angle_control(2200, 2100, 800, 1800)
        time.sleep(2)

        datahex = self.sensor.ser.read(33)
        self.sensor.DueData(datahex)
        self.offset = self.sensor.Angle[1]
        time.sleep(1)
        print("Auto Adjustment Begin:")

    def run(self):
        p1 = 2200
        p4 = 1800
        while True:
            datahex = self.sensor.ser.read(33)
            self.sensor.DueData(datahex)
            print("Angle Y = {:.3f}".format(self.sensor.Angle[1]))
            cur = self.sensor.Angle[1] - self.offset
            if cur < -1:
                p1 = p1-10
                p4 = p4+10
            elif cur > 1:
                p1 = p1+10
                p4 = p4-10
            else:
                pass
            if p1 > 3700:
                p1=3700
                print("out of range")
            elif p1 <700:
                p1=700
                print("out of range")
            elif p4 > 3000:
                p4=3000
                print("out of range")
            elif p4 <700:
                p4=700
            else:
                pass
            self.mv.angle_control(p1, 2100, 800, p4)


if __name__ == '__main__':
    my = Adjustment()
    my.run()

