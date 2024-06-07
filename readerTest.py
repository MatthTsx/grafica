import serial
from customtkinter import StringVar
from time import sleep

class Connection():
    reading: bool = True
    response: StringVar
    Exit = False

    def __init__(self):
        # self.open()
        self.response = StringVar()

    def loop(self):
        while True:
            if self.Exit: return
            if not self.reading: continue
            try:
                # value = float(self.readline().decode('utf-8').strip())
                value = 2
                self.response.set("Distancia: " + str(value) + "cm")
                if value < 10: print("RED")
                elif value <= 20: print("YELLOW")
                elif value > 20: print("GREEN")
            except: pass
            sleep(1/60)
    
    def Stop(self):
        # self.close()
        self.reading = False
    
    def Open(self):
        # self.open()
        self.reading = True