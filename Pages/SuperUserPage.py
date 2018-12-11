from tkinter import *
from tkinter import messagebox
import json

class SuperUserPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        fr = Frame(self)
        rd_Frame = Frame(self)

        self.welcome_label = Label(self, text='Correct Login, Welcome Super User!', font="Times 25 bold")
        self.welcome_label.pack(padx=15, pady=5)

        Lab0 = Label(fr, text='What would you like to do?', font="Times 16 bold")
        Lab0.pack(padx=15, pady=6)

        # Providing buttons for various SU options:

        button0 = Button(fr, text='Documents')  # Providing buttons for various SU options
        button0.pack(side=TOP, padx=5, pady=5)

        button1 = Button(fr, text='View OU Applications', command=lambda: parent.show_frame(ViewApplications))
        button1.pack(side=TOP, padx=6, pady=5)

        button2 = Button(fr, text='View Complaints', command=lambda: parent.show_frame(ViewComplaints))
        button2.pack(side=TOP, padx=7, pady=5)

        button3 = Button(fr, text='View Taboo Words/Taboo Word Suggestions', command=lambda: parent.show_frame(ViewTabooWords))
        button3.pack(side=TOP, padx=8, pady=5)

        button4 = Button(fr, text='Remove OU\'s', command=lambda: parent.show_frame(RemoveOU))
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

        from Pages.LoginPage import LoginPage
        button = Button(self, text="Visit Login User Page", command=lambda: parent.show_frame(LoginPage))
        button.pack()

class ViewComplaints(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        vc_label = Label(self, text= "Choose a complaint")
        vc_label.pack(side=TOP)
        vc_complaints = ["Complaint 1", "Complaint 2", "Complaint 3"]
        self.vc_var = StringVar(self)
        self.vc_var.set(vc_complaints[0])
        vc_om = OptionMenu(self, self.vc_var, *vc_complaints)
        vc_om.pack(side=TOP)
        vc_ok_button = Button(self, text='ok')
        vc_ok_button.pack(side=TOP)

        vc_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(SuperUserPage))
        vc_cancel_button.pack(side=TOP)

class ViewApplications(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        va_label = Label(self, text= "Choose an application")
        va_label.pack(side=TOP)

        va_apps = self.retrieveApplications() # retrieve all applications as a dictionary
        va_apps_keys = self.retrieveApplications().keys() # get keys from the dictionary
        va_apps_keys_list = list(va_apps_keys) # turns set of keys into a list of keys

        self.va_var = StringVar(self)
        if (len(va_apps) != 0):
            self.va_var.set(va_apps_keys_list[0])
            va_om = OptionMenu(self, self.va_var, *va_apps_keys_list)
            va_om.pack(side=TOP)
            va_ok_button = Button(self, text='ok', command=lambda: self.va_set_and_go(va_apps) )
            va_ok_button.pack(side=TOP)

        va_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(SuperUserPage))
        va_cancel_button.pack(side=TOP)

    def va_set_and_go(self, all_apps):
        va_var_selected = self.va_var.get()
        an_app = all_apps[va_var_selected]
        self.parent.show_frame(ViewAnApplication, va_var_selected, an_app)

    def retrieveApplications(self):
        try:
            f = open('Databases/Applications/Applications.json', 'r+')
            applications = json.load(f)
            f.close()
            return applications
        except FileNotFoundError:
            messagebox.showerror('Error', 'This file does not exist!')

