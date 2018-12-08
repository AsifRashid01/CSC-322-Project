from tkinter import *
from tkinter import messagebox
import json

class CreateGuestUserAccount(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='red')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        CGUA_Label0 = Label(self, text='Create Guest User Account Page', font="Times 16 bold")
        CGUA_Label0.pack(padx=15, pady=5)

        CGUA_Label1 = Label(self, text='Username:')
        CGUA_Label1.pack(padx=15, pady=5)

        self.CGUA_entry1 = Entry(self, bd=5)
        self.CGUA_entry1.pack(padx=15, pady=5)

        CGUA_Label2 = Label(self, text='Password:')
        CGUA_Label2.pack(padx=15, pady=6)

        self.CGUA_entry2 = Entry(self, bd=5)
        self.CGUA_entry2.pack(padx=15, pady=7)

        CGUA_btn1 = Button(self, text='Create Account', command=self.checkUniqueUsername)
        CGUA_btn1.pack(padx=5)

        from Pages.LoginPage import LoginPage
        CGUA_btn2 = Button(self, text='Cancel', command=lambda: parent.show_frame(LoginPage))
        CGUA_btn2.pack(padx=6)

    def checkUniqueUsername(self):
        username = self.CGUA_entry1.get()
        password = self.CGUA_entry2.get()

        if username == '' or username[0] == ' ':
            messagebox.showerror('Error', 'Usernames must begin with a non-whitespace character.')
        elif password == '':
            messagebox.showerror('Error', 'Enter a password with at least one character.')
        else:
            try:
                f = open('Databases/Users/GU.json', 'r+')
                GU_dict = json.load(f)
                if username in GU_dict:
                    messagebox.showerror('Error', 'Username already taken. Try again!')
                else:
                    GU_dict.update({username: password}) # update the dictionary
                    f.seek(0)
                    json.dump(GU_dict, f, sort_keys=True) # update json file
                f.close()
            except FileNotFoundError:
                f = open('Databases/Users/GU.json', 'w')
                new_dict = {username: password}
                json.dump(new_dict, f)
                f.close()

        from Pages.LoginPage import LoginPage
        self.parent.show_frame(LoginPage)
