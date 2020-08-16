from robotpi_movement import Movement
from robotpi_serOp import serOp
import serial
import time

class Covid():
    def __init__(self):
        self.ser = serOp()
        self.mv = Movement()
        self.sensor = serial.Serial("/dev/ttyUSB1", 9600, timeout=0.5)

    def read_temperature(self):
        self.mv.set_volume(80)
        self.mv.play_sounds('0255\\0113.WAV')#请伸出手配合体温测量
        data = self.sensor.readline()
        temperature = (data[0]-48) * 10 + (data[1]-48) + (data[3]-48) * 0.1
        self.mv.play_sounds('0255\\0112.WAV')  # 您的体温是
        self.mv.play_sounds('0255\\00'+str(data[0]-48)+str(data[1]-48)+'.WAV')
        print("Your temperature is : {}".format(temperature))
        if temperature>37.3:
            self.mv.play_sounds('0255\\0111.WAV')  # 您的体温过高

    def run(self):
        while True:
            # self.mv.action_2()
            self.read_temperature()
            # time.sleep(2)
            # self.mv.action_1()
            time.sleep(10)


if __name__ == '__main__':
    covid = Covid()
    covid.run()

