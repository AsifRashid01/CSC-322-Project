from tkinter import *
from tkinter import messagebox
import sys
import os
import json

class GuestUserPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='green')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        self.welcome_label = Label(self, text='Welcome Guest User', font="Times 25 bold")
        self.welcome_label.pack(padx=15, pady=5)

        fram = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        # Providing buttons for various GU options:

        but0 = Button(fram, text='Documents', command=lambda: parent.show_frame(Documents_GU))
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fram, text='Send Taboo word suggestions to SU', command=lambda: parent.show_frame(Taboo_Word_Suggestions))
        but1.pack(side=TOP, padx=7, pady=5)

        but2 = Button(fram, text='Apply to be an OU', command=lambda: parent.show_frame(Apply_GU_to_OU))
        but2.pack(side=TOP, padx=7, pady=5)

        fram.pack(padx=100, pady=19)

        from Pages.LoginPage import LoginPage
        button = Button(self, text="Visit Login Page", command=lambda: parent.show_frame(LoginPage))
        button.pack()

class Apply_GU_to_OU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        agu_label1 = Label(self, text="Enter first name: ")
        agu_label1.pack(side=TOP)

        self.agu_entry1 = Entry(self, bd=5)
        self.agu_entry1.pack(side=TOP)

        agu_label2 = Label(self, text="Enter last name: ")
        agu_label2.pack(side=TOP)

        self.agu_entry2 = Entry(self, bd=5)
        self.agu_entry2.pack(side=TOP)

        agu_label3 = Label(self, text="Enter email: ")
        agu_label3.pack(side=TOP)

        self.agu_entry3 = Entry(self, bd=5)
        self.agu_entry3.pack(side=TOP)

        agu_label4 = Label(self, text="Technical interests:")
        agu_label4.pack(side=TOP)

        agu_options = ["Software Design", "Design Reporting", "Application Development", "Information Systems"]
        self.variable = StringVar(self)
        self.variable.set(agu_options[0])

        self.variable2 = StringVar(self)
        self.variable2.set(agu_options[0])

        w = OptionMenu(self, self.variable, *agu_options)
        w.pack(side=TOP)

        w2 = OptionMenu(self, self.variable2, *agu_options)
        w2.pack(side=TOP)

        agu_label5 = Label(self, text="Other technical interest(s): ")
        agu_label5.pack(side=TOP)

        self.agu_entry5 = Entry(self, bd=5)
        self.agu_entry5.pack(side=TOP)

        agu_button = Button(self, text='Submit', command=self.submit_application)
        agu_button.pack(side=TOP)

        # from Pages.GuestUserPage import GuestUserPage
        cancel_button = Button(self, text="Cancel", command=lambda: parent.show_frame(GuestUserPage))
        cancel_button.pack(side=BOTTOM)

    def submit_application(self):
        from Application import Application
        formatted_application = {Application.current_logged_in_user: {"First name": self.agu_entry1.get(),
                                                                      "Last name": self.agu_entry2.get(),
                                                                      "Email": self.agu_entry3.get(),
                                                                      "Technical interests": [self.variable.get(), self.variable2.get()],
                                                                      "Other interests": self.agu_entry5.get()}}
        try:
            f = open('Databases/Applications/Applications.json', 'r+')
            applications = json.load(f)
            f.seek(0)

            if Application.current_logged_in_user in applications:
                messagebox.showerror('Error', 'You have already submitted an application, and it is pending.')
            else:
                applications.update(formatted_application) # update dictionary with new application
                json.dump(applications, f) # update json file with updated dictionary
        except FileNotFoundError:
            f = open('Databases/Applications/Applications.json', 'w')
            json.dump(formatted_application, f)

class Documents_GU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        # from GuestUserPage import GuestUserPage
        back_button = Button(self, text="Back to GU Home Page", command=lambda: parent.show_frame(GuestUserPage))
        back_button.pack(side=BOTTOM)

        yd_label = Label(self, text= "Choose a document")
        yd_label.pack(side=TOP)

        yd_options = os.listdir(sys.path[0] + "/Document")
        self.variable = StringVar(self)
        self.variable.set(yd_options[0])

        w = OptionMenu(self, self.variable, *yd_options)
        w.pack(side=TOP)

        self.button1 = Button(self, text='OK', command=self.doc_selection)
        self.button1.pack(side=TOP)

    def doc_selection(self):
        self.button1['state'] = 'disabled'
        self.Var_get = self.variable.get()

        yd_label2 = Label(self, text="What would you like to do?")
        yd_label2.pack(side=TOP)

        yd_options2 = ["Read Doc", "Retrieve older version of Doc", "File complaint about Doc"]
        variable2 = StringVar(self)
        variable2.set(yd_options2[0])

        w = OptionMenu(self, variable2, *yd_options2)
        w.pack(side=TOP)

        self.button2 = Button(self, text='submit', command= self.doc_decision)
        self.button2.pack(side=TOP)

    def doc_decision(self):
        F = open(sys.path[0] + "/Document/" + self.Var_get, "r")
        a = F.read()
        print (a)

        yd_label = Label(self, text= a)
        yd_label.pack(side=TOP)

class Taboo_Word_Suggestions(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent
        print(self, parent)
        print(type(self) == Taboo_Word_Suggestions)
        if(type(self) == Taboo_Word_Suggestions):
            cancel_button = Button(self, text="Go back", command=lambda: parent.show_frame(GuestUserPage))
            cancel_button.pack(side=BOTTOM)

        tw_label = Label(self, text="** You are about to send a list of taboo words ** ")
        tw_label.pack(side=TOP)

        tw_label1 = Label(self, text="Enter taboo words separated by spaces or lines: ")
        tw_label1.pack(side=TOP)

        self.tw_entry1 = Text(self, bd=5)

        self.tw_entry1.pack(side=TOP)

        button2 = Button(self, text='submit', command=self.submit_taboo_suggestions)
        button2.pack(side=TOP)

    def submit_taboo_suggestions(self):
        try:
            f = open('Databases/TabooWordSuggestions/TabooWordSuggestions.json', 'r+')
            list_of_suggested_taboos = json.load(f)

        except FileNotFoundError:
            f = open('Databases/TabooWordSuggestions/TabooWordSuggestions.json', 'w+')
            json.dump({}, f)
            list_of_suggested_taboos = {}

        submission_list = self.tw_entry1.get('1.0', END).split()

        for w in submission_list:
            if w not in list_of_suggested_taboos:
                list_of_suggested_taboos[w] = 1
            else:
                list_of_suggested_taboos[w] += 1

        f.seek(0)
        json.dump(list_of_suggested_taboos, f)
