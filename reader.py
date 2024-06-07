import serial
from customtkinter import StringVar
from time import sleep

class Connection(serial.Serial):
    reading: bool = True
    response: StringVar
    Exit = False

    def __init__(self):
        super().__init__('COM6', 9600)
        self.open()
        self.response = StringVar()

    def loop(self):
        while True:
            if self.Exit: break
            if not self.reading: continue
            try:
                value = float(self.readline().decode('utf-8').strip())
                self.response.set("Distancia: " + str(value) + "cm")
                if value < 10: self.write(b"r")
                elif value <= 20: self.write(b"y")
                elif value > 20: self.write(b"g")
            except: pass
            sleep(1/60)
    
    def Stop(self):
        self.close()
        self.reading = False
    
    def Open(self):
        self.open()
        self.reading = True