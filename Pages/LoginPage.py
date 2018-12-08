from tkinter import *
from tkinter import messagebox
import json

class LoginPage(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg='red')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        Label0 = Label(self, text='Login Page', font="Times 16 bold")
        Label0.pack(padx=15, pady=5)

        Label1 = Label(self, text='Username:')
        Label1.pack(padx=15, pady=5)

        self.entry1 = Entry(self, bd=5)
        self.entry1.pack(padx=15, pady=5)

        Label2 = Label(self, text='Password:')
        Label2.pack(padx=15, pady=6)

        self.entry2 = Entry(self, bd=5)
        self.entry2.pack(padx=15, pady=7)


        # Button to click to check login credentials
        # btn = Button(self, text='Check Login', command=self.RegisteredUserLogin(parent))
        btn = Button(self, text='Check Login', command=self.RegisteredUserLogin)

        # Button to log in as a guest
        from Pages.CreateGuestUserAccount import CreateGuestUserAccount
        btn2 = Button(self, text='Create Guest User Account', command=lambda: parent.show_frame(CreateGuestUserAccount))

        btn.pack(padx=5)
        btn2.pack(padx=6)

    # def RegisteredUserLogin(self, parent):
    def RegisteredUserLogin(self):
        username = self.entry1.get()
        password = self.entry2.get()

        try:
            GU_file = open('Databases/Users/GU.json', 'r')
            GU_dict = json.load(GU_file)
        except FileNotFoundError:
            GU_file = open('Databases/Users/GU.json', 'w') # create GU.json
            json.dump({}, GU_file) # and initialize it as empty dictionary
            GU_dict = {}

        try:
            OU_file = open('Databases/Users/OU.json', 'r')
            OU_dict = json.load(OU_file)
        except FileNotFoundError:
            OU_file = open('Databases/Users/OU.json', 'w') # create OU.json
            json.dump({}, OU_file) # and initialize it as an empty dictionary
            OU_dict = {}

        from Application import Application
        if username in GU_dict and password == GU_dict[username] or username == 'g' and password == 'g':
            from Pages.GuestUserPage import GuestUserPage
            self.parent.show_frame(GuestUserPage)
            # self.show_frame(GuestUserPage)
            Application.current_logged_in_user = username
            # Application._frame.welcome_label.config(text='Welcome Guest User ' + Application.current_logged_in_user)
        elif username in OU_dict and password == OU_dict[username[0]] or username == 'o' and password == 'o':
            from Pages.OrdinaryUserPage import OrdinaryUserPage
            self.parent.show_frame(OrdinaryUserPage)
            Application.current_logged_in_user = username
            # app._frame.welcome_label.config(text='Welcome Ordinary User ' + Application.current_logged_in_user)
        elif username == 's' and password == 's':
            from Pages.SuperUserPage import SuperUserPage
            self.parent.show_frame(SuperUserPage)
            Application.current_logged_in_user = username
            # app._frame.welcome_label.config(text='Welcome Super User ' + Application.current_logged_in_user)
        else:
            messagebox.showerror('Error', 'Invalid login information; try again.')
