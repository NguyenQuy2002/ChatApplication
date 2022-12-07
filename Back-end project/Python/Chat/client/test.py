import socket
import threading
from tkinter import *


class GUI:
    def __init__(self):

        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title('Login')
        self.login.resizable(width=False, height=False)
        self.login.configure(width=500, height=500)

        self.pls = Label(self.login, text='Please login to continue',
                        justify=CENTER, font='Helvetica 13 bold', background='yellow')
        
        self.pls.place(relheight=0.05, relx=0.2, rely=0.05)
        
        self.Window.update()
        self.Window.mainloop()

g = GUI()
