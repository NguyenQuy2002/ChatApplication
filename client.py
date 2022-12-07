import socket
import threading
from tkinter import *
from random import randint
import os


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below",
          bg="orange", font='Calibri 16 bold', width="400", height="2").pack()
    Label(register_screen, text="").pack()
    username_label = Label(
        register_screen, text="New Username:", font='Calibri 13 bold')
    username_label.pack()
    username_entry = Entry(
        register_screen, textvariable=username, font='Calibri 13 bold')
    username_entry.pack()
    username_label = Label(
        register_screen, text="New Password:", font='Calibri 13 bold')
    username_label.pack()
    password_entry = Entry(
        register_screen, textvariable=password, show='*', font='Calibri 13 bold')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=30,
           height=1, bg="orange", command=register_user).pack()


def register_user():

    username_info = username.get()
    password_info = password.get()

# Open file in write mode
    file = open(username_info, "w")

# write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    Label(login_screen, text="Please enter details below to login", bg='orange',
          font='Calibri 16 bold', width="400", height="2").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="").pack()
    Label(login_screen, text="Username:", font='Calibri 13 bold').pack()
    username_login_entry = Entry(
        login_screen, textvariable=username_verify, font='Calibri 13 bold')
    username_login_entry.pack()
    Label(login_screen, text="Password:", font='Calibri 13 bold').pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*', font='Calibri 13 bold')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=30,
           height=1, command=login_verify).pack()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, "r")

        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        print('User not found!')


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()

    Button(login_success_screen, text="OK",
           command=login_success_screen.destroy()).pack()
    

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=password_not_recog_screen.destroy()).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="orange", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