class ViewAnApplication(Frame):
    def __init__(self, parent, *args):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        v_an_app = Text(self)
        v_an_app.insert(INSERT,"Username: " + args[0])
        v_an_app.insert(END, '\n')

        for key in args[1]:
            if(type(args[1][key]) is list):
                v_an_app.insert(INSERT, key + ": " + ", ".join(args[1][key]))
                v_an_app.insert(END, '\n')
            else:
                v_an_app.insert(INSERT, key + ": " + args[1][key])
                v_an_app.insert(END, '\n')

        v_an_app.config(state=DISABLED)
        v_an_app.pack(side=TOP)

        v_an_app_promote_button = Button(self, text='Accept', command=lambda: self.accept_an_app(args[0], args[1]))
        v_an_app_promote_button.pack(side=TOP)

        v_an_app_reject_button = Button(self, text='Reject', command=lambda: self.reject_an_app(args[0]))
        v_an_app_reject_button.pack(side=TOP)

        v_an_app_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(ViewApplications))
        v_an_app_cancel_button.pack(side=TOP)

    def reject_an_app(self, *args):

        if (messagebox.askyesno('Confirm Rejection', 'Are you sure you want to reject this application?')):
            self.remove_an_app(args[0])

    def remove_an_app(self, *args):
        try:
            f = open('Databases/Applications/Applications.json', 'r+')
            apps = json.load(f)
            apps.pop(args[0])
            f.seek(0)
            f.truncate()
            json.dump(apps, f, sort_keys=True)
            f.close()
            self.parent.show_frame(ViewApplications)
        except:
            messagebox.showerror('Error', 'Something went wrong!')

    def accept_an_app(self, *args):
        try:
            if (messagebox.askyesno('Confirm Acceptance', 'Are you sure you want to accept this application?')):
                f = open('Databases/Users/GU.json', 'r+') #retrieve all username:passwords from GU.json file

                gu = json.load(f) # turns the json data into a python dictionary
                gu_pass = gu[args[0]] # retrieves the applicants password
                args[1]["password"] = gu_pass #insert the applicants password to dictionarys

                gu.pop(args[0]) # removes the GU's username:password from the gu dictionary
                f.seek(0)
                f.truncate() #deletes the contents of the file
                json.dump(gu, f, sort_keys=True) # inserts the new dictonary into the file as json data
                f.close()

                f2 = open('Databases/Users/OU.json', 'r+') #retrieve all OU information from OU.json file

                ous = json.load(f2) #turns the json data into a python dictionary
                ous.update({args[0]:args[1]}) #adds applicant dictionary username:{information} to OU dictionary

                f2.seek(0)
                f2.truncate()
                json.dump(ous, f2, sort_keys=True)
                f2.close()
                self.remove_an_app(args[0])
        except:
            messagebox.showerror('Error', 'Something went wrong!')

class ViewTabooWords(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        vtw_label = Label(self, text= "Taboo Words")
        vtw_label.pack(side=TOP)

        vtw_list = self.retrieve_taboo_words()
        vtw_lb = Listbox(self)
        vtw_lb.pack(side=TOP)

        for item in vtw_list:
            vtw_lb.insert(END, item)

        vtw_add_button = Button(self, text='Add')
        vtw_add_button.pack(side=TOP)

        vtw_remove_button = Button(self, text='Remove')
        vtw_remove_button.pack(side=TOP)

        vtw_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(SuperUserPage))
        vtw_cancel_button.pack(side=TOP)

        vtw_vst_button = Button(self, text='View Suggested Taboo Words', command=lambda: parent.show_frame(ViewSuggestedTabooWords)) #change later
        vtw_vst_button.pack(side=TOP)

    def retrieve_taboo_words(self):
        try:
            f = open('Databases/TabooWords/TabooWords.json', 'r+')
            taboo_words = json.load(f)
            f.close()
            return taboo_words
        except FileNotFoundError:
            f = open('Databases/TabooWords/TabooWords.json', 'w')
            json.dump([], f)
            f.close()
            messagebox.showerror('Error', 'This file does not exist!')

class ViewSuggestedTabooWords(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        vtw_label = Label(self, text= "Taboo Words")
        vtw_label.pack(side=TOP)

        vtw_list = self.retrieve_taboo_word_suggestions()
        self.vtw_lb = Listbox(self)
        self.vtw_lb.pack(side=TOP)
        for item in vtw_list:
            self.vtw_lb.insert(END, item)

        vtw_add_button = Button(self, text='Add to Taboo Words list', command = self.add_taboo_word)
        vtw_add_button.pack(side=TOP)

        vtw_remove_button = Button(self, text='Remove')
        vtw_remove_button.pack(side=TOP)

        vtw_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(ViewTabooWords))
        vtw_cancel_button.pack(side=TOP)

    def retrieve_taboo_word_suggestions(self):
        f = open('Databases/TabooWordSuggestions/TabooWordSuggestions.json', 'r+')
        tws_dict = json.load(f)
        f.close()
        return list(tws_dict.keys())

    def add_taboo_word(self):
        try:
            print( self.vtw_lb.get(self.vtw_lb.curselection()) )
        except TclError:
            messagebox.showerror('Error', 'Please select a word!')

    def remove_suggested_taboo_word(self):
        pass

class RemoveOU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        rou_label = Label(self, text= "Choose an OU")
        rou_label.pack(side=TOP)
        rou_OUS = ["OU 1", "OU 2", "OU 3"]
        self.rou_var = StringVar(self)
        self.rou_var.set(rou_OUS[0])
        vc_om = OptionMenu(self, self.rou_var, *rou_OUS)
        vc_om.pack(side=TOP)
        vc_ok_button = Button(self, text='remove')
        vc_ok_button.pack(side=TOP)

        rou_cancel_button = Button(self, text='Cancel', command=lambda: parent.show_frame(SuperUserPage))
        rou_cancel_button.pack(side=TOP)

class Your_Documents_SU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        back_button = Button(self, text="Back to SU Home Page", command=lambda: parent.show_frame(SuperUserPage))
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
