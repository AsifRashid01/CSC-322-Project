from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from Application import Application
import sys
import os
import json

class WarningPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='grey')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        self.back_button = Button(self, text="Logout", command=lambda: parent.show_frame(LoginPage))
        self.back_button.pack(side=BOTTOM)

        docs_label = Label(self, text= "Your account is disabled until you update the following documents, which were tagged by our taboo words system.", "15")
        docs_label.pack(side=TOP)

        docs_label = Label(self, text= "Choose Document")
        docs_label.pack(side=TOP)

        self.bot = Frame(self) # frame in which 'Save' button will appear if the user requests to edit a doc
        self.bot.pack(side=BOTTOM)

        with open("Databases/User warnings/Taboo warnings.json", "r") as f:
            warning_data = json.load(f)
        
        doc_options = []

        for doc in warning_data[Application.currently_logged_in_user]:
            doc_options.append(key)

        self.variable = StringVar(self)
        if doc_options != []:
            self.variable.set(doc_options[0])
            self.w1 = OptionMenu(self, self.variable, *doc_options, command=self.update_info) # selecting a doc updates the info label
            self.w1.pack(side=TOP)
        else:
            self.variable.set('')
            self.w1 = OptionMenu(self, self.variable, '', command=self.update_info)
            self.w1.pack(side=TOP)

        self.docinfo_label = Label(self, text="Owner:\nVersion:\nMode:\nRead/update count:", justify=LEFT, font = ("Courier", 11))
        self.docinfo_label.pack(pady=9, side=TOP)

        action_label = Label(self, text="What would you like to do?")
        action_label.pack(side=TOP, padx=5, pady=5)

        action_options = ["Read", "Edit"]

        self.variable2 = StringVar(self)
        self.variable2.set("Read")
        self.w2 = OptionMenu(self, self.variable2, *action_options)
        self.w2.pack(side=TOP)

        if doc_options != []:
            self.update_info(doc_options[0])

        self.ok_button = Button(self, text='OK', command = self.doc_decision)
        self.ok_button.pack(side=TOP)

        self.mytext = scrolledtext.ScrolledText(self, font=("Times", 10))
        self.mytext.pack(expand=TRUE, fill=Y)
        self.mytext.configure(state="disabled")

    def doc_decision(self):
        doc_name = self.variable.get()
        action_name = self.variable2.get()

        if doc_name == '':
            return

        if action_name == "Read":
            with open("Document/" + doc_name + ".txt", "r+") as f:
                contents = f.read()
                self.mytext.configure(state="normal")
                self.mytext.delete(1.0,END)
                self.mytext.insert(INSERT, contents)
                self.mytext.configure(state="disabled")

        elif action_name == "Edit":
            print("Edit" + doc_name)


