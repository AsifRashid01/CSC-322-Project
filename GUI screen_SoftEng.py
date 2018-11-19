from Tkinter import *                                                  # Using Tkinter for GUI properties
import tkMessageBox as box                                             # Importing MessageBox module


def DocumentSharingSystem_OU_SU():                                    # function to attain dialog box
    username = entry1.get()                                     # Asking User for username and password
    password = entry2.get()

    if (username == 's' and password == 's'):                    # Check to see if info is correct
        w = Tk()                                                # Setting up window using Tk and providing labels/titles
        w.title('Super User Options Page')
        w.configure(background='yellow')

        fr = Frame(w)

        Lab = Label(w, text='Correct Login, Welcome Super User!', font="Times 25 bold")
        Lab.pack(padx=15, pady=5)

        Lab0 = Label(w, text='What would you like to do?', font="Times 16 bold")
        Lab0.pack(padx=15, pady=6)

        button0 = Button(fr, text='See taboo words')            # Providing buttons for various SU options
        button0.pack(side=TOP, padx=5, pady=5)

        button1 = Button(fr, text='Unlock Locked documents')
        button1.pack(side=TOP, padx=6, pady=5)

        button2 = Button(fr, text='Update Membership')
        button2.pack(side=TOP, padx=7, pady=5)

        button3 = Button(fr, text='Process Complaints of OUs')
        button3.pack(side=TOP, padx=8, pady=5)

        button4 = Button(fr, text='Create new document')
        button4.pack(side=TOP, padx=9, pady=5)

        button5 = Button(fr, text='Invite OUs')
        button5.pack(side=TOP, padx=10, pady=5)

        button6 = Button(fr, text='Accept/Deny invitations')
        button6.pack(side=TOP, padx=11, pady=5)

        button7 = Button(fr, text='Get info about other OUs')
        button7.pack(side=TOP, padx=12, pady=5)

        Lab1 = Label(fr, text='Recent Documents: ', font="Times 25 bold")
        Lab1.pack(side=TOP, padx=14, pady=5)

        button8 = Button(fr, text='Document 1')
        button8.pack(side=LEFT, padx=17, pady=5)

        button9 = Button(fr, text='Document 2')
        button9.pack(side=LEFT, padx=16, pady=5)

        button9 = Button(fr, text='Document 3')
        button9.pack(side=LEFT, padx=15, pady=5)

        button10 = Button(w, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fr.pack(padx=100, pady=19)
        w.mainloop()  # Running main using window as dialog screen

    elif username == 'Ordinary User' and password == '0002':
        wi = Tk()                                              # Setting up window using Tk and providing labels/titles
        wi.title('Ordinary User Options Page')
        wi.configure(background='yellow')
        Labe = Label(wi, text='Correct Login, Welcome Ordinary User!', font="Times 25 bold")
        Labe.pack(padx=15, pady=5)

        fra = Frame(wi)

        Labe0 = Label(wi, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        but0 = Button(fra, text='Create new document')         # Providing buttons for various OU options
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fra, text='Invite OUs')
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

        button10 = Button(wi, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fra.pack(padx=100, pady=19)
        wi.mainloop()                                            # Running main using wi as dialog screen

    else:
        box.showinfo('Status', 'Invalid Login, Please Try Again')


def GU_Entry():
    g = Tk()                                             # Setting up window using Tk and providing labels/titles
    g.title('Guest User Login Page')
    g.configure(background='green')
    La = Label(g, text='Welcome Guest User!', font="Times 25 bold")
    La.pack(padx=15, pady=5)

    fram = Frame(g)

    Labe0 = Label(g, text='What would you like to do?', font="Times 16 bold")
    Labe0.pack(padx=15, pady=5)

    but0 = Button(fram, text='Read open documents')          # Providing buttons for various GU options
    but0.pack(side=TOP, padx=5, pady=5)

    but1 = Button(fram, text='Retrieve old versions')
    but1.pack(side=TOP, padx=6, pady=5)

    but2 = Button(fram, text='Complain about documents')
    but2.pack(side=TOP, padx=7, pady=5)

    but3 = Button(fram, text='Send Taboo word suggestions to SU')
    but3.pack(side=TOP, padx=7, pady=5)

    but4 = Button(fram, text='Apply to be OU')
    but4.pack(side=TOP, padx=7, pady=5)

    fram.pack(padx=100, pady=19)
    g.mainloop()  # Running main using window as dialog screen


window = Tk()                                                   # Setting up window using Tk and providing labels/titles
window.title('Login Page')
window.configure(background='red')                              # GUI Background color


frame = Frame(window)

Label0 = Label(window, text='Login Page', font="Times 16 bold")
Label0.pack(padx=15, pady=5)

Label1 = Label(window, text='Username:')
Label1.pack(padx=15, pady=5)

entry1 = Entry(window, bd=5)
entry1.pack(padx=15, pady=5)

Label2 = Label(window, text='Password:')
Label2.pack(padx=15, pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx=15, pady=7)

btn = Button(frame, text='Check Login', command=DocumentSharingSystem_OU_SU)    # Button to click to check login credentials

btn2 = Button(frame, text='Login as Guest User', command=GU_Entry)      # Button to log in as a guest

btn.pack(side=RIGHT, padx=5)
btn2.pack(side=RIGHT, padx=6)
frame.pack(padx=100, pady=19)
window.mainloop()                                               # Running main using window as dialog screen
