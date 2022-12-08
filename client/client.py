import socket
import threading
from tkinter import *
from random import randint
import os


class GUI():
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.geometry("300x250")
        self.main_screen.title("Account Login")

        Label(text="Select Your Choice", bg="orange", width="300",
              height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="3", width="30", command=self.login).pack()
        Label(text="").pack()
        Button(text="Register", height="3", width="30",
               command=self.register).pack()

        self.main_screen.mainloop()

    def register(self):
        self.register_screen = Toplevel(self.main_screen)
        self.register_screen.title("Account Register")
        self.register_screen.geometry("400x300")

        self.username = StringVar()
        self.password = StringVar()

        Label(self.register_screen, text="Please enter details below",
              bg="orange", font='Calibri 16 bold', width="400", height="2").pack()
        Label(self.register_screen, text="").pack()

        self.username_label = Label(
            self.register_screen, text="New Username:", font='Calibri 13 bold')
        self.username_label.pack()

        self.username_entry = Entry(
            self.register_screen, textvariable=self.username, font='Calibri 13 bold')
        self.username_entry.pack()

        self.username_label = Label(
            self.register_screen, text="New Password:", font='Calibri 13 bold')
        self.username_label.pack()

        self.password_entry = Entry(
            self.register_screen, textvariable=self.password, show='*', font='Calibri 13 bold')
        self.password_entry.pack()

        Label(self.register_screen, text="").pack()
        Button(self.register_screen, text="Register", width=30,
               height=1, bg="orange", command=self.register_user).pack()

    def login(self):
        self.login_screen = Toplevel(self.main_screen)
        self.login_screen.title("Login")
        self.login_screen.geometry("400x300")
        Label(self.login_screen, text="Please enter details below to login", bg='orange',
              font='Calibri 16 bold', width="400", height="2").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Username:",
              font='Calibri 13 bold').pack()
        self.username_login_entry = Entry(
            self.login_screen, textvariable=self.username_verify, font='Calibri 13 bold')
        self.username_login_entry.pack()
        Label(self.login_screen, text="Password:",
              font='Calibri 13 bold').pack()
        self.password_login_entry = Entry(
            self.login_screen, textvariable=self.password_verify, show='*', font='Calibri 13 bold')
        self.password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        # Button(login_screen, text="Login", width=30, height=1, command=login_verify).pack()
        Button(self.login_screen, text="Login", width=30,
               height=1, command=self.chat_layout).pack()

    def register_user(self):

        self.username_info = self.username.get()
        self.password_info = self.password.get()

    # Open file in write mode
        self.file = open(self.username_info, "w")

    # write username and password information into file
        self.file.write(self.username_info + "\n")
        self.file.write(self.password_info)
        self.file.close()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        Label(self.register_screen, text="Registration Success",
              fg="green", font=("Calibri", 11)).pack()

    def login_verify(self):

        self.username1 = self.username_verify.get()
        self.password1 = self.password_verify.get()

        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        list_of_files = os.listdir()

        if self.username1 in list_of_files:
            file1 = open(self.username1, "r")

            verify = file1.read().splitlines()
            if self.password1 in verify:
                login_success()
            else:
                self.password_not_recognised()
        else:

            print('User not found!')

    def login_success(self):

        self.login_success_screen = Toplevel(self.login_screen)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        Label(self.login_success_screen, text="Login Success").pack()

        Button(self.login_success_screen, text="OK",
               command=self.login_success_screen.destroy()).pack()

    def password_not_recognised(self):
        self.password_not_recog_screen = Toplevel(self.login_screen)
        self.password_not_recog_screen.title("Success")
        self.password_not_recog_screen.geometry("150x100")
        Label(self.password_not_recog_screen, text="Invalid Password ").pack()
        Button(self.password_not_recog_screen, text="OK",
               command=self.password_not_recog_screen.destroy()).pack()

    def chat_layout(self):
        self.name = self.username_login_entry
        # to show chat window
        self.Window = Tk()
        self.Window.withdraw()
        self.Window.deiconify()
        self.Window.title("Chat room")
        self.Window.resizable(width=False,
                              height=False)
        self.Window.configure(width=470,
                              height=550,
                              bg="#17202A")
        self.labelHead = Label(self.Window,
                               bg="#17202A",
                               fg="#EAECEE",
                               text=self.name,
                               font="Helvetica 13 bold",
                               pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,
                          width=450,
                          bg="#ABB2B9")

        self.line.place(relwidth=1,
                        rely=0.07,
                        relheight=0.012)

        self.textCons = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 14",
                             padx=5,
                             pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.labelBottom = Label(self.Window,
                                 bg="#ABB2B9",
                                 height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.825)

        self.entryMsg = Entry(self.labelBottom,
                              bg="#2C3E50",
                              fg="#EAECEE",
                              font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74,
                            relheight=0.06,
                            rely=0.008,
                            relx=0.011)

        self.entryMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text="Send",
                                font="Helvetica 10 bold",
                                width=20,
                                bg="#ABB2B9",
                                command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.06,
                             relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        self.scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        self.scrollbar.place(relheight=1,
                             relx=0.974)

        self.scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

    def sendButton(self, msg):
        self.textCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    # function to receive messages

    # def receive(self):
    #     while True:
    #         try:
    #             message = client.recv(1024).decode(FORMAT)

    #             # if the messages from the server is NAME send the client's name
    #             if message == 'NAME':
    #                 client.send(name.encode(FORMAT))
    #             else:
    #                 # insert messages to text box
    #                 textCons.config(state=NORMAL)
    #                 textCons.insert(END,
    #                                 message+"\n\n")

    #                 textCons.config(state=DISABLED)
    #                 textCons.see(END)
    #         except:
    #             # an error will be printed on the command line or console if there's an error
    #             print("An error occurred!")
    #             client.close()
    #             break

    # # function to send messages

    # def sendMessage(self):
    #     self.textCons.config(state=DISABLED)
    #     while True:
    #         message = (f"{name}: {msg}")
    #         client.send(message.encode(FORMAT))
    #         break


g = GUI()
