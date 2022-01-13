import csv
import tkinter as tk
from tkinter import W
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import *



import mainV2
from mainV2 import startWeb

import re

fileName = 'Records.csv'
accessMode = 'r+'

def processRecord(userName,staffNumber, password, confPassword):
    with open(fileName, 'a') as file:
        with open(fileName, 'r+') as file:
            fullList = file.readlines()
            fullList = list(dict.fromkeys(fullList))
            dataToSend = f"\n{userName.upper()},{staffNumber},{password},{confPassword}\n"

            if dataToSend not in fullList:

                file.writelines(dataToSend)

            elif dataToSend in fullList:
                print('This already exist')


        file.close()

def defaultAdmin():
    defAdminRecord = 'Joel RIOHE TONKA,30104386,Play2020,Play2020'
    with open(fileName, 'a') as file:
        with open(fileName, 'r+') as file:

            allRows= file.readlines()

            if defAdminRecord not in allRows:
                file.write(defAdminRecord)

    # file.close()

def getSigned_Info():
    username_info = username.get()
    staffNumber_info = staffNumber.get()
    password_info = password.get()
    confPassword_info = confPassword.get()

    global newTitle

    if username_info == '' or staffNumber_info == '' or password_info == '' or confPassword_info == '':
        newTitle = f'Sorry {username_info.upper()} none of fields can be empty!!! TRY AGAIN'
        smsLabel.config(text=newTitle, bg='red', font=("Garamond",  13, 'bold'))
        loadProgram()
        print("None of fields can be empty")
    elif password_info != confPassword_info:
        print("Passwords don't match")
        newTitle = f'Sorry {username_info.upper()} your password must be the same'

        smsLabel.config(text=newTitle, bg='purple', font=("Garamond",  13, 'bold'))

    elif (len(username_info)<3 or len(username_info)>15) or (len(staffNumber_info)<3 or len(staffNumber_info)>15) or (len(password_info)<3 or len(password_info)>15) or (len(confPassword_info)<3 or len(confPassword_info)>15):

        newTitle = f'Sorry {username_info.upper()} fields should be more than 3 chars AND less than 15'
        smsLabel.config(text=newTitle, bg='pink',font=("Garamond",  13, 'bold'))
    elif not staffNumber_info.isdigit() or len(staffNumber_info) != 8:
        newTitle = f'Sorry {username_info.upper()} your staff number should be 8 integers'
        smsLabel.config(text=newTitle, bg='brown', font=("Garamond",  13, 'bold'))

    else:
        #  -----------Enter values if do not exist not in file
        processRecord(username_info, staffNumber_info, password_info, confPassword_info)
        newTitle = f'Hi {username_info} you are now an admin'
        smsLabel.config(text=newTitle, bg='green',font=("Garamond",  13, 'bold'))


    nameEntry.delete(0, END)
    staffNumberEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confPassEntry.delete(0, END)

def getLogin_Info():


    global loginNewTitle
    global loginUsername_info
    global loginStaffNumber_info
    global loginPassword_info

    loginUsername_info = loginUsername.get().upper()
    loginStaffNumber_info = loginStaffNumber.get()
    loginPassword_info = loginPassword.get()

    with open(fileName, accessMode) as file:
        readAllRows = file.readlines()
        readAllRows = list(dict.fromkeys(readAllRows))  #  ---Eliminate any duplications
        for row in readAllRows:
            newRow = row.split(',')


            if loginUsername_info == newRow[0] and loginStaffNumber_info == newRow[1] and loginPassword_info == newRow[2]:
                print("Welcome " + loginUsername_info)
                 #  -----------------LOAD SOFTWARE HERE-----------------


                loginNewTitle = f'Welcome {loginUsername_info}, program loaded...'
                loginSMSLabel.config(text=loginNewTitle, bg='green', font=("Garamond",  13, 'bold'))
                loadProgram()  #-----------------------------------------

                break
            elif (loginUsername_info == '') or (loginStaffNumber_info == '') or (loginPassword_info == ''):
                loginNewTitle = f'Sorry {loginUsername_info} none of fields can be empty!!! TRY AGAIN'
                loginSMSLabel.config(text=loginNewTitle, bg='red', font=("Garamond",  13, 'bold'))
                print('No text fields empty')
            elif loginUsername_info != newRow[0] or loginStaffNumber_info != newRow[1] or loginPassword_info != newRow[2] :
                loginNewTitle = f'Sorry incorrect name, staff number or password'
                loginSMSLabel.config(text=loginNewTitle, bg='purple')
                print(f'Sorry incorrect name, staff number or password')
            else:
                print('No such  a user '+ loginUsername_info)



    loginNameEntry.delete(0, END)
    loginStaffNumberEntry.delete(0, END)
    loginPasswordEntry.delete(0, END)

