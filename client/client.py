import socket
import threading
from tkinter import *
from random import randint
import os
from tkinter import messagebox
from wsgiref.simple_server import server_version

from sympy import re

HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 3001

ADMIN_ADDR = socket.gethostbyname(socket.gethostname())
ADMIN_PORT = 3000


class User:
    def __init__(self):
        self.num_clients = 0
        self.server_addr = socket.gethostbyname(HOST_ADDR)
        self.server_port = HOST_PORT

        self.client_addr = socket.gethostbyname(HOST_ADDR)
        self.client_port = ADMIN_PORT

        self.server = socket.socket()
        self.client = socket.socket()

        self.server.bind((self.server_addr, 0))
        self.server.listen(10)

    def serverConnecting(self, server_addr):
        self.client_addr = server_addr
        print(self.client_addr)
        try:
            self.client.connect((self.client_addr, self.client_port))
            messagebox.showinfo('Information', 'Welcome to chat room!')
            # mainFrame.place(relheight=0, relwidth=0)
            # loginFrame.place(relheight=1, relwidth=1)
        except:
            messagebox.showerror("ERROR", 'Invalid ID')


if __name__ == "__main__":
    print('Running the User Interface')
    root = Tk()

    user = User()

    root.title('User chat application')
    root.geometry('450x450')
    root.protocol('WM_DELETE_WINDOW')

    # --------------------MAIN FRAME-----------------------#
    # mainFrame = Frame(root)
    # mainFrame.config(bg='#CCE5FF')
    # mainFrame.place(relheight=1, relwidth=1)

    # --------------------Main intro-----------------------#
    # mainIntro = Label(mainFrame, text='Welcome to Chat Application!')
    # mainIntro.config(bg='#0066CC', font=('Calibri', 13, 'bold'),
    #                  borderwidth=1, relief=SOLID, fg='#fff')
    # mainIntro.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.05)

    # --------------------Main IP input-----------------------#
    # mainIPinput = Entry(mainFrame)
    # mainIPinput.config(bg='#fff', relief=SUNKEN, font=('Calibri', 10, 'bold'))
    # mainIPinput.place(relheight=0.08, relwidth=0.55, relx=0.35, rely=0.25)

    # --------------------Main label-----------------------#
    # mainLabel = Label(mainFrame, text='Enter ID room')
    # mainLabel.config(bg='#0066CC', font=('Calibri', 10, 'bold'),
    #                  borderwidth=1, relief=SOLID, fg='#fff')
    # mainLabel.place(relheight=0.08, relwidth=0.2, relx=0.1, rely=0.25)

    # --------------------Main button-----------------------#
    # mainButton = Button(mainFrame, text='Connect')
    # mainButton.config(bg='#0066CC', font=('Calibri', 11, 'bold'),
    #                   borderwidth=2, relief=RAISED, fg='#fff', command=lambda: user.serverConnecting(mainIPinput.get()))
    # mainButton.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.5)

    # # --------------------LOGIN FRAME-----------------------#
    # loginFrame = Frame(root)
    # loginFrame.config(bg='#CCE5FF')
    # loginFrame.place(relheight=1, relwidth=1)

    # # --------------------Login intro component-----------------------#
    # loginIntro = Label(loginFrame, text='Welcome to Chat Application!')
    # loginIntro.config(bg='#0066CC', font=('Calibri', 13, 'bold'),
    #                   borderwidth=1, relief=SOLID, fg='#fff')
    # loginIntro.place(relheight=0.1, relwidth=0.7, relx=0.15, rely=0.05)

    # # --------------------Login pls component-----------------------#
    # loginPls = Label(
    #     loginFrame, text='Please enter the username and password to login')
    # loginPls.config(font=('Calibri', 10, 'bold'))
    # loginPls.place(relheight=0.08, relwidth=0.7, relx=0.15, rely=0.17)

    # # --------------------Login username component-----------------------#
    # loginUserInput = Entry(loginFrame)
    # loginUserInput.config(bg='#fff', relief=SUNKEN,
    #                       font=('Calibri', 12, 'bold'))
    # loginUserInput.place(relheight=0.08, relwidth=0.55, relx=0.35, rely=0.3)

    # loginUser = Label(loginFrame, text='Username: ')
    # loginUser.config(bg='#CCE5FF', font=('Calibri', 12, 'bold'), relief=FLAT)
    # loginUser.place(relheight=0.08, relwidth=0.2, relx=0.1, rely=0.3)

    # # --------------------Login password component-----------------------#
    # loginPassInput = Entry(loginFrame)
    # loginPassInput.config(bg='#fff', font=(
    #     'Calibri', 12, 'bold'), relief=SUNKEN)
    # loginPassInput.place(relheight=0.08, relwidth=0.55, relx=0.35, rely=0.45)

    # loginPass = Label(loginFrame, text='Password: ')
    # loginPass.config(bg='#CCE5FF', relief=FLAT,
    #                  font=('Calibri', 12, 'bold'))
    # loginPass.place(relheight=0.08, relwidth=0.2, relx=0.1, rely=0.45)

    # # --------------------Login button component-----------------------#
    # loginButton = Button(loginFrame, text='Login')
    # loginButton.config(bg='#0066CC', relief=RAISED,
    #                    font=('Calibri', 12, 'bold'))
    # loginButton.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.6)

    # --------------------CHATTING FRAME-----------------------#

    chatFrame = Frame(root)
    chatFrame.place(relheight=1, relwidth=1)

    # --------------------Friend list-----------------------#
    friendsFrame = Frame(chatFrame)
    friendsFrame.config(bg='#0066CC')
    friendsFrame.place(relheight=1, relwidth=0.2, relx=0, rely=0)

    friendsIntro = Label(friendsFrame, text='Friends')
    friendsIntro.config(bg='#0066CC', font=(
        'Calibri', 12, 'bold'), borderwidth=1, relief=SOLID)
    friendsIntro.place(relwidth=1, relx=0, rely=0)

    # --------------------Display Chat-----------------------#
    displayFrame = Frame(chatFrame)
    displayFrame.config(bg='#CCE5FF')
    displayFrame.place(relheight=0.9, relwidth=0.8, relx=0.2, rely=0)

    # --------------------Message Bar-----------------------#
    messageFrame = Frame(chatFrame)
    messageFrame.config(bg='#fff')
    messageFrame.place(relheight=0.1, relwidth=0.8, relx=0.2, rely=0.9)

    sendFileButton = Button(messageFrame, text='File')
    sendFileButton.config(relief=SUNKEN, borderwidth=1)
    sendFileButton.place(relheight=1, relwidth=0.1, relx=0, rely=0)

    sendMessButton = Button(messageFrame, text='Send')
    sendMessButton.config(relief=SUNKEN, borderwidth=1)
    sendMessButton.place(relheight=1, relwidth=0.1, relx=0.1, rely=0)

    messengerInput = Entry(messageFrame)

    chatFrame.mainloop()

    # root.mainloop()
