from tkinter import *
from tkinter import messagebox
import sys
import os

class OrdinaryUserPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        self.welcome_label = Label(self, text='Welcome Ordinary User!', font="Times 25 bold")
        self.welcome_label.pack(padx=15, pady=5)

        fra = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        # Providing buttons for various OU options:

        but_0 = Button(fra, text='Your Documents', command=lambda: parent.show_frame(Your_Documents_OU))
        but_0.pack(side=TOP, padx=4, pady=5)

        but0 = Button(fra, text='Create new document', command=lambda: parent.show_frame(create_new_document))
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fra, text='Invite OUs', command=lambda: parent.show_frame(invite_ou_window))
        but1.pack(side=TOP, padx=6, pady=5)

        but2 = Button(fra, text='View Invitations', command=lambda: parent.show_frame(accept_decline_invites))
        but2.pack(side=TOP, padx=7, pady=5)

        but3 = Button(fra, text='Search other Users', command=lambda: parent.show_frame(get_info_ou))
        but3.pack(side=TOP, padx=8, pady=5)

        but4 = Button(fra, text='Process Complaints of OUs')
        but4.pack(side=TOP, padx=9, pady=5)

        but5 = Button(fra, text='File Complaints', command=lambda: parent.show_frame(File_Complaints))
        but5.pack(side=TOP, padx=10, pady=5)

        # from Pages.GuestUserPage import Taboo_Word_Suggestions
        but6 = Button(fra, text='Suggest Taboo words', command=lambda: parent.show_frame(Taboo_Word_Suggestions_OU))
        but6.pack(side=TOP, padx=9, pady=5)

        Labe1 = Label(fra, text='Recent Documents: ', font="Times 25 bold")
        Labe1.pack(side=TOP, padx=11, pady=5)

        button8 = Button(fra, text='Document 1', command=lambda: parent.show_frame(Recent_Documents_OU))
        button8.pack(side=LEFT, padx=14, pady=5)

        button9 = Button(fra, text='Document 2', command=lambda: parent.show_frame(Recent_Documents_OU))
        button9.pack(side=LEFT, padx=13, pady=5)

        button9 = Button(fra, text='Document 3', command=lambda: parent.show_frame(Recent_Documents_OU))
        button9.pack(side=LEFT, padx=12, pady=5)

        button10 = Button(self, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fra.pack(padx=100, pady=19)

        from Pages.LoginPage import LoginPage
        button = Button(self, text="Visit Login User Page", command=lambda: parent.show_frame(LoginPage))
        button.pack()

class Your_Documents_OU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        back_button.pack(side=BOTTOM)
        yd_label = Label(self, text= "Choose Document")
        yd_label.pack(side=TOP)
        #yd_options = ["Doc 1", "Doc 2", "Doc 3"]
        yd_options = os.listdir(sys.path[0] + "/Document/")
        self.variable = StringVar(self)
        self.variable.set(yd_options[0])
        w = OptionMenu(self, self.variable, *yd_options)
        w.pack(side=TOP)
        self.button1 = Button(self, text='ok', command= self.doc_selection)
        self.button1.pack(side=TOP)

    def doc_selection(self):
        #print(self.variable.get())
        self.button1['state'] = 'disabled'
        self.Var_get = self.variable.get()
        yd_label2 = Label(self, text="What would you like to do?")
        yd_label2.pack(side=TOP)
        yd_options2 = ["Read Doc", "Edit Doc", "Send suggestions (taboo words)", "retrieve older versions",
                       "Invite other OUs", "change privacy settings"]
        variable2 = StringVar(self)
        variable2.set(yd_options2[0])
        w = OptionMenu(self, variable2, *yd_options2)
        w.pack(side=TOP)

        button2 = Button(self, text='submit', command = self.doc_decision_ou)
        button2.pack(side=TOP)

    def doc_decision_ou(self):
        F = open(sys.path[0] + "/Document/" + self.Var_get, "r")
        a = F.read()
        print (a)
        yd_label = Label(self, text= a)
        yd_label.pack(side=TOP)

class Recent_Documents_OU(Frame):
     def __init__(self, parent):
         Frame.__init__(self, parent, bg='yellow')
         Frame.pack(self, side="top", fill="both", expand=True)
         Frame.grid_rowconfigure(self, 0, weight=1)
         Frame.grid_columnconfigure(self, 0, weight=1)

         self.parent = parent

         rd_label0 = Label(self, text="What would you like to do?")
         rd_label0.pack(side=TOP)
         rd_options = ["Read", "Edit", "Retrieve older versions", "Change privacy setting", "Lock document", "Unlock document", "Remove collaborator"]
         variable = StringVar(self)
         variable.set(rd_options[0])
         w = OptionMenu(self, variable, *rd_options)
         w.pack(side=TOP)

         button0 = Button(self, text='submit')
         button0.pack(side=TOP)
         button1 = Button(self, text='back', command=lambda: parent.show_frame(OrdinaryUserPage))
         button1.pack(side=TOP)

class File_Complaints(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        label0 = Label(self, text = "Select Document:")
        label0.pack(side=TOP)

        fc_options = os.listdir(sys.path[0] + "/Document/")

        self.variable = StringVar(self)
        self.variable.set(fc_options[0])

        w = OptionMenu(self, self.variable, *fc_options)
        w.pack(side=TOP)

        button1 = Button(self, text = "ok", command=self.Complain_About)
        button1.pack(side=TOP)

        cnd_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        cnd_back_button.pack(side=BOTTOM)

    def Complain_About(self):
        T = Text(self, height = 3, width = 30)
        T.pack(side = TOP, pady = 10)
        T.insert(END, "Write complaint here")

        var1 = Checkbutton(self, text = "Notify owner")
        var1.pack(side=TOP)
        button0 = Button(self, text = "Submit")
        button0.pack(side=TOP, pady = 5)

class create_new_document(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        cnd_label = Label(self, text= "Enter file name:")
        cnd_label.pack(side = TOP)
        self.cnd_entry = Entry(self, bd = 5)
        self.cnd_entry.pack(side = TOP)
        cnd_button = Button(self, text='Submit')
        cnd_button.pack(side = TOP)
        cnd_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        cnd_back_button.pack(side=TOP)

    def create_new_document(self):
        new_file_name = self.cnd_entry.get() + ".txt"
        file_names = os.listdir(sys.path[0] + "/Document")
        if new_file_name in file_names:
            #python 3:
            messagebox.showerror('Error', 'Can\'t create file. File name already exists.')
        else:
            open(sys.path[0] + "/Document/" + new_file_name, "w")

class invite_ou_window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        iou_label = Label(self, text="Who would you like to invite: ")
        iou_label.pack(side=TOP)

        options = ["User1", "User2", "User3"]
        variable = StringVar(self)
        variable.set(options[0])

        w = OptionMenu(self, variable, *options)
        w.pack(side=TOP)

        iou_button = Button(self, text='Invite')
        iou_button.pack(side=TOP)

        iow_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        iow_back_button.pack(side=TOP)

class accept_decline_invites(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        adi_label = Label(self, text = "Invitations:")
        adi_label.pack(side=TOP)
        options = ["doc1.txt", "doc2.txt", "doc3.txt"]
        variable = StringVar(self)
        variable.set(options[0])

        w = OptionMenu(self, variable, *options)
        w.pack(side=TOP)

        adi_button0 = Button(self, text = 'Cancel', command=lambda: parent.show_frame(OrdinaryUserPage))
        adi_button0.pack(side=TOP, padx = 6, pady = 4)

        adi_button1 = Button(self, text = 'Accept')
        adi_button1.pack(side=TOP, padx = 6, pady =4)

        adi_button2 = Button(self, text = 'Decline')
        adi_button2.pack(side=TOP, padx = 6, pady = 4)

class get_info_ou(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        gio_label0 = Label(self, text = "Enter OU's Name:")
        gio_label0.pack(side=TOP)

        self.gio_entry0 = Entry(self, bd = 5)
        self.gio_entry0.pack(side=TOP)

        gio_label1 = Label(self, text = "Interests: ")
        gio_label1.pack(side=TOP)

        self.gio_entry1 = Entry(self, bd =5)
        self.gio_entry1.pack(side=TOP)

        gio_button0 = Button(self, text = "cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        gio_button0.pack(side=TOP, padx = 6, pady = 4)

        gio_button1 = Button(self, text = "search", command=lambda: parent.show_frame(display_ou_info))
        gio_button1.pack(side=TOP, padx = 6, pady = 4)

class display_ou_info(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        dou_label0 = Label(self, text = "Best matches:")
        dou_label0.pack(side=TOP)

        # if self.gio_entry0.get() == "John Doe" and self.gio_entry1.get() == "Interest1":
        #     lb = Listbox(dou_frame, height=1, bd = 3)
        #     lb.pack(side=TOP)
        #     lb.insert(END, "John Doe")
        # else:
        #     users = ["User1", "User2", "User3"]
        #     variable = StringVar(self)
        #     variable.set(users[0])
        #     w = OptionMenu(self, variable, *users)
        #     w.pack(side=TOP)

        dou_button0 = Button(self, text = "Cancel", command=lambda: parent.show_frame(OrdinaryUserPage) )
        dou_button0.pack(side=TOP, padx = 6, pady = 4)

        dou_button1 = Button(self, text = "View profile")
        dou_button1.pack(side=TOP, padx = 6, pady = 4)

from Pages.GuestUserPage import Taboo_Word_Suggestions
class Taboo_Word_Suggestions_OU(Taboo_Word_Suggestions):
    def __init__(self, parent):
        Taboo_Word_Suggestions.__init__(self, parent)
        cancel_button2 = Button(self, text="Go back", command=lambda: parent.show_frame(OrdinaryUserPage))
        cancel_button2.pack(side=BOTTOM)
        print("1", self, parent)