def loadProgram():
    print('Loading cameras')
    startWeb()

#  -------This method loads admin view
def screenViewAdmins():

    screenAdmins = tk.Tk()
    screenAdmins.geometry('600x500')
    screenAdmins.resizable(0, 0)
    screenAdmins.title('View all administrators')

    tittleLabel = tk.Label(screenAdmins, text="All administrators", bg="grey", width=600, height=2, font=("Garamond",  24, 'bold'))
    tittleLabel.pack(side=TOP, pady=20)

    adminText = tk.Text(screenAdmins, width=150, height=200)
    adminText.pack()


    with open(fileName, accessMode) as dataFile:

        dataList = dataFile.readlines()
        # dataList = list(dict.fromkeys(dataList))

        for row in dataList:
            adminText.insert(tk.END, row)
            # print(row)
        adminText.config(state= DISABLED)


    screenAdmins.mainloop()

def chechIfAdmin():
    global loginUsername_info

    loginUsername_info = loginUsername.get().upper()
    loginStaffNumber_info = loginStaffNumber.get()
    loginPassword_info = loginPassword.get()

    with open(fileName, accessMode) as file:
        readAllRows = file.readlines()
        readAllRows = list(dict.fromkeys(readAllRows))  # ---Eliminate any duplications
        for row in readAllRows:
            newRow = row.split(',')

            if loginUsername_info == newRow[0] and loginStaffNumber_info == newRow[1] and loginPassword_info == newRow[2]:
                print("Welcome " + loginUsername_info+ 'you can add a new administrator')
                #  -----------------LOAD SOFTWARE HERE-----------------

                loginNewTitle = f'Welcome {loginUsername_info} you can add a new administrator'
                loginSMSLabel.config(text=loginNewTitle, bg='green',font=("Garamond",  13, 'bold'))
                screenSign()
                break

            elif (loginUsername_info == '') or (loginStaffNumber_info == '') or (loginPassword_info == ''):
                loginNewTitle = f'Sorry {loginUsername_info} none of fields can be empty!!! TRY AGAIN'
                loginSMSLabel.config(text=loginNewTitle, bg='red',font=("Garamond",  13, 'bold'))
                print('No text fields empty')

            elif loginUsername_info != newRow[0] or loginStaffNumber_info != newRow[1] or loginPassword_info != newRow[2]:
                print("Sorry you not an admin")
                loginNewTitle = f'Please first become an administrator'
                loginSMSLabel.config(text=loginNewTitle, bg='Red',font=("Garamond",  13, 'bold'))
            else:
                print('No such  a user ' + loginUsername_info)


    loginNameEntry.delete(0, END)
    loginStaffNumberEntry.delete(0, END)
    loginPasswordEntry.delete(0, END)


