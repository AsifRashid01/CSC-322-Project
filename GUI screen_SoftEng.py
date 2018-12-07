# from Tkinter import *                             # Using Tkinter for GUI properties
# import tkMessageBox                               # Importing MessageBox module

#python 3:
from tkinter import *                                                      # Using Tkinter for GUI properties
from tkinter import messagebox                                             # Importing MessageBox module
import sys
import os
import json
# from tkinter import ttk
LARGE_FONT = ("Verdana", 12)
#

class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, GuestUserPage, OrdinaryUserPage, SuperUserPage,
                  Your_Documents_OU, Recent_Documents_OU, Your_Documents_SU, Documents_GU, Taboo_Word_Suggestions_GU,
                  ViewApplications, ViewTabooWords, Apply_GU_to_OU, File_Complaints, CreateGuestUserAccount, Taboo_Word_Suggestions_OU):



            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == LoginPage:
            Tk.wm_title(self, "Login Page")
        elif cont == GuestUserPage:
            Tk.wm_title(self, "Guest User Page")
        elif cont == OrdinaryUserPage:
            Tk.wm_title(self, "Ordinary User Page")
        elif cont == SuperUserPage:
            Tk.wm_title(self, "Super User Page")
        else:
            Tk.wm_title(self, "DSS")

    current_logged_in_user = None # variable to keep track of a currently logged in user

class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='red')

        self.controller = controller

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
        btn = Button(self, text='Check Login', command=self.RegisteredUserLogin)
        # Button to log in as a guest
        btn2 = Button(self, text='Create Guest User Account', command=lambda: self.controller.show_frame(CreateGuestUserAccount))


        btn.pack(padx=5)
        btn2.pack(padx=6)

    def RegisteredUserLogin(self):
        username = self.entry1.get()
        password = self.entry2.get()
        
        try:
            GU_file = open('GU.json', 'r')
            GU_dict = json.load(GU_file)
        except FileNotFoundError:
            GU_file = open('GU.json', 'w') # create GU.json
            json.dump({}, GU_file) # and initialize it as empty dictionary
            GU_dict = {}

        try:
            OU_file = open('OU.json', 'r')
            OU_dict = json.load(OU_file)
        except FileNotFoundError:
            OU_file = open('OU.json', 'w') # create OU.json
            json.dump({}, OU_file) # and initialize it as an empty dictionary
            OU_dict = {}

        if username in GU_dict and password == GU_dict[username] or username == 'g' and password == 'g':
            self.controller.show_frame(GuestUserPage)
            Application.current_logged_in_user = username
        elif username in OU_dict and password == OU_dict[username[0]] or username == 'o' and password == 'o':
            self.controller.show_frame(OrdinaryUserPage)
            Application.current_logged_in_user = username
        elif username == 's' and password == 's':
            self.controller.show_frame(SuperUserPage)
            Application.current_logged_in_user = username
        else:
            messagebox.showerror('Error', 'Invalid login information; try again.')

#        if username == 's' and password == 's':
#            self.controller.show_frame(SuperUserPage)
#        elif username == 'o' and password == 'o':
#            self.controller.show_frame(OrdinaryUserPage)
#        elif  username == 'g' and password == 'g':
#            self.controller.show_frame(GuestUserPage)
#        else:
#            #tkMessageBox.showinfo('Status', 'Invalid Login, Please Try Again')
#            #python 3:
#            messagebox.showerror('Error', 'Invalid Login, Please Try Again')

    def GuestUserLogin(self):
        self.controller.show_frame(GuestUserPage)

class CreateGuestUserAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='red')

        self.controller = controller

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

        CGUA_btn2 = Button(self, text='Cancel', command=lambda: self.controller.show_frame(LoginPage))
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
                f = open('GU.json', 'r+')
                GU_dict = json.load(f)
                if username in GU_dict:
                    messagebox.showerror('Error', 'Username already taken. Try again!')
                else:
                    GU_dict.update({username: password}) # update the dictionary
                    f.seek(0)
                    json.dump(GU_dict, f, sort_keys=True) # update json file
                f.close()
            except FileNotFoundError:
                f = open('GU.json', 'w')
                new_dict = {username: password}
                json.dump(new_dict, f)
                f.close()

class GuestUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='green')

        Label1 = Label(self, text='Welcome Guest User!', font="Times 25 bold")
        Label1.pack(padx=15, pady=5)

        fram = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        # Providing buttons for various GU options:

        but0 = Button(fram, text='Documents', command=lambda: controller.show_frame(Documents_GU))
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fram, text='Send Taboo word suggestions to SU', command=lambda: controller.show_frame(Taboo_Word_Suggestions_GU))
        but1.pack(side=TOP, padx=7, pady=5)

        but2 = Button(fram, text='Apply to be an OU', command=lambda: controller.show_frame(Apply_GU_to_OU))
        but2.pack(side=TOP, padx=7, pady=5)

        fram.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login Page", command=lambda: controller.show_frame(LoginPage))
        button.pack()


class Apply_GU_to_OU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')
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
        cancel_button = Button(self, text="Cancel", command=lambda: controller.show_frame(GuestUserPage))
        cancel_button.pack(side=BOTTOM)

    def submit_application(self):
        formatted_application = {Application.current_logged_in_user: {"First name": self.agu_entry1.get(),
                                                                      "Last name": self.agu_entry2.get(),
                                                                      "Email": self.agu_entry3.get(),
                                                                      "Technical interests": [self.variable.get(), self.variable2.get()],
                                                                      "Other interests": self.agu_entry5.get()}}
        try:
            f = open('Applications.json', 'r+')
            applications = json.load(f)
            f.seek(0)

            if Application.current_logged_in_user in applications:
                messagebox.showerror('Error', 'You have already submitted an application, and it is pending.')
            else:
                applications.update(formatted_application) # update dictionary with new application
                json.dump(applications, f) # update json file with updated dictionary
        except FileNotFoundError:
            f = open('Applications.json', 'w')
            json.dump(formatted_application, f)

class Documents_GU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')
        back_button = Button(self, text="Back to GU Home Page", command=lambda: controller.show_frame(GuestUserPage))
        back_button.pack(side=BOTTOM)
        yd_label = Label(self, text= "Choose a document")
        yd_label.pack(side=TOP)
        # yd_options = os.listdir("/Users/rafey7/Desktop/CSC-322-Project/Document/")
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

        # self.button2['state'] = 'disabled'
        # F = open("/Users/rafey7/Desktop/CSC-322-Project/Document/" + self.Var_get, "r")
        F = open(sys.path[0] + "/Document/" + self.Var_get, "r")
        a = F.read()
        print (a)

        yd_label = Label(self, text= a)
        yd_label.pack(side=TOP)


'''
    def doc_decision(self):

        F = open("/Users/rafey7/Desktop/CSC-322-Project/Document/" + self.Var_get, "r")
        print F.read()

'''




class Taboo_Word_Suggestions_GU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        cancel_button = Button(self, text="Cancel", command=lambda: controller.show_frame(GuestUserPage))
        cancel_button.pack(side=BOTTOM)
        tw_label = Label(self, text="** You are about to send a list of taboo words ** ")
        tw_label.pack(side=TOP)

        tw_label1 = Label(self, text="Enter taboo words (one word per line): ")
        tw_label1.pack(side=TOP)

        self.tw_entry1 = Text(self, bd=5)

        self.tw_entry1.pack(side=TOP)

        button2 = Button(self, text='submit', command=self.Retrieve_Taboo_words)
        button2.pack(side=TOP)



    def Retrieve_Taboo_words(self):
        result = self.tw_entry1.get("1.0", 'end-3c')
        print(result)




class OrdinaryUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        Labe = Label(self, text='Correct Login, Welcome Ordinary User!', font="Times 25 bold")
        Labe.pack(padx=15, pady=5)

        fra = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        # Providing buttons for various OU options:

        but_0 = Button(fra, text='Your Documents', command=lambda: controller.show_frame(Your_Documents_OU))
        but_0.pack(side=TOP, padx=4, pady=5)

        but0 = Button(fra, text='Create new document', command=self.create_new_document_window)
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fra, text='Invite OUs', command=self.invite_ou_window)
        but1.pack(side=TOP, padx=6, pady=5)

        but2 = Button(fra, text='View Invitations', command=self.accept_decline_invites)
        but2.pack(side=TOP, padx=7, pady=5)

        but3 = Button(fra, text='Search other Users', command=self.get_info_ou)
        but3.pack(side=TOP, padx=8, pady=5)

        but4 = Button(fra, text='Process Complaints of OUs')
        but4.pack(side=TOP, padx=9, pady=5)

        but5 = Button(fra, text='File Complaints', command=lambda: controller.show_frame(File_Complaints))
        but5.pack(side=TOP, padx=10, pady=5)

        but6 = Button(fra, text='Suggest Taboo words', command=lambda: controller.show_frame(Taboo_Word_Suggestions_OU))
        but6.pack(side=TOP, padx=9, pady=5)

        Labe1 = Label(fra, text='Recent Documents: ', font="Times 25 bold")
        Labe1.pack(side=TOP, padx=11, pady=5)

        button8 = Button(fra, text='Document 1', command=lambda: controller.show_frame(Recent_Documents_OU))
        button8.pack(side=LEFT, padx=14, pady=5)

        button9 = Button(fra, text='Document 2', command=lambda: controller.show_frame(Recent_Documents_OU))
        button9.pack(side=LEFT, padx=13, pady=5)

        button9 = Button(fra, text='Document 3', command=lambda: controller.show_frame(Recent_Documents_OU))
        button9.pack(side=LEFT, padx=12, pady=5)

        button10 = Button(self, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fra.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login User Page", command=lambda: controller.show_frame(LoginPage))
        button.pack()

    def create_new_document_window(self):
        self.cnd_window = Tk()
        cnd_fram = Frame(self.cnd_window)
        cnd_label = Label(cnd_fram, text= "Enter file name:")
        cnd_label.pack(side = LEFT)
        self.cnd_entry = Entry(cnd_fram, bd = 5)
        self.cnd_entry.pack(side = LEFT)
        cnd_button = Button(cnd_fram, text='Submit', command=self.create_new_document)
        cnd_button.pack(side = LEFT)
        cnd_fram.pack()
        self.cnd_window.mainloop()

    def create_new_document(self):
        new_file_name = self.cnd_entry.get() + ".txt"
        file_names = os.listdir(sys.path[0] + "/Document")
        # file_names = os.listdir("/Users/rafey7/Desktop/CSC-322-Project/Document/")
        if new_file_name in file_names:
            #python 3:
            messagebox.showerror('Error', 'Can\'t create file. File name already exists.')
        else:
            open(sys.path[0] + "/Document/" + new_file_name, "w")

    def invite_ou_window(self):
        iou_window = Tk()
        iou_frame = Frame(iou_window)
        iou_label = Label(iou_frame, text="Who would you like to invite: ")
        iou_label.pack(side=TOP)
        iou_frame.pack()
        options = ["User1", "User2", "User3"]
        iou_button = Button(iou_frame, text='Invite')
        iou_button.pack(side=RIGHT)
        variable = StringVar(iou_window)
        variable.set(options[0])
        w = OptionMenu(iou_window, variable, *options)
        w.pack(side=TOP)
        iou_window.mainloop()

    def accept_decline_invites(self):
        adi_window = Tk()
        adi_frame = Frame(adi_window)
        adi_label = Label(adi_frame, text = "Invitations:")
        adi_label.pack(side=TOP)
        adi_frame.pack()
        options = ["doc1.txt", "doc2.txt", "doc3.txt"]
        variable = StringVar(adi_window)
        variable.set(options[0])
        w = OptionMenu(adi_frame, variable, *options)
        w.pack(side=TOP)
        adi_button0 = Button(adi_frame, text = 'Cancel', command=adi_window.destroy)
        adi_button0.pack(side=LEFT, padx = 6, pady = 4)
        adi_button1 = Button(adi_frame, text = 'Accept')
        adi_button1.pack(side=LEFT, padx = 6, pady =4)
        adi_button2 = Button(adi_frame, text = 'Decline')
        adi_button2.pack(side=LEFT, padx = 6, pady = 4)
        adi_window.mainloop()


    def get_info_ou(self):
        gio_window = Tk()
        gio_window.title("Search for an OU")
        gio_frame = Frame(gio_window)
        gio_label0 = Label(gio_frame, text = "Enter OU's Name:")
        gio_label0.pack(side=TOP)
        self.gio_entry0 = Entry(gio_frame, bd = 5)
        self.gio_entry0.pack(side=TOP)
        gio_label1 = Label(gio_frame, text = "Interests: ")
        gio_label1.pack(side=TOP)
        self.gio_entry1 = Entry(gio_frame, bd =5)
        self.gio_entry1.pack(side=TOP)
        gio_button0 = Button(gio_frame, text = "cancel", command=gio_window.destroy)
        gio_button0.pack(side=LEFT, padx = 6, pady = 4)
        gio_button1 = Button(gio_frame, text = "search", command=self.display_ou_info)
        gio_button1.pack(side=LEFT, padx = 6, pady = 4)
        gio_frame.pack()
        gio_window.mainloop()


    def display_ou_info(self):

        # if self.gio_entry0.get() == "" and self.gio_entry1.get() == "":
        #     print("Invalid entry")

        dou_window = Tk()
        dou_window.title("View OU profiles")
        dou_frame = Frame(dou_window)
        dou_frame.pack()
        dou_label0 = Label(dou_frame, text = "Best matches:")
        dou_label0.pack(side=TOP)

        if self.gio_entry0.get() == "John Doe" and self.gio_entry1.get() == "Interest1":
            lb = Listbox(dou_frame, height=1, bd = 3)
            lb.pack(side=TOP)
            lb.insert(END, "John Doe")
        else:
            users = ["User1", "User2", "User3"]
            variable = StringVar(dou_frame)
            variable.set(users[0])
            w = OptionMenu(dou_frame, variable, *users)
            w.pack(side=TOP)

        dou_button0 = Button(dou_frame, text = "Cancel", command=dou_window.destroy)
        dou_button0.pack(side=LEFT, padx = 6, pady = 4)
        dou_button1 = Button(dou_frame, text = "View profile")
        dou_button1.pack(side=LEFT, padx = 6, pady = 4)
        dou_window.mainloop()


class Your_Documents_OU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        back_button = Button(self, text="Back to OU Home Page", command=lambda: controller.show_frame(OrdinaryUserPage))
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

        button3 = Button(self, text='go back')
        button3.pack(side=TOP)

    def doc_decision_ou(self):
        F = open(sys.path[0] + "/Document/" + self.Var_get, "r")
        a = F.read()
        print (a)
        yd_label = Label(self, text= a)
        yd_label.pack(side=TOP)



class Recent_Documents_OU(Frame):
     def __init__(self, parent, controller):
         Frame.__init__(self, parent, bg='yellow')
         rd_label0 = Label(self, text="What would you like to do?")
         rd_label0.pack(side=TOP)
         rd_options = ["Read", "Edit", "Retrieve older versions", "Change privacy setting", "Lock document", "Unlock document", "Remove collaborator"]
         variable = StringVar(self)
         variable.set(rd_options[0])
         w = OptionMenu(self, variable, *rd_options)
         w.pack(side=TOP)

         button0 = Button(self, text='submit')
         button0.pack(side=TOP)
         button1 = Button(self, text='back', command=lambda: controller.show_frame(OrdinaryUserPage))
         button1.pack(side=TOP)



class File_Complaints(Frame):
    def __init__(self, parent, controller):
            Frame.__init__(self, parent, bg='yellow')
            label0 = Label(self, text = "Select Document:")
            label0.pack(side=TOP)

            # import os
            # path = 'C:/Users/Asif/Desktop/Project test/Document/'
            # fc_options = []
            # for filename in os.listdir(path):
            #     fc_options.append(filename)

            fc_options = os.listdir(sys.path[0] + "/Document/")

            self.variable = StringVar(self)
            self.variable.set(fc_options[0])
            w = OptionMenu(self, self.variable, *fc_options)
            w.pack(side=TOP)
            button1 = Button(self, text = "ok", command=self.Complain_About)
            button1.pack(side=TOP)

    def Complain_About(self):
        T = Text(self, height = 3, width = 30)
        T.pack(side = TOP, pady = 10)
        T.insert(END, "Write complaint here")

        var1 = Checkbutton(self, text = "Notify owner")
        var1.pack(side=TOP)
        button0 = Button(self, text = "Submit")
        button0.pack(side=TOP, pady = 5)


class Taboo_Word_Suggestions_OU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        cancel_button = Button(self, text="Cancel", command=lambda: controller.show_frame(OrdinaryUserPage))
        cancel_button.pack(side=BOTTOM)
        tw_label = Label(self, text="** You are about to send a list of taboo words ** ")
        tw_label.pack(side=TOP)

        tw_label1 = Label(self, text="Enter taboo words (one word per line): ")
        tw_label1.pack(side=TOP)

        self.tw_entry1 = Text(self, bd=5)

        self.tw_entry1.pack(side=TOP)

        button2 = Button(self, text='submit', command=self.Retrieve_Taboo_words)
        button2.pack(side=TOP)


    def Retrieve_Taboo_words(self):
        result = self.tw_entry1.get("1.0", 'end-3c')
        print(result)


class Your_Documents_SU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        back_button = Button(self, text="Back to SU Home Page", command=lambda: controller.show_frame(SuperUserPage))
        back_button.pack(side=BOTTOM)
        yd_label = Label(self, text= "Choose Document")
        yd_label.pack(side=TOP)
        yd_options = ["Doc 1", "Doc 2", "Doc 3"]
        self.variable = StringVar(self)
        self.variable.set(yd_options[0])
        w = OptionMenu(self, self.variable, *yd_options)
        w.pack(side=TOP)
        button1 = Button(self, text='ok', command= self.doc_selection)
        button1.pack(side=TOP)

    def doc_selection(self):
        print(self.variable.get())
        yd_label2 = Label(self, text="What would you like to do?")
        yd_label2.pack(side=TOP)
        yd_options2 = ["Read Doc", "Edit Doc", "Send suggestions (taboo words)", "retrieve older versions",
                       "Invite other OUs", "change privacy settings"]
        variable2 = StringVar(self)
        variable2.set(yd_options2[0])
        w = OptionMenu(self, variable2, *yd_options2)
        w.pack(side=TOP)

        button2 = Button(self, text='submit')
        button2.pack(side=TOP)

        button3 = Button(self, text='go back')
        button3.pack(side=TOP)


class SuperUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        fr = Frame(self)
        rd_Frame = Frame(self)

        Lab = Label(self, text='Correct Login, Welcome Super User!', font="Times 25 bold")
        Lab.pack(padx=15, pady=5)

        Lab0 = Label(fr, text='What would you like to do?', font="Times 16 bold")
        Lab0.pack(padx=15, pady=6)

        # Providing buttons for various SU options:

        button0 = Button(fr, text='Documents')  # Providing buttons for various SU options
        button0.pack(side=TOP, padx=5, pady=5)

        button1 = Button(fr, text='View OU Applications', command=lambda: controller.show_frame(ViewApplications))
        button1.pack(side=TOP, padx=6, pady=5)

        button2 = Button(fr, text='View Complaints')
        button2.pack(side=TOP, padx=7, pady=5)

        button3 = Button(fr, text='View Taboo Words', command=lambda: controller.show_frame(ViewTabooWords))
        button3.pack(side=TOP, padx=8, pady=5)

        button4 = Button(fr, text='Remove OU\'s')
        button4.pack(side=TOP, padx=9, pady=5)

        button5 = Button(fr, text='Search OUs')
        button5.pack(side=TOP, padx=10, pady=5)

        button6 = Button(fr, text='View invitations')
        button6.pack(side=TOP, padx=11, pady=5)

        Lab1 = Label(rd_Frame, text='Recent Documents: ', font="Times 25 bold")
        Lab1.pack(side=TOP, padx=14, pady=5)

        button7 = Button(rd_Frame, text='Document 1')
        button7.pack(side=LEFT, padx=17, pady=5)

        button8 = Button(rd_Frame, text='Document 2')
        button8.pack(side=LEFT, padx=16, pady=5)

        button9 = Button(rd_Frame, text='Document 3')
        button9.pack(side=LEFT, padx=15, pady=5)

        button10 = Button(self, text='Change Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)

        fr.pack(padx=100, pady=19)
        rd_Frame.pack(padx = 101, pady = 19)

        button = Button(self, text="Visit Login User Page", command=lambda: controller.show_frame(LoginPage))
        button.pack()

    def create_new_document_window(self):
        cnd_window = Tk()
        cnd_fram = Frame(cnd_window)
        cnd_label = Label(cnd_fram, text="Enter file name:")
        cnd_label.pack(side=LEFT)
        self.cnd_entry = Entry(cnd_fram, bd=5)
        self.cnd_entry.pack(side=RIGHT)
        cnd_button = Button(cnd_fram, text='Submit', command=self.create_new_document)
        cnd_button.pack(side=RIGHT)
        cnd_fram.pack()
        cnd_window.mainloop()

    def create_new_document(self):
        new_file_name = self.cnd_entry.get() + ".txt"
        #file_names = os.listdir("/Users/rafey7/Desktop/CSC-322-Project/Document/")
        file_names = os.listdir(sys.path[0] + "/Document")
        if new_file_name in file_names:
            print(new_file_name)
        else:
            #open("/Users/rafey7/Desktop/CSC-322-Project/Document/" + new_file_name, "w")
            open(sys.path[0] + "/Document/" + new_file_name, "w")
            self.cnd_window.destroy()

class ViewApplications(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        va_label = Label(self, text= "Choose an application")
        va_label.pack(side=TOP)
        va_apps = ["APP 1", "APP 2", "APP 3"]
        self.va_var = StringVar(self)
        self.va_var.set(va_apps[0])
        va_om = OptionMenu(self, self.va_var, *va_apps)
        va_om.pack(side=TOP)
        va_ok_button = Button(self, text='ok')
        va_ok_button.pack(side=TOP)
        va_cancel_button = Button(self, text='Cancel', command=lambda: controller.show_frame(SuperUserPage))
        va_cancel_button.pack(side=TOP)

class ViewTabooWords(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')
        vtw_label = Label(self, text= "Taboo Words")
        vtw_label.pack(side=TOP)
        vtw_list = ["Fork", "Beach", "Damn"]
        vtw_lb = Listbox(self)
        vtw_lb.pack(side=TOP)
        for item in vtw_list:
            vtw_lb.insert(END, item)
        vtw_add_button = Button(self, text='Add')
        vtw_add_button.pack(side=TOP)
        vtw_remove_button = Button(self, text='Remove')
        vtw_remove_button.pack(side=TOP)
        vtw_cancel_button = Button(self, text='Cancel', command=lambda: controller.show_frame(SuperUserPage))
        vtw_cancel_button.pack(side=TOP)

class ViewApplications(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')
        va_label = Label(self, text= "Choose an application")
        va_label.pack(side=TOP)
        va_apps = ["APP 1", "APP 2", "APP 3"]
        self.va_var = StringVar(self)
        self.va_var.set(va_apps[0])
        va_om = OptionMenu(self, self.va_var, *va_apps)
        va_om.pack(side=TOP)
        va_ok_button = Button(self, text='ok')
        va_ok_button.pack(side=TOP)
        va_cancel_button = Button(self, text='Cancel', command=lambda: controller.show_frame(SuperUserPage))
        va_cancel_button.pack(side=TOP)


class ViewTabooWords(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')
        vtw_label = Label(self, text= "Taboo Words")
        vtw_label.pack(side=TOP)
        vtw_list = ["Fork", "Beach", "Damn"]
        vtw_lb = Listbox(self)
        vtw_lb.pack(side=TOP)
        for item in vtw_list:
            vtw_lb.insert(END, item)
        vtw_add_button = Button(self, text='Add')
        vtw_add_button.pack(side=TOP)
        vtw_remove_button = Button(self, text='Remove')
        vtw_remove_button.pack(side=TOP)
        vtw_cancel_button = Button(self, text='Cancel', command=lambda: controller.show_frame(SuperUserPage))
        vtw_cancel_button.pack(side=TOP)

app = Application()
app.mainloop()
