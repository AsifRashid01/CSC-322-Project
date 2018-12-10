from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from Application import Application
import sys
import os
import json

class OrdinaryUserPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        # create JSON files if they have not yet been created
        # maybe do this at the start of the Application instead
        if not os.path.isfile("Databases/Documents/Unshared documents.json"):
            f = open("Databases/Documents/Unshared documents.json", "w")
            json.dump({}, f)
            f.close()
        if not os.path.isfile("Databases/Documents/Shared documents.json"):
            f = open("Databases/Documents/Shared documents.json", "w")
            json.dump({}, f)
            f.close()

        self.welcome_label = Label(self, text='Welcome Ordinary User!', font="Times 25 bold")
        self.welcome_label.pack(padx=15, pady=5)

        fra = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        # Providing buttons for various OU options:

        but_0 = Button(fra, text='Your Documents', command=lambda: parent.show_frame(Your_Documents_OU))
        but_0.pack(side=TOP, padx=4, pady=5)

        # but0 = Button(fra, text='Create new document', command=lambda: parent.show_frame(create_new_document))
        but0 = Button(fra, text='Create new document', command=lambda: parent.show_frame(create_new_document_OU))
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

        back_button = Button(self, text="Back to OU Home Page", command=lambda: parent.show_frame(OrdinaryUserPage))
        back_button.pack(side=BOTTOM)
        docs_label = Label(self, text= "Choose Document")
        docs_label.pack(side=TOP)

       # doc_options = [x for x in os.listdir("Document") if x[-4:] == ".txt"] # list of files in Document folder that end in .txt.
        doc_options = []
        f1 = open("Databases/Documents/Unshared documents.json", "r")
        f2 = open("Databases/Documents/Shared documents.json", "r")
        unshared_docs = json.load(f1)
        shared_docs = json.load(f2)
        f1.close(); f2.close()

        # doc_options will contain the names of only those documents belonging to Application.current_logged_in_user
        for key, value in unshared_docs.items():
            if value[0] == Application.current_logged_in_user:
                doc_options.append(key)
        for key, value in shared_docs.items():
            if value[0] == Application.current_logged_in_user:
                doc_options.append(key)

        # Remember that entries in Unshared docs have format {Doc_name: [Owner, Version, Mode]},
        # whereas entries in Shared docs have format {Doc_name: [Owner, Version, Mode, Collaborators_list, Lock_status]}.
        # Lock_status is either 'Unlocked' or 'Locked by <user>' where <user> is the user who has currently locked it.

        self.docinfo_label = Label(self, text="Owner:\nVersion:\nMode:", justify=LEFT, font = ("Courier", 11))

        self.variable = StringVar(self)
        if doc_options != []: # if doc_options is not empty
            self.variable.set(doc_options[0]) # set default option (i.e., to the first doc name in doc_options)
            self.w1 = OptionMenu(self, self.variable, *doc_options, command=self.update_info_label)
            self.w1.pack(side=TOP)
        else:
            self.variable.set('')
            self.w1 = OptionMenu(self, self.variable, '', command=self.update_info_label)
            self.w1.pack(side=TOP)

        self.docinfo_label.pack(pady=9, side=TOP)

        action_label = Label(self, text="What would you like to do?")
        action_label.pack(side=TOP, padx=5, pady=5)
        action_options = ["Read", "Lock", "Edit", "Unlock", "Change mode", "Retrieve previous versions", "View collaborators"]

        self.variable2 = StringVar(self)
        self.variable2.set(action_options[0])
        self.w2 = OptionMenu(self, self.variable2, *action_options)
        self.w2.pack(side=TOP)

        self.top = Frame(self) # frame in which a third optionmenu may later appear (right below the second optionmenu)
        self.top.pack(side=TOP)

        # initialize info label and action menu
        if doc_options != []:
            self.update_info_label(doc_options[0])

        self.ok_button = Button(self, text='OK', command = self.doc_decision)
        self.ok_button.pack(side=TOP)

        self.mytext = scrolledtext.ScrolledText(self, font=("Times", 10))
        self.mytext.pack(expand=TRUE, fill=Y)
        self.mytext.configure(state="disabled") # initially, the text box is disabled

    def document_info(self, document_name):
        # returns document info or False if the info is not found
        f = open("Databases/Documents/Unshared documents.json", "r")
        g = open("Databases/Documents/Shared documents.json", "r")
        unshared_docs = json.load(f)
        shared_docs = json.load(g)

        if document_name in unshared_docs:
            return unshared_docs[document_name]
        elif document_name in shared_docs: 
            return shared_docs[document_name]
        else: # document could not be found
            return False

        f.close()

    def update_info_label(self, event):
        # The command called when you select a document from the document OptionMenu: updates info label as well as the action OptionMenu;
        # depending on whether the selected document is Shared or not, the action OptionMenu differs.

        doc_info = self.document_info(event)
        if doc_info != False:
            action_menu = self.w2["menu"]

            if doc_info[2] == 'Shared':
                self.docinfo_label['text'] = ('Owner: {}\nVersion: {}\nMode: Shared\n' + \
                                              ' Collaborators: {}\n Lock status: {}').format(doc_info[0], doc_info[1], doc_info[3], doc_info[4])

                action_menu.delete(0, "end")
                new_actions = ["Read", "Lock", "Edit", "Unlock",
                               "Change mode to open", "Change mode to private", "Change mode to restricted", "Change mode to shared",
                               "Retrieve previous versions", "Invite collaborator", "Remove collaborator"]
                for act in new_actions:
                    action_menu.add_command(label=act, command=lambda value=act: self.variable2.set(value))
            else:
                self.docinfo_label['text'] = 'Owner: {}\nVersion: {}\nMode: {}'.format(doc_info[0], doc_info[1], doc_info[2])

                action_menu.delete(0, "end")
                new_actions = ["Read", "Edit",
                               "Change mode to open", "Change mode to private", "Change mode to restricted", "Change mode to shared",
                               "Retrieve previous versions"]
                for act in new_actions:
                    action_menu.add_command(label=act, command=lambda value=act: self.variable2.set(value))

    def doc_decision(self):
        # the command when you click 'OK': performs the selected action on the selected document
        doc_name = self.variable.get()
        action_name = self.variable2.get()

        if doc_name == '':
            # if there are no documents, the selected document is empty, so just return
            return

        if action_name == "Read":
            f = open("Document/" + doc_name + ".txt", "r")
            contents = f.read()
            self.mytext.configure(state="normal") # reenable text box to update its contents
            self.mytext.delete(1.0,END) # delete old contents
            self.mytext.insert(INSERT, contents) # insert new contents
            self.mytext.configure(state="disabled") # disable text box again
            f.close()
        elif action_name == "Lock":
            g = open("Databases/Documents/Shared documents.json", "r+")
            shared_docs = json.load(g) # {doc_name: [owner name, version, mode, collaborator_list, lock_status]}
            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[4] == "Unlocked":
                    shared_docs[doc_name][4] = "Locked by " + Application.current_logged_in_user # update lock_status

                    g.seek(0)
                    json.dump(shared_docs, g) # dump shared_docs

                    # update info label
                    self.docinfo_label['text'] = ('Owner: {}\nVersion: {}\nMode: Shared\n' + \
                                              ' Collaborators: {}\n Lock status: {}').format(doc_info[0], doc_info[1], doc_info[3], doc_info[4])

                else:
                    messagebox.showerror("Hmmm", "Already locked.")
            g.close()
     #   elif action_name == "Edit":
            # move to a new frame
        elif action_name == "Unlock":
            g = open("Databases/Documents/Shared documents.json", "r")
            shared_docs = json.load(g) # {doc_name: [owner name, version, mode, collaborator_list, lock_status]}
            g.close()

            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[4] != "Unlocked":
                    shared_docs[doc_name][4] = "Unlocked" # update lock_status

                    with open("Databases/Documents/Shared documents.json", "w") as g:
                        json.dump(shared_docs, g) # dump shared_docs

                    # update info label
                    self.docinfo_label['text'] = ('Owner: {}\nVersion: {}\nMode: Shared\n' + \
                                              ' Collaborators: {}\n Lock status: {}').format(doc_info[0], doc_info[1], doc_info[3], doc_info[4])

                else:
                    messagebox.showerror("Hmmm", "Already unlocked.")
        elif action_name == "Change mode to open":
            self.change_mode(doc_name, "Open")
        elif action_name == "Change mode to private":
            self.change_mode(doc_name, "Private")
        elif action_name == "Change mode to restricted":
            self.change_mode(doc_name, "Restricted")
        elif action_name == "Change mode to shared":
            self.change_mode(doc_name, "Shared")
