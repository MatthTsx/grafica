import customtkinter as CTk
from App import App
import threading as th


app = App()

t = th.Thread(target=app._reader.loop)
t.start()

app.mainloop()
print("aaa")
app.Exit()