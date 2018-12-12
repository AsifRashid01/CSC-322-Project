from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from Application import Application
from EditDistance import Edit
import re
import datetime
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

        q_label = Label(self, text='What would you like to do?', font="Times 16 bold")
        q_label.pack(padx=15, pady=5)

        # Providing buttons for various OU options:

        own_docs_button = Button(fra, text='Your documents', command=lambda: parent.show_frame(Your_Documents_OU))
        own_docs_button.pack(side=TOP, padx=4, pady=5)

        collab_docs_button = Button(fra, text='Documents you\'re collaborating on', command=lambda: parent.show_frame(Collab_Documents_OU))
        collab_docs_button.pack(side=TOP, padx=4, pady=5)

        other_docs_button = Button(fra, text='Other documents you may view (open/restricted)', command=lambda: parent.show_frame(Other_Documents))
        other_docs_button.pack(side=TOP, padx=4, pady=5)

        create_doc_button = Button(fra, text='Create new document', command=lambda: parent.show_frame(create_new_document_OU))
        create_doc_button.pack(side=TOP, padx=5, pady=5)

        view_invites_button = Button(fra, text='View invitations', command=lambda: parent.show_frame(accept_decline_invites))
        view_invites_button.pack(side=TOP, padx=7, pady=5)

        search_users_button = Button(fra, text='Search for other users', command=lambda: parent.show_frame(get_info_ou))
        search_users_button.pack(side=TOP, padx=8, pady=5)

        proc_button = Button(fra, text='Process complaints about OUs')
        proc_button.pack(side=TOP, padx=9, pady=5)

        complain_button = Button(fra, text='File complaints', command=lambda: parent.show_frame(File_Complaints))
        complain_button.pack(side=TOP, padx=10, pady=5)

        view_complaints_button = Button(fra, text='View complaints', command=lambda: parent.show_frame(View_Complaints))
        view_complaints_button.pack(side=TOP, padx=10, pady=5)

        # from Pages.GuestUserPage import Taboo_Word_Suggestions
        suggest_taboo_button = Button(fra, text='Suggest taboo words', command=lambda: parent.show_frame(Taboo_Word_Suggestions_OU))
        suggest_taboo_button.pack(side=TOP, padx=9, pady=5)

        recent_docs_label = Label(fra, text='Recent documents: ', font="Times 25 bold")
        recent_docs_label.pack(side=TOP, padx=11, pady=5)

        doc1_button = Button(fra, text='Document 1', command=lambda: parent.show_frame(Recent_Documents_OU))
        doc1_button.pack(side=LEFT, padx=14, pady=5)

        doc2_button = Button(fra, text='Document 2', command=lambda: parent.show_frame(Recent_Documents_OU))
        doc2_button.pack(side=LEFT, padx=13, pady=5)

        doc3_button = Button(fra, text='Document 3', command=lambda: parent.show_frame(Recent_Documents_OU))
        doc3_button.pack(side=LEFT, padx=12, pady=5)

        pic_button = Button(self, text='Add Profile Picture')
        pic_button.pack(anchor='nw', padx=5, pady=0)
        pic_button.config(height='6', width='6')

        fra.pack(padx=100, pady=19)

        from Pages.LoginPage import LoginPage
        button = Button(self, text="Visit Login User Page", command=lambda: parent.show_frame(LoginPage))
        button.pack()

class Other_Documents(Frame):
    # (1) This frame shows documents that the OU does not own but that are still visible to them, i.e., other users' open/restricted documents.
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='turquoise')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        self.back_button = Button(self, text="Back to OU Home Page", command=lambda: parent.show_frame(OrdinaryUserPage))
        self.back_button.pack(side=BOTTOM)

        docs_label = Label(self, text= "Choose a document")
        docs_label.pack(side=TOP)

        self.bot = Frame(self) # frame in which 'Save' button will appear if the user requests to edit a doc
        self.bot.pack(side=BOTTOM)

        with open("Databases/Documents/Unshared documents.json", "r") as f:
            unshared_docs = json.load(f) # unshared documents <=> all documents not in Shared mode
        
        doc_options = []

        for key, value in unshared_docs.items():
            owner = value[0]
            mode = value[2]
            if owner != Application.current_logged_in_user and (mode == "Open" or mode == "Restricted"):
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

        # initially update frame elements to pertain to first selected document
        if doc_options != []:
            self.update_info(doc_options[0])

        self.ok_button = Button(self, text='OK', command = self.doc_decision)
        self.ok_button.pack(side=TOP)

        self.mytext = scrolledtext.ScrolledText(self, font=("Times", 10))
        self.mytext.pack(expand=TRUE, fill=Y)
        self.mytext.configure(state="disabled") # initially, the text box is disabled

    def update_info(self, event):
        # The command called when you select a document from the document OptionMenu: updates info label as well as
        # action OptionMenu to what is appropriate for the selected document.
        with open("Databases/Documents/Unshared documents.json", "r") as f:
            unshared_docs = json.load(f)

        if event in unshared_docs: # make sure chosen document is still in unshared docs
            entry = unshared_docs[event]
            action_menu = self.w2["menu"] # get current action menu

            # change info and actions appropriately:
            if entry[2] == "Open":
                self.docinfo_label['text'] = 'Owner: {}\nVersion: {}\nMode: {}\n Read/update count: {}'.format(entry[0], entry[1], entry[2], entry[3])
                action_menu.delete(0, "end")
                action_menu.add_command(label="Read", command=lambda: self.variable2.set("Read"))
            elif entry[2] == "Restricted":
                self.docinfo_label['text'] = 'Owner: {}\nVersion: {}\nMode: {}\n Read/update count: {}'.format(entry[0], entry[1], entry[2], entry[3])
                action_menu.delete(0, "end")
                action_menu.add_command(label="Read", command=lambda: self.variable2.set("Read"))
                action_menu.add_command(label="Edit", command=lambda: self.variable2.set("Edit"))

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

            # increment read/update count
            with open("Databases/Documents/Unshared documents.json", "r+") as f:
                unshared_docs = json.load(f)
                if doc_name in unshared_docs:
                    unshared_docs[doc_name][3] += 1
        elif action_name == "Edit":

            # increment version number as well as read/update count
            with open("Databases/Documents/Unshared documents.json", "r+") as f:
                unshared_docs = json.load(f)
                if doc_name in unshared_docs:
                    unshared_docs[doc_name][1] += 1
                    unshared_docs[doc_name][3] += 1

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

        self.bot = Frame(self) # frame in which 'Save' button would appear
        self.bot.pack(side=BOTTOM)
        self.save_button = Button(self.bot, text="Save changes")

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

        # Entries in Unshared docs have format {Doc_name: [Owner, Version, Mode, Read-update_count]},
        # whereas entries in Shared docs have the format
        # {Doc_name: [Owner, Version, Mode, Collaborator_list, Lock_status, {Versions: [Updator, Time_updated]}]}.
        # Lock_status is either 'Unlocked' or 'Locked by <user>' where <user> is the user who has currently locked it.

        self.docinfo_label = Label(self, text="Owner:\nVersion:\nMode\nRead/update count:", justify=LEFT, font=("Courier", 11))

        self.variable = StringVar(self)
        if doc_options != []: # if doc_options is not empty
            self.variable.set(doc_options[0]) # set default option (i.e., to the first doc name in doc_options)
            # selecting a doc updates the info label
            self.w1 = OptionMenu(self, self.variable, *doc_options, command=lambda x=self.variable:self.update_info_label(x))
            self.w1.pack(side=TOP)
        else:
            self.variable.set('')
            self.w1 = OptionMenu(self, self.variable, '', command=lambda x=self.variable:self.update_info_label(x))
            self.w1.pack(side=TOP)

        self.docinfo_label.pack(pady=9, side=TOP)

        action_label = Label(self, text="What would you like to do?")
        action_label.pack(side=TOP, padx=5, pady=5)
        action_options = ["Read", "Lock", "Edit", "Unlock", "Change mode", "Retrieve previous version"]

        self.variable2 = StringVar(self)
        self.variable2.set(action_options[0])
        self.w2 = OptionMenu(self, self.variable2, *action_options)
        self.w2.pack(side=TOP)

        self.top = Frame(self) # frame in which a third optionmenu may later appear (right below the second optionmenu)
        self.top.pack(side=LEFT)

        # update info label and action menu for the first time
        if doc_options != []:
            self.update_info_label(doc_options[0])

        self.ok_button = Button(self, text='OK', command = self.doc_decision)
        self.ok_button.pack(side=TOP)

        keyword_label = Label(self, text="Specify a keyword:")
        keyword_label.pack(side=TOP)
        self.keyword_entry = Entry(self) # frame in which additional actions may appear (search, invite/remove collaborators)
        self.keyword_entry.pack(side=TOP)

        collaborator_label = Label(self, text="Specify a collaborator:")
        collaborator_label.pack(side=TOP)
        self.collaborator_entry = Entry(self)
        self.collaborator_entry.pack(side=TOP)

        hist_label = Label(self, text="Specify a version number:")
        hist_label.pack(side=TOP)
        self.hist_entry = Entry(self)
        self.hist_entry.pack(side=TOP)

        self.mytext = scrolledtext.ScrolledText(self, font=("Times", 10))
        self.mytext.pack(expand=TRUE, fill=Y)
        self.mytext.configure(state="disabled") # initially, the text box is disabled

    def document_info(self, document_name):
        # returns document info or False if the info is not found
        with open("Databases/Documents/Unshared documents.json", "r") as f, open("Databases/Documents/Shared documents.json", "r") as g:
            unshared_docs = json.load(f)
            shared_docs = json.load(g)

        if document_name in unshared_docs:
            return unshared_docs[document_name]
        elif document_name in shared_docs: 
            return shared_docs[document_name]
        else: # document could not be found
            return False

    def update_info_label(self, event):
        # The command called when you select a document from the document OptionMenu: updates info label as well as
        # other parts of the frame showing the available actions: depending on the selected document, those actions differ.

        doc_info = self.document_info(event)
        if doc_info != False:
            action_menu = self.w2["menu"]

            if doc_info[2] == 'Shared':
                collaborator_list = doc_info[4]
                if len(collaborator_list) <= 4:
                    formatted_collaborator_list = '  ' + ', '.join(collaborator_list)
                else: # collaborator list has more than 5 collaborators; break it into lines of 4
                    remainder = len(collaborator_list) % 4
                    formatted_collaborator_list = '  ' + '\n  '.join([ ', '.join(x) for x in zip(collaborator_list[0::4], collaborator_list[1::4],
                                                                                                 collaborator_list[2::4], collaborator_list[3::4]) ]) +\
                                                  ',\n  ' + ', '.join(collaborator_list[-remainder:])


                update_info = ''
                version = str(doc_info[1])
                # if update info exists for the version number
                if doc_info[6] != {} and (version in doc_info[6]):
                    update_info = doc_info[6][version][0] + " at " + doc_info[6][version][1]

                self.docinfo_label['text'] = ('Owner: {}\nVersion: {}\nMode: Shared\nRead/update count: {}\n').format(doc_info[0], doc_info[1], doc_info[3]) + \
                                             ('Collaborators:\n{}\nLock status: {}\n').format(formatted_collaborator_list, doc_info[5]) + \
                                             ('Last updated by: {}').format(update_info)
    
                action_menu.delete(0, "end")
                new_actions = ["Read", "Find specified keyword", "Lock", "Edit", "Unlock",
                               "Change mode to open", "Change mode to private", "Change mode to restricted", "Change mode to shared",
                               "Retrieve previous version", "Invite specified user to collaborate", "Remove specified collaborator"]
                for act in new_actions:
                    action_menu.add_command(label=act, command=lambda value=act: self.variable2.set(value))
            else:
                self.docinfo_label['text'] = 'Owner: {}\nVersion: {}\nMode: {}\nRead/update count: {}'.format(\
                                             doc_info[0], doc_info[1], doc_info[2], doc_info[3])

                action_menu.delete(0, "end")
                new_actions = ["Read", "Find specified keyword", "Edit", "Change mode to open", "Change mode to private",
                               "Change mode to restricted", "Change mode to shared", "Retrieve previous version"]
                for act in new_actions:
                    action_menu.add_command(label=act, command=lambda value=act: self.variable2.set(value))

    def doc_decision(self):
        # the command when you click 'OK': performs the selected action on the selected document

        # First, if the user does not Save changes after requesting to edit and makes another request,
        # the save button disappears and the textbox gets disabled.
        self.mytext.configure(state="disabled")
        self.save_button.pack_forget()
        self.bot.pack_forget()

        doc_name = self.variable.get()
        action_name = self.variable2.get()

        if doc_name == '':
            # if there are no documents, the selected document is empty, so just return
            return

        if action_name == "Read":
            with open("Document/" + doc_name + ".txt", "r") as f:
                contents = f.read()
                self.mytext.configure(state="normal") # reenable text box to update its contents
                self.mytext.delete(1.0,END) # delete old contents
                self.mytext.insert(INSERT, contents) # insert new contents
                self.mytext.configure(state="disabled") # disable text box again

            # increment view count and display it
            self.increment_views(doc_name)
            self.update_info_label(doc_name)

        elif action_name == "Lock": 
            g = open("Databases/Documents/Shared documents.json", "r+")
            shared_docs = json.load(g)
            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[5] == "Unlocked":
                    shared_docs[doc_name][5] = "Locked by " + Application.current_logged_in_user # update lock_status

                    g.seek(0)
                    json.dump(shared_docs, g) # dump shared_docs
                    g.close()

                    # update info label:
                    self.update_info_label(doc_name)
                else:
                    messagebox.showerror("Hmmm", "Already locked.")
        elif action_name == "Edit":
            # populate textbox with contents first
            with open("Document/" + doc_name + ".txt", "r") as f:
                contents = f.read()
                self.mytext.configure(state="normal") # reenable text box for updating
                self.mytext.delete(1.0, END)
                self.mytext.insert(INSERT, contents)

            info = self.document_info(doc_name)

            # before allowing the user to update a Shared doc, check that the user has locked the document first:
            if info != False:
                if info[2] == "Shared" and info[5] != "Locked by " + Application.current_logged_in_user:
                    messagebox.showerror("Error", "You must lock a shared document before updating.")
                else:
                    self.mytext.configure(state="normal")
                    self.bot.pack() # display bottom frame
                    self.save_button['command'] = lambda f=doc_name: self.save_doc(f) # activate button
                    self.save_button.pack() # display 'Save' button

        elif action_name == "Unlock":
            with open("Databases/Documents/Shared documents.json", "r") as g:
                shared_docs = json.load(g) # {doc_names: [owner, version, mode, collaborator_list, lock_status, {versions: [updator, updatetime]}]}

            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[5] != "Unlocked":
                    shared_docs[doc_name][5] = "Unlocked" # update lock_status

                    with open("Databases/Documents/Shared documents.json", "w") as g:
                        json.dump(shared_docs, g) # dump shared_docs

                    # update info label:
                    self.update_info_label(doc_name)

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

        elif action_name == "Retrieve previous version":
            doc_name = self.variable.get()
            old_version = self.hist_entry.get()

            if doc_name == '' or old_version == '':
                return
###########
            history_folder = os.listdir("History files")
            history_files = [m for m in history_folder if re.match(doc_name + "_" + "[0-9]+" + ".h", m)]

            with open("Databases/Documents/Shared documents.json", "r") as f, open("Databases/Documents/Unshared documents.json") as g:
                shared_docs = json.load(f)
                unshared_docs = json.load(g)

            if doc_name in shared_docs:
                current_version = shared_docs[doc_name][1]
            elif doc_name in unshared_docs:
                current_version = unshared_docs[doc_name][1]

            editdistance = Edit()

            try:
               while current_version != old_version:
                   editdistance.restore_file(list_of_ops, list_of_lines)
                    
            except:
                messagebox.showerror("Error", "Something went wrong")

        elif action_name == "Find specified keyword":
            keyword = self.keyword_entry.get()
            if keyword != '':
                # read (populate textbox)
                with open("Document/" + doc_name + ".txt", "r") as f:
                    contents = f.read()
                    self.mytext.configure(state="normal") # reenable text box to update its contents
                    self.mytext.delete(1.0, END) # delete old contents
                    self.mytext.insert(INSERT, contents) # insert new contents
                    self.mytext.configure(state="disabled") # disable text box again

                # highlight
                self.highlight(keyword)
            
        elif action_name == "Invite specified user to collaborate":
            # initialize (pending) invitations JSON file if it doesn't yet exist:
            if not os.path.isfile("Databases/Invitations/Pending invitations.json"):
                with open("Databases/Invitations/Pending invitations.json", "w") as f:
                    json.dump({}, f)

            name = self.collaborator_entry.get()

            if name == Application.current_logged_in_user:
                messagebox.showerror("Error", "You can't invite yourself.")
                return

            if name != '':
            # save the "pending" invitation
                with open("Databases/Invitations/Pending invitations.json", "r+") as f:
                    shared_docs = json.load(f) # {Usernames: [Documents_invited_to]}
                    if name in shared_docs:
                        if doc_name not in shared_docs[name]:
                            shared_docs[name].append(doc_name)
                        else:
                            messagebox.showerror("Error", "You've already invited this user to the document (the invitation is pending).")
                            return
                    else:
                        shared_docs.update({name: [doc_name]}) # insert new entry

                    f.seek(0)
                    json.dump(shared_docs, f)

                messagebox.showinfo("Success", "Invitation sent")
            
        elif action_name == "Remove specified collaborator":
            if not os.path.isfile("Databases/Invitations/Pending invitations.json"):
                with open("Databases/Invitations/Pending invitations.json", "w") as f:
                    json.dump({}, f)

            name = self.collaborator_entry.get()

            if name != '':
                with open("Databases/Documents/Shared documents.json", "r+") as f:
                    data = json.load(f)
                    if name in data[doc_name][4]:
                        data[doc_name][4].remove(name)

                        f.seek(0)
                        f.truncate()
                        json.dump(data, f)

                        messagebox.showinfo("Success", "Collaborator " + name + " removed from document " + doc_name + ".")
                    else:
                        messagebox.showerror("Error", name + " is not a collaborator for " + doc_name + ".")

            self.update_info_label(doc_name)

    def change_mode(self, doc_name, mode):
        f1 = open("Databases/Documents/Shared documents.json", "r")
        f2 = open("Databases/Documents/Unshared documents.json", "r")
        shared_docs = json.load(f1); unshared_docs = json.load(f2)
        f1.close(); f2.close()

        if mode == "Open" or mode == "Restricted" or mode == "Private":
            if doc_name in shared_docs: # in this case, we must move the entry to Unshared documents
                with open("Databases/Documents/Shared documents.json", "w") as f:
                    entry = shared_docs[doc_name] # save the entry before deleting
                    entry[2] = mode # change the entry's mode
                    del shared_docs[doc_name]
                    json.dump(shared_docs, f)

                with open("Databases/Documents/Unshared documents.json", "r+") as f:
                     e = {doc_name: [entry[0], entry[1], entry[2], entry[3]]} # save Owner, Version, Mode and Read/update count
                     unshared_docs.update(e)

                     json.dump(unshared_docs, f)
            elif doc_name in unshared_docs: # no need to move the entry; just update the entry's mode
                with open("Databases/Documents/Unshared documents.json", "w") as h:
                    unshared_docs[doc_name][2] = mode

                    json.dump(unshared_docs, h)
            # finally, update the frame:
            self.update_info_label(doc_name)
        elif mode == "Shared":
            # only needs updating (and moving) if it is in unshared_docs
            if doc_name in unshared_docs:
                with open("Databases/Documents/Unshared documents.json", "w") as f:
                    temp = unshared_docs[doc_name] # save the entry before deleting
                    temp[2] = "Shared"
                    del unshared_docs[doc_name] # delete
                    json.dump(unshared_docs, f)

                with open("Databases/Documents/Shared documents.json", "r+") as f:
                     e = {doc_name: [temp[0], temp[1], temp[2], temp[3], [], "Unlocked", {}]}
                     shared_docs.update(e)

                     json.dump(shared_docs, f)
                # finally, update the frame:
                self.update_info_label(doc_name)

    def highlight(self, keyword):
        # highlight:
        pos = '1.0'
        while True:
            index = self.mytext.search(keyword, pos, END)
            if not index:
                break
            pos = '{}+{}c'.format(index, len(keyword))
            self.mytext.tag_config('tag', background='yellow')
            self.mytext.tag_add('tag', index, pos)

    def increment_views(self, doc_name): # used for reading
        with open("Databases/Documents/Shared documents.json", "r+") as f:
            shared_docs = json.load(f)
            if doc_name in shared_docs:
                shared_docs[doc_name][3] += 1
            f.seek(0)
            json.dump(shared_docs, f)

    def save_doc(self, doc_name):
        # save old contents for history file generation:
        with open("Document/" + doc_name + ".txt", "r") as f:
            s2 = f.read()

        # get and save new contents
        s1 = self.mytext.get("1.0", "end-1c")
        with open("Document/" + doc_name + ".txt", "w") as f:
            f.write(s1)

        with open("Databases/Documents/Shared documents.json", "r+") as f:
            shared_docs = json.load(f)
        with open("Databases/Documents/Unshared documents.json", "r+") as g:
            unshared_docs = json.load(g)

        if doc_name in shared_docs:
            with open("Databases/Documents/Shared documents.json", "r+") as f:
                shared_docs[doc_name][3] += 1 # increment read/edit count
                shared_docs[doc_name][1] += 1 # increment version #

                current_version = shared_docs[doc_name][1]
                # save updator's info for current version
                shared_docs[doc_name][6].update({current_version: [Application.current_logged_in_user, datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S")]})

                json.dump(shared_docs, f)

            # generate a history command file to restore to prior version
            s1 = s1.split('\n')
            s2 = s2.split('\n')
            editdistance = Edit()
            list_of_ops = editdistance.list_of_edit_operations(s1, s2)

            with open("History files/" + doc_name + "_" + str(current_version-1) + ".h", "w") as f:
                f.write('\n'.join(list_of_ops))

        elif doc_name in unshared_docs:
            # in this case, we just have to increment the version and read/edit count:
            with open("Databases/Documents/Unshared documents.json", "r+") as f:
                shared_docs[doc_name][3] += 1 # increment read/edit count
                shared_docs[doc_name][1] += 1 # increment version #
                json.dump(shared_docs, f)

        # refresh info
        self.update_info_label(doc_name)

        self.mytext.configure(state="disabled") # disable textbox again
        self.save_button.pack_forget() # hide Save button (user will need to request to update again)
        self.bot.pack_forget() # hide bottom frame as well

class Collab_Documents_OU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='orange')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent
        
        back_button = Button(self, text="Back to OU Home Page", command=lambda: parent.show_frame(OrdinaryUserPage))
        back_button.pack(side=BOTTOM)

        self.bot = Frame(self) # frame in which 'Save' button would appear
        self.bot.pack(side=BOTTOM)
        self.save_button = Button(self.bot, text="Save changes") # button that appears when user requests to edit

        docs_label = Label(self, text= "Choose Document")
        docs_label.pack(side=TOP)

        doc_options = []

        with open("Databases/Documents/Shared documents.json", "r") as f:
            shared_docs = json.load(f)

        # doc_options will contain the names of only those shared documents whose collaborators include Application.current_logged_in_user
        for key, value in shared_docs.items():
            if Application.current_logged_in_user in value[4]:
                doc_options.append(key)

        self.docinfo_label = Label(self, text="Owner:\nVersion:\nMode:\nRead/update count:\nCollaborators:\nLock status:\nLast updated by:",
                                   justify=LEFT, font = ("Courier", 11))

        self.variable = StringVar(self)
        if doc_options != []:
            self.variable.set(doc_options[0])
            self.w1 = OptionMenu(self, self.variable, *doc_options, command=self.update_info_label)
            self.w1.pack(side=TOP)
        else:
            self.variable.set('')
            self.w1 = OptionMenu(self, self.variable, '', command=self.update_info_label)
            self.w1.pack(side=TOP)

        self.docinfo_label.pack(pady=9, side=TOP)

        action_label = Label(self, text="What would you like to do?")
        action_label.pack(side=TOP, padx=5, pady=5)
        action_options = ["Read", "Lock", "Edit", "Unlock", "Retrieve previous version"]

        self.variable2 = StringVar(self)
        self.variable2.set(action_options[0])
        self.w2 = OptionMenu(self, self.variable2, *action_options)
        self.w2.pack(side=TOP)

        self.top = Frame(self) # frame in which a third optionmenu may later appear (right below the second optionmenu)
        self.top.pack(side=TOP)

        # update info label with first document's information
        if doc_options != []:
            self.update_info_label(doc_options[0])

        self.ok_button = Button(self, text='OK', command=self.doc_decision)
        self.ok_button.pack(side=TOP)

        self.mytext = scrolledtext.ScrolledText(self, font=("Times", 10))
        self.mytext.pack(expand=TRUE, fill=Y)
        self.mytext.configure(state="disabled")

    def document_info(self, document_name):
        with open("Databases/Documents/Shared documents.json", "r") as f:
            shared_docs = json.load(f)

            if document_name in shared_docs: 
                return shared_docs[document_name]
            else: # document could not be found
                return False

    def update_info_label(self, event):
        # The command called when you select a document from the document OptionMenu. it updates the info label
        doc_info = self.document_info(event)
        if doc_info != False:
            collab_list = doc_info[4]
            if len(collab_list) <= 4:
                formatted_collaborator_list = '  ' + ', '.join(collab_list)
            else:
                remainder = len(collab_list) % 4
                formatted_collaborator_list = '  ' + '\n  '.join([ ', '.join(x) for x in zip(collab_list[0::4], collab_list[1::4],
                                                                                             collab_list[2::4], collab_list[3::4]) ]) +\
                                              ',\n  ' + ', '.join(collab_list[-remainder:])

            update_info = ''
            version = str(doc_info[1])
            if doc_info[6] != {} and (version in doc_info[6]): # format update info if it exists
                update_info = doc_info[6][version][0] + " at " + doc_info[6][version][1]

            self.docinfo_label['text'] = ('Owner: {}\nVersion: {}\nMode: Shared\nRead/update count: {}\n').format(doc_info[0], doc_info[1], doc_info[3]) + \
                                         ('Collaborators:\n{}\nLock status: {}\n').format(formatted_collaborator_list, doc_info[5]) + \
                                         ('Last updated by: {}').format(update_info)

    def doc_decision(self):
        # if the user does not Save changes after requesting to edit and makes another request, the save button disappears and the textbox disabled.
        self.mytext.configure(state="disabled")
        self.save_button.pack_forget()
        self.bot.pack_forget()

        doc_name = self.variable.get()
        action_name = self.variable2.get()

        if doc_name == '':
            return

        if action_name == "Read":
            with open("Document/" + doc_name + ".txt", "r") as f:
                contents = f.read()
                self.mytext.configure(state="normal") # reenable text box to update its contents
                self.mytext.delete(1.0,END) # delete old contents
                self.mytext.insert(INSERT, contents) # insert new contents
                self.mytext.configure(state="disabled") # disable text box again
            # increment read/update count:
            self.increment_views(doc_name)
            self.update_info_label(doc_name)
        elif action_name == "Lock":
            f = open("Databases/Documents/Shared documents.json", "r+")
            shared_docs = json.load(f)
            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[5] == "Unlocked":
                    shared_docs[doc_name][5] = "Locked by " + Application.current_logged_in_user

                    f.seek(0)
                    json.dump(shared_docs, f)
                    f.close()

                    self.update_info_label(doc_name)
                else:
                    messagebox.showerror("Hmmm", "Already locked.")
        elif action_name == "Edit":
            # populate textbox with contents first
            with open("Document/" + doc_name + ".txt", "r") as f:
                contents = f.read()
                self.mytext.configure(state="normal") # reenable text box to update its contents
                self.mytext.delete(1.0,END) # delete old contents
                self.mytext.insert(INSERT, contents) # insert new contents

            with open("Databases/Documents/Shared documents.json", "r") as f:
                info = json.load(f)

            # check if the user has locked the document first before allowing them to update:
            if info[doc_name][5] != "Locked by " + Application.current_logged_in_user:
                messagebox.showerror("Error", "You must lock a shared document before updating.")
            else:
                self.mytext.configure(state="normal")
                self.bot.pack() # display bottom frame
                self.save_button['command'] = lambda f=doc_name: self.save_doc(f) # activate button
                self.save_button.pack() # display 'Save' button
  
        elif action_name == "Unlock":
            with open("Databases/Documents/Shared documents.json", "r") as f:
                shared_docs = json.load(f)

            if doc_name in shared_docs:
                doc_info = shared_docs[doc_name]
                if doc_info[5] == "Unlocked":
                    messagebox.showerror("Hmmm", "Already unlocked.")
                elif doc_info[5] == "Locked by " + Application.current_logged_in_user:
                    shared_docs[doc_name][5] = "Unlocked"

                    with open("Databases/Documents/Shared documents.json", "w") as f:
                        json.dump(shared_docs, f)

                    self.update_info_label(doc_name)
                else:
                    messagebox.showerror("Hmmm", "Someone else is updating this document.")

        elif action_name == "Retrieve previous version":
            history_folder = os.listdir("History files")
            options = [m for m in history_folder if re.match(doc_name + "_" + "[0-9]+" + ".h", m)]

            self.var1 = StringVar(self)
            self.top.pack()
            if options != []:
                self.var1.set(options[0])
                
                self.om = OptionMenu(self.top, self.var1, *options)
                self.om.pack()
            else:
                self.var1.set('')
                self.om = OptionMenu(self, self.var1, '')
                self.om.pack()


    def save_doc(self, doc_name):
        # get user input and write it
        saved_contents = self.mytext.get("1.0", "end-1c")
        with open("Document/" + doc_name + ".txt", "w") as f:
            f.write(saved_contents)

        # increment view count and version number and display the new data:
        self.increment_views_and_version(doc_name)

        # save updator and time information for the new version:
        with open("Databases/Documents/Shared documents.json", "r+") as f:
            shared_docs = json.load(f)

            current_version = shared_docs[doc_name][1]
            shared_docs[doc_name][6].update({current_version: [Application.current_logged_in_user, datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S")]})

            f.seek(0)
            json.dump(shared_docs, f)

        # refresh info
        self.update_info_label(doc_name)

        # return to previous state:
        self.mytext.configure(state="disabled") # disable textbox again
        self.save_button.pack_forget() # hide Save button (user will need to request to update again)
        self.bot.pack_forget() # hide bottom frame as well

    def increment_views(self, doc_name): # used for reading
        with open("Databases/Documents/Shared documents.json", "r+") as f:
            shared_docs = json.load(f)
            if doc_name in shared_docs:
                shared_docs[doc_name][3] += 1
            f.seek(0)
            json.dump(shared_docs, f)

    def increment_views_and_version(self, doc_name): # used for updating
        with open("Databases/Documents/Shared documents.json", "r+") as f:
            shared_docs = json.load(f)
            if doc_name in shared_docs:
                shared_docs[doc_name][3] += 1
                shared_docs[doc_name][1] += 1
            f.seek(0)
            json.dump(shared_docs, f)

class Recent_Documents_OU(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        rd_label0 = Label(self, text="What would you like to do?")
        rd_label0.pack(side=TOP)
        rd_options = ["Read", "Edit", "Retrieve previous version", "Change privacy setting", "Lock document", "Unlock document", "Remove collaborator"]
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

        fc_options = self.retrieve_ous_shared_docs()
        self.variable = StringVar(self)

        if (len(fc_options) != 0):
            self.variable.set(fc_options[0])
            w = OptionMenu(self, self.variable, *fc_options)
            w.pack(side=TOP)

            self.button1 = Button(self, text = "ok", command=self.retrieve_sd_collaborators)
            self.button1.pack(side=TOP)

        cnd_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        cnd_back_button.pack(side=BOTTOM)

    def retrieve_ous_shared_docs(self):
        f = open('Databases/Documents/Shared documents.json', 'r+')
        shared_doc_info = json.load(f)
        shared_docs = []
        for key in shared_doc_info:
            if Application.current_logged_in_user in shared_doc_info[key][3]:
                shared_docs.append(key)
        f.close()
        return shared_docs

    def retrieve_sd_collaborators(self):
        self.button1['state'] = DISABLED
        self.selected_doc = self.variable.get()
        f = open('Databases/Documents/Shared documents.json', 'r+')
        shared_doc_info = json.load(f)
        rsc_collaborators = []
        rsc_collaborators.append(shared_doc_info[self.selected_doc][0])

        for rsc_collaborator in shared_doc_info[self.selected_doc][3]:
            if (rsc_collaborator != Application.current_logged_in_user):
                rsc_collaborators.append(rsc_collaborator)

        f.close()
        fc_collab = rsc_collaborators
        self.fc_collab_var = StringVar(self)

        if(len(fc_collab) != 0):
            self.fc_collab_var.set(fc_collab[0])
            fc_om = OptionMenu(self, self.fc_collab_var, *fc_collab)
            fc_om.pack(side=TOP)
            self.rsc_button = Button(self, text = "ok", command=self.Complain_About)
            self.rsc_button.pack(side=TOP)

    def Complain_About(self):
        self.rsc_button['state'] = DISABLED
        self.T = Text(self, height = 3, width = 30)
        self.T.pack(side = TOP, pady = 10)
        self.T.insert(END, "Write complaint here")

        button0 = Button(self, text = "Submit", command=self.submit_complaint)
        button0.pack(side=TOP, pady = 5)

    def submit_complaint(self):
        try:
            self.selected_collaborator = self.fc_collab_var.get()
            self.complaint_text = self.T.get(1.0, END)
            sc_list = []
            sc_list.append(self.selected_doc)
            sc_list.append(self.selected_collaborator)
            sc_list.append(self.complaint_text)
            f = open('Databases/Complaints/Complaints.json', 'r+')
            sc_complaint = json.load(f)
            sc_complaint.update({Application.current_logged_in_user: sc_list})
            f.seek(0)
            f.truncate()
            json.dump(sc_complaint, f)
            f.close()
            messagebox.showinfo('Success', 'Your complaint was successfully submitted!')
            self.parent.show_frame(File_Complaints)
        except FileNotFoundError:
            f = open('Databases/Complaints/Complaints.json', 'w')
            json.dump({}, f)
            f.close()
            messagebox.showerror('Error', 'This file does not exist!')

class View_Complaints(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        label0 = Label(self, text = "View Complaints:")
        label0.pack(side=TOP)

        vc_options = self.retrieve_complaints()
        self.vc_var = StringVar(self)

        if (len(vc_options) != 0):
            self.variable.set(vc_options[0])
            w = OptionMenu(self, self.vc_var, *vc_options)
            w.pack(side=TOP)

           # self.button1 = Button(self, text = "ok", command=self.)
            self.button1.pack(side=TOP)

        vc_back_button = Button(self, text="Cancel", command=lambda: parent.show_frame(OrdinaryUserPage))
        vc_back_button.pack(side=BOTTOM)

    #in progress
    def retrieve_complaints(self):
        f = open('Databases/Complaints/Complaints.json', 'r+')
        rc_complaints = json.load(f)
        for key in shared_doc_info:
            if Application.current_logged_in_user in shared_doc_info[key][3]:
                shared_docs.append(key)
        f.close()
        return shared_docs

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
        new_file = self.cnd_entry.get()
        file_names = os.listdir("Document")

        if new_file == '':
            messagebox.showerror("Error", "File name can't be empty")
        elif (new_file + ".txt") not in file_names:
            open("Document/" + new_file + ".txt", "w") # save document.txt

            # We also have to save the information of the newly created (private) document in 'Unshared documents.json':

            with open("Databases/Documents/Unshared documents.json", "r+") as f:
                mydict = json.load(f)
                mydict.update({new_file: [Application.current_logged_in_user, 1, "Private", 0]})
                f.seek(0)
                json.dump(mydict, f)

            # show success message:
            messagebox.showinfo("Success", new_file + " created.")
        else:
            messagebox.showerror('Error', 'Can\'t create file. File name already exists.')

class accept_decline_invites(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='yellow')
        Frame.pack(self, side="top", fill="both", expand=True)
        Frame.grid_rowconfigure(self, 0, weight=1)
        Frame.grid_columnconfigure(self, 0, weight=1)

        self.parent = parent

        label1 = Label(self, text = "Pending invitations: ")
        label1.pack(side=TOP)
        
        self.listbox = Listbox(self)
        self.listbox.pack()

        if not os.path.isfile("Databases/Invitations/Pending invitations.json"):
            with open("Databases/Invitations/Pending invitations.json", "w") as g:
                json.dump({}, g)
     
        with open("Databases/Invitations/Pending invitations.json", "r") as f:
            v = json.load(f)

        if Application.current_logged_in_user in v:
            for doc in v[Application.current_logged_in_user]:
                self.listbox.insert(END, doc)

        adi_button0 = Button(self, text = 'Cancel', command=lambda: parent.show_frame(OrdinaryUserPage))
        adi_button0.pack(side=TOP, padx = 6, pady = 4)

        adi_button1 = Button(self, text = 'Accept', command=self.accept_invitation)
        adi_button1.pack(side=TOP, padx = 6, pady =4)

        adi_button2 = Button(self, text = 'Decline', command=self.decline_invitation)
        adi_button2.pack(side=TOP, padx = 6, pady = 4)

    def accept_invitation(self):
        doc = self.listbox.get(ANCHOR)
        if doc != '':
            with open("Databases/Documents/Shared documents.json", "r+") as f:
                shared_docs = json.load(f)
                shared_docs[doc][4].append(Application.current_logged_in_user)

                f.seek(0)
                json.dump(shared_docs, f)

            with open("Databases/Invitations/Pending invitations.json", "r+") as f:
                updated_dict = json.load(f)
                updated_dict[Application.current_logged_in_user].remove(doc)
                f.seek(0); f.truncate()
                json.dump(updated_dict, f)

            self.listbox.delete(ANCHOR)
        
    def decline_invitation(self):
        doc = self.listbox.get(ANCHOR)
        if doc == '': return
        with open("Databases/Invitations/Pending invitations.json", "r+") as f:
            updated_dict = json.load(f)
            updated_dict[Application.current_logged_in_user].remove(doc)
            f.seek(0); f.truncate()
            json.dump(updated_dict, f)
        self.listbox.delete(ANCHOR)


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