#        elif action_name == "Change mode to private":
#            modes = ["Open", "Restricted", "Shared", "Private"]
#            self.var = StringVar(self)
#            active_mode = self.document_info(doc_name)[2]
#            self.var.set(active_mode) # default value
#            
#            modes = OptionMenu(self, self.var, *modes)
#            modes.pack(in_=self.top, side=LEFT)

#            self.ok_button.configure(text = "Change", command=self.save_mode(self.var.get()))


     #   elif action_name == "Retrieve previous versions":
            
     #   elif action_name == "Invite collaborator":
            
#        elif action_name == "Remove collaborator":

    def change_mode(self, doc_name, mode):
        f1 = open("Databases/Documents/Shared documents.json", "r")
        f2 = open("Databases/Documents/Unshared documents.json", "r")
        shared_docs = json.load(f1)
        unshared_docs = json.load(f2)
        f1.close(); f2.close()

        if mode == "Open" or mode == "Restricted" or mode == "Private":
            if doc_name in shared_docs: # in this case, we must move the entry to Unshared documents
                with open("Databases/Documents/Shared documents.json", "w") as f:
                    temp = shared_docs[doc_name] # save the entry before deleting
                    temp[2] = mode # change the entry's mode
                    del shared_docs[doc_name] # remove entry from dictionary

                    json.dump(shared_docs, f)

                with open("Databases/Documents/Unshared documents.json", "r+") as f:
                     e = {doc_name: [temp[0], temp[1], temp[2]]}
                     unshared_docs.update(e)

                     json.dump(unshared_docs, f)
            elif doc_name in unshared_docs: # no need to move the entry; just update the entry's mode
                with open("Databases/Documents/Unshared documents.json", "w") as h:
                    unshared_docs[doc_name][2] = mode

                    json.dump(unshared_docs, h)
            # finally, update frame:
            self.update_info_label(doc_name)
        elif mode == "Shared":
            # only needs updating (and moving) if it is in unshared_docs
            if doc_name in unshared_docs:
                with open("Databases/Documents/Unshared documents.json", "w") as f:
                    temp = unshared_docs[doc_name] # save the entry before deleting
                    temp[2] = "Shared"
                    del unshared_docs[doc_name] # remove entry from dictionary

                    json.dump(unshared_docs, f)

                with open("Databases/Documents/Shared documents.json", "r+") as f:
                     e = {doc_name: [temp[0], temp[1], temp[2], [], "Unlocked"]}
                     shared_docs.update(e)

                     json.dump(shared_docs, f)

                # finally, update frame:
                self.update_info_label(doc_name)

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

