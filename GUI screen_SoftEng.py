# from Tkinter import *                             # Using Tkinter for GUI properties
# import tkMessageBox                               # Importing MessageBox module

#python 3:
from tkinter import *                                                      # Using Tkinter for GUI properties
from tkinter import messagebox                                             # Importing MessageBox module

# from tkinter import ttk
LARGE_FONT = ("Verdana", 12)


class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, GuestUserPage, OrdinaryUserPage, SuperUserPage,
                  Your_Documents_OU, Your_Documents_SU, Documents_GU, Taboo_Word_Suggestions_GU):
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
        btn2 = Button(self, text='Login as Guest User', command=self.GuestUserLogin)


        btn.pack(padx=5)
        btn2.pack(padx=6)

    def RegisteredUserLogin(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username == 's' and password == 's':
            self.controller.show_frame(SuperUserPage)
        elif username == 'o' and password == 'o':
            self.controller.show_frame(OrdinaryUserPage)
        else:
            #tkMessageBox.showinfo('Status', 'Invalid Login, Please Try Again')
            #python 3:
            messagebox.showerror('Error', 'Invalid Login, Please Try Again')

    def GuestUserLogin(self):
        self.controller.show_frame(GuestUserPage)


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

        but2 = Button(fram, text='Apply to be an OU', command=self.Apply_GU_to_OU)
        but2.pack(side=TOP, padx=7, pady=5)

        fram.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login Page", command=lambda: controller.show_frame(LoginPage))
        button.pack()

    def Apply_GU_to_OU(self):
        agu_window = Tk()
        agu_fram = Frame(agu_window)
        agu_label1 = Label(agu_fram, text="Enter first name: ")
        agu_label1.pack(side=TOP)
        self.agu_entry1 = Entry(agu_fram, bd=5)
        self.agu_entry1.pack(side=TOP)
        agu_label2 = Label(agu_fram, text="Enter last name: ")
        agu_label2.pack(side=TOP)
        self.agu_entry2 = Entry(agu_fram, bd=5)
        self.agu_entry2.pack(side=TOP)
        agu_label3 = Label(agu_fram, text="Enter email: ")
        agu_label3.pack(side=TOP)
        self.agu_entry3 = Entry(agu_fram, bd=5)
        self.agu_entry3.pack(side=TOP)
        agu_label4 = Label(agu_fram, text="Technical Interest Field: ")
        agu_label4.pack(side=TOP)
        agu_options = ["Software Design", "Design Reporting", "Application Development", "Information Systems"]
        self.variable = StringVar(agu_fram)
        self.variable.set(agu_options[0])
        w = OptionMenu(agu_fram, self.variable, *agu_options)
        w.pack(side=TOP)
        agu_button = Button(agu_fram, text='Submit')
        agu_button.pack(side=BOTTOM)
        agu_fram.pack()
        agu_window.mainloop()


class Documents_GU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        back_button = Button(self, text="Back to GU Home Page", command=lambda: controller.show_frame(GuestUserPage))
        back_button.pack(side=BOTTOM)
        yd_label = Label(self, text= "Choose a document")
        yd_label.pack(side=TOP)
        yd_options = ["Doc 1", "Doc 2", "Doc 3"]
        self.variable = StringVar(self)
        self.variable.set(yd_options[0])
        w = OptionMenu(self, self.variable, *yd_options)
        w.pack(side=TOP)
        button1 = Button(self, text='OK', command=self.doc_selection)
        button1.pack(side=TOP)

    def doc_selection(self):
        print(self.variable.get())
        yd_label2 = Label(self, text="What would you like to do?")
        yd_label2.pack(side=TOP)
        yd_options2 = ["Read Doc", "Retrieve older version of Doc", "File complaint about Doc"]
        variable2 = StringVar(self)
        variable2.set(yd_options2[0])
        w = OptionMenu(self, variable2, *yd_options2)
        w.pack(side=TOP)

        button2 = Button(self, text='submit')
        button2.pack(side=TOP)


class Taboo_Word_Suggestions_GU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        cancel_button = Button(self, text="Cancel", command=lambda: controller.show_frame(GuestUserPage))
        cancel_button.pack(side=BOTTOM)
        tw_label = Label(self, text="** You are about to send a list of taboo words ** ")
        tw_label.pack(side=TOP)

        tw_label1 = Label(self, text="Enter taboo words: ")
        tw_label1.pack(side=TOP)
        self.tw_entry1 = Entry(bd=5)
        self.tw_entry1.pack(side=TOP)

        button2 = Button(self, text='submit')
        button2.pack(side=TOP)


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

        but2 = Button(fra, text='Accept or Deny invitations')
        but2.pack(side=TOP, padx=7, pady=5)

        but3 = Button(fra, text='Get info about other OUs')
        but3.pack(side=TOP, padx=8, pady=5)

        but4 = Button(fra, text='Process Complaints of OUs')
        but4.pack(side=TOP, padx=9, pady=5)

        Labe1 = Label(fra, text='Recent Documents: ', font="Times 25 bold")
        Labe1.pack(side=TOP, padx=11, pady=5)

        button8 = Button(fra, text='Document 1')
        button8.pack(side=LEFT, padx=14, pady=5)

        button9 = Button(fra, text='Document 2')
        button9.pack(side=LEFT, padx=13, pady=5)

        button9 = Button(fra, text='Document 3')
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
        cnd_window.mainloop()

    def create_new_document(self):
        new_file_name = self.cnd_entry.get() + ".txt"
        import os
        file_names = os.listdir("/Users/rafey7/Desktop/CSC-322-Project/Document/")
        if new_file_name in file_names:
            #python 3:
            messagebox.showerror('Error', 'Can\'t create file. File name already exists.')
        else:
            open("/Users/rafey7/Desktop/CSC-322-Project/Document/" + new_file_name, "w")

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


class Your_Documents_OU(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        back_button = Button(self, text="Back to OU Home Page", command=lambda: controller.show_frame(OrdinaryUserPage))
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

        Lab = Label(self, text='Correct Login, Welcome Super User!', font="Times 25 bold")
        Lab.pack(padx=15, pady=5)

        Lab0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Lab0.pack(padx=15, pady=6)

        # Providing buttons for various SU options:

        button_0 = Button(fr, text='Your Documents', command=lambda: controller.show_frame(Your_Documents_SU))
        button_0.pack(side=TOP, padx=4, pady=5)

        button1 = Button(fr, text='See taboo words')
        button1.pack(side=TOP, padx=5, pady=5)

        button2 = Button(fr, text='Unlock Locked documents')
        button2.pack(side=TOP, padx=6, pady=5)

        button3 = Button(fr, text='Update Membership')
        button3.pack(side=TOP, padx=7, pady=5)

        button4 = Button(fr, text='Process Complaints of OUs')
        button4.pack(side=TOP, padx=8, pady=5)

        button5 = Button(fr, text='Create new document', command=self.create_new_document_window)
        button5.pack(side=TOP, padx=9, pady=5)

        button6 = Button(fr, text='Invite OUs')
        button6.pack(side=TOP, padx=10, pady=5)

        button7 = Button(fr, text='Accept/Deny invitations')
        button7.pack(side=TOP, padx=11, pady=5)

        button8 = Button(fr, text='Get info about other OUs')
        button8.pack(side=TOP, padx=12, pady=5)

        Lab1 = Label(fr, text='Recent Documents: ', font="Times 25 bold")
        Lab1.pack(side=TOP, padx=14, pady=5)

        button8 = Button(fr, text='Document 1')
        button8.pack(side=LEFT, padx=17, pady=5)

        button9 = Button(fr, text='Document 2')
        button9.pack(side=LEFT, padx=16, pady=5)

        button9 = Button(fr, text='Document 3')
        button9.pack(side=LEFT, padx=15, pady=5)

        button10 = Button(self, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fr.pack(padx=100, pady=19)

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
        import os
        #file_names = os.listdir("/Users/rafey7/Desktop/CSC-322-Project/Document/")
        file_names = os.listdir("C:/Users/saddi/Desktop/CSC-322-Project/Document")
        if new_file_name in file_names:
            print(new_file_name)
        else:
            #open("/Users/rafey7/Desktop/CSC-322-Project/Document/" + new_file_name, "w")
            open("C:/Users/saddi/Desktop/CSC-322-Project/Document/" + new_file_name, "w")
            self.cnd_window.destroy()


app = Application()
app.mainloop()
