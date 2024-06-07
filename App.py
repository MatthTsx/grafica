import customtkinter as CTk
from reader import Connection

class App(CTk.CTk):
    
    _reader: Connection
    _btnText: CTk.StringVar

    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("Humberto")
        self._reader = Connection()
        self._btnText = CTk.StringVar()
        self._btnText.set("Stop")
        self._init_Components()
    
    def _init_Components(self):
        CTk.CTkLabel(self, textvariable=self._reader.response).grid(column=0, row=0, sticky="nsew")
        CTk.CTkButton(self, textvariable=self._btnText, command=self.Btn_Toggle).grid(column=0, row=1, sticky="nsew")
    
    def Btn_Toggle(self):
        if self._reader.reading:
            self._reader.Stop()
            self._btnText.set("Resume")
        else:
            self._reader.Open()
            self._btnText.set("Stop")
    
    def Exit(self):
        self._reader.Exit = True