# class create_new_document(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent, bg='yellow')
#         Frame.pack(self, side="top", fill="both", expand=True)
#         Frame.grid_rowconfigure(self, 0, weight=1)
#         Frame.grid_columnconfigure(self, 0, weight=1)
#
#         self.parent = parent
#
#         cnd_label = Label(self, text= "Enter file name:")
#         cnd_label.pack(side = TOP)
#         self.cnd_entry = Entry(self, bd = 5)
#         self.cnd_entry.pack(side = TOP)
#         cnd_button = Button(self, text='Submit')
#         cnd_button.pack(side = TOP)
#         cnd_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
#         cnd_back_button.pack(side=TOP)
#
#     def create_new_document(self):
#         new_file_name = self.cnd_entry.get() + ".txt"
#         file_names = os.listdir(sys.path[0] + "/Document")
#         if new_file_name in file_names:
#             #python 3:
#             messagebox.showerror('Error', 'Can\'t create file. File name already exists.')
#         else:
#             open(sys.path[0] + "/Document/" + new_file_name, "w")

class create_new_document_OU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        back_button = Button(self, text="Back to Home Page", command=lambda: parent.show_frame(OrdinaryUserPage))
        back_button.pack(side=BOTTOM)

        cnd_label = Label(self, text= "Enter file name:")
        cnd_label.pack(side = LEFT)

        self.cnd_entry = Entry(self, bd = 5)
        self.cnd_entry.pack(side = LEFT)
        cnd_button = Button(self, text='Create', command=self.create_doc)
        cnd_button.pack(side = LEFT)

    def create_doc(self):
        new_file_name = self.cnd_entry.get()
        file_names = os.listdir("Document")

        if new_file_name == '':
            messagebox.showerror("Error", "File name can't be empty")
        elif (new_file_name + ".txt") not in file_names:
            open("Document/" + new_file_name + ".txt", "w") # save document.txt

            # We also have to save the information of the newly created (private) document in 'Unshared documents.json':

            f = open("Databases/Documents/Unshared documents.json", "r+")
            d = json.load(f)
            d.update({new_file_name: [Application.current_logged_in_user, 1, "Private"]}) # doc_name: [doc_owner, version #, doc_mode]
            f.seek(0)
            json.dump(d, f, sort_keys=True)
            f.close()

            # show success message:
            messagebox.showinfo("Success", new_file_name + " created.")
        else:
            messagebox.showerror('Error', 'Can\'t create file. File name already exists.')

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