def screenLogins():
    # defaultAdmin()

    global screenLogIn
    screenLogIn = Tk()
    screenLogIn.geometry('600x500')
    screenLogIn.resizable(0, 0)
    screenLogIn.title('Log in')


    global loginUsername
    global loginStaffNumber
    global loginPassword
    global loginNameEntry
    global loginStaffNumberEntry
    global loginPasswordEntry

    global loginSMSLabel
    global text

    loginUsername = tk.StringVar()
    loginStaffNumber = tk.StringVar()
    loginPassword = tk.StringVar()


    tittleLabel = tk.Label(screenLogIn, text="Log in as admin or create a profile", bg="grey", width=600, height=2, font=("Garamond", 24, 'bold'))
    tittleLabel.pack(side=TOP, pady=1)

    nameLabel = tk.Label(screenLogIn, text="Enter full name", bg="grey",width=600, font=('Garamond', 13))
    nameLabel.pack(padx=0, pady=8)

    loginNameEntry = tk.Entry(screenLogIn, textvariable=loginUsername, width=25)
    loginNameEntry.pack(pady=8)

    staffNumberLabel = tk.Label(screenLogIn, text='Enter staff number', bg="grey", width=600, font=('Garamond', 13))
    staffNumberLabel.pack(pady=8)

    loginStaffNumberEntry = tk.Entry(screenLogIn,textvariable=loginStaffNumber, width=25)
    loginStaffNumberEntry.pack(pady=8)

    loginPasswordLabel = tk.Label(screenLogIn, text='Enter password', bg="grey", width=600, font=('Garamond', 13))
    loginPasswordLabel.pack(pady=8)

    loginPasswordEntry = Entry(screenLogIn,textvariable= loginPassword, show="*", width=25)
    loginPasswordEntry.pack(pady=35)

    loginSMSLabel = Label(screenLogIn, text="", bg="pink", width=600, height=1, font=("Garamond", 13))
    loginSMSLabel.pack()

    loginButton = Button(screenLogIn, text="Login", font=("Garamond", 13), width=15, command=getLogin_Info)
    loginButton.pack(side=LEFT, padx=85)


    createProfileButton = Button(screenLogIn, text="Create account", font=("Garamond", 13), width=20, command=chechIfAdmin)
    createProfileButton.pack(side=LEFT, padx=65)



    #  ----------- Get a default administrator----------


    screenLogIn.mainloop()

def screenSign():

    screenSign = Toplevel(screenLogIn)
    screenSign.geometry('600x500')
    screenSign.resizable(0, 0)
    screenSign.title('Sign up')



    global username
    global staffNumber
    global password
    global confPassword

    global nameEntry
    global staffNumberEntry
    global passwordEntry
    global confPassEntry

    global smsLabel
    global text



    username = tk.StringVar()
    staffNumber =  tk.StringVar()
    password =  tk.StringVar()
    confPassword =  tk.StringVar()





    tittleLabel = tk.Label(screenSign, text=f"Please sign or view an administrator", bg="grey", width=600, height=2, font=("Garamond",  24, 'bold'))
    tittleLabel.pack(side=TOP, pady=1)

    nameLabel = tk.Label(screenSign, text="Enter full name", bg="grey", width=600, font=('Garamond', 13))
    nameLabel.pack(padx=0, pady= 8)

    nameEntry = Entry(screenSign, textvariable=username, width=25)
    nameEntry.pack(pady=8)

    staffNumberLabel = tk.Label(screenSign, text='Enter staff number', bg="grey",width=600, font=('Garamond', 13))
    staffNumberLabel.pack(pady=8)

    staffNumberEntry = Entry(screenSign, textvariable=staffNumber, width=25)
    staffNumberEntry.pack(pady=8)

    passwordLabel = tk.Label(screenSign, text='Enter password', bg="grey",width=600, font=('Garamond', 13))
    passwordLabel.pack(pady=8)

    passwordEntry = Entry(screenSign, textvariable=password, show="*", width=25)
    passwordEntry.pack(pady=8)

    confPassLabel = tk.Label(screenSign, text='Confirm password', bg="grey",width=600, font=('Garamond', 13))
    confPassLabel.pack(pady=8)

    confPassEntry = Entry(screenSign, textvariable=confPassword, show="*", width=25)
    confPassEntry.pack(pady=20)

    smsLabel = Label(screenSign, text="", bg="grey", width=600, height=1, font=("Garamond", 13))
    smsLabel.pack()

    signButton = Button(screenSign, text="Sign up", font=("Garamond", 13), width=15, command=getSigned_Info)
    signButton.pack(side=RIGHT,padx=35)

    viewAdmin = Button(screenSign,text ="View administrators", font= ("Garamond", 13), width= 15, command=screenViewAdmins)
    viewAdmin.pack(side=RIGHT, padx=20)

    BackButton = Button(screenSign, text="Back to login ", font=("Garamond", 13), width=15, command= screenSign.destroy)
    BackButton.pack(side=RIGHT, padx=20)



try:
    screenLogins()
except:
    print('Sorry the program was interrupted')



