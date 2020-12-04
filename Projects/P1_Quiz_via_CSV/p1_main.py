# Rishabh Agarwal
# 1801EE40
# Importing Required Modules
import csv
import sqlite3
import datetime
import os
import re
import keyboard
import time
from numpy.core.numeric import roll
import pandas as pd
import threading
from tkinter import *
import shutil
import bcrypt
import getpass as gp

# # Please note in responses marked_choices will be blank if time is over or forcefully submitted  # #
# global variable to determine how the quiz is finished ex- time over,
# ques over or user chose to finish or the quiz is still goin on
global flag
# 1 quiz goin on
# 2 timer off
# -1 user forcefully submitted
# 0 ques over


def goto():
    """   Gives the user a chance to access whatever ques he/she wants   """
    i = int(input('which question you want to go: '))
    os.system("cls" if os.name == "nt" else "clear")
    with open(r'./quiz_wise_questions/'+quiz_number+'.csv', 'r') as file:
        reader = csv.reader(file)
        row = list(reader)
        print("Roll No- ", rollno)
        print("Name- ", Name)
        print("Goto Question: (Press - Ctrl+Alt+g)")
        print("Final Submit: (Press Ctrl+Alt+f)")
        print("Export Database Into CSV: (Press Ctrl+Alt+e)")
        print("Ques No ", row[i][0], sep=':-')
        print(row[i][1], " ?")
        print("Option 1) ", row[i][2])
        print("Option 2) ", row[i][3])
        print("Option 3) ", row[i][4])
        print("Option 4) ", row[i][5])
        print("Credits if correct option: ", row[i][7])
        print("Negative Marking: ", row[i][8])
        print("Is Compulsory: ", row[i][9])
    print("Press esc to continue!!")
    pass


def extract_database(username):
    """  Extracting users data into a csv file  """
    con = sqlite3.connect("project1_quiz_cs384.db")
    c = con.cursor()
    c.execute("SELECT * FROM project1_marks WHERE roll=?", (username,))
    lst = c.fetchall()
    header = ['Roll', 'quiz_num', 'marks', 'Time_of_submission']
    current_time = datetime.datetime.now()
    for tup in lst:
        details = list(tup)
        details.append(current_time)
        if not os.path.isfile(r'./quiz_wise_responses/scores_'+tup[1]+'.csv'):
            with open(r'./quiz_wise_responses/scores_'+tup[1]+'.csv', 'w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
        else:
            input_file = open(
                r'./quiz_wise_responses/scores_'+tup[1]+'.csv', "r+")
            reader_file = csv.reader(input_file)
            value = len(list(reader_file))
            if value == 0:
                with open(r'./quiz_wise_responses/scores_'+tup[1]+'.csv', 'w', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)

        with open(r'./quiz_wise_responses/scores_'+tup[1]+'.csv', 'a+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(details)


def quiz_submit():
    """  Giving user a chance to submit quiz before time  """
    global flag
    if flag == 1:
        flag = -1
    print("Quiz Submitted!!")
    pass


def timer(t):
    """ A GUI Based yimer which will run along with quiz """
    global flag
    root = Tk()
    root.geometry("300x80")
    root.title("Time Counter")

    minute = StringVar()
    second = StringVar()

    minute.set("00")
    second.set("00")

    minuteEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=100, y=20)

    secondEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=second)
    secondEntry.place(x=150, y=20)

    while t > -1:
        if flag != 1:
            break
        mins, secs = divmod(t, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        t -= 1
    if flag == 1:
        flag = 2


def start_quiz(rollno, Name, quiz_number):
    """ Function to start the quiz """
    global flag
    flag = 1
    mark = 0
    conn = sqlite3.connect('project1_quiz_cs384.db')
    c = conn.cursor()
    header = []
    input_file = open(r'./quiz_wise_questions/'+quiz_number+'.csv', "r+")
    reader_file = csv.reader(input_file)
    value = len(list(reader_file))
    lst = []
    for i in range(1, value):
        lst.append(i)
    Correct_Choices, Wrong_choices, Unattempted, Marks_Obtained, Total_Quiz_Marks = 0, 0, 0, 0, 0
    with open(r'./quiz_wise_questions/'+quiz_number+'.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if header == []:
                header = row
                header.pop()
                header.append("marked_choice")
                with open(r'./individual_responses/'+quiz_number+'_'+rollno+'.csv', 'w', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
            else:
                print("Roll No- ", rollno)
                print("Name- ", Name)
                print('Unattempted questions- ', lst)
                print("Goto Question: (Press - Ctrl+Alt+g)")
                print("Final Submit: (Press Ctrl+Alt+f)")
                print("Export Database Into CSV: (Press Ctrl+Alt+e)")
                if flag == 1:
                    print("Press esc to continue!")
                    keyboard.wait('esc')
                answer = -1
                if flag == 1:
                    print("Ques No ", row[0], sep=':-')
                    print(row[1], " ?")
                    print("Option 1) ", row[2])
                    print("Option 2) ", row[3])
                    print("Option 3) ", row[4])
                    print("Option 4) ", row[5])
                    print("Credits if correct option: ", row[7])
                    print("Negative Marking: ", row[8])
                    print("Is Compulsory: ", row[9])
                    if row[9] == 'n':
                        answer = input("Enter choice [1/2/3/4/S]: S to Skip ")
                    else:
                        answer = input("Enter choice [1/2/3/4]: ")
                if flag == 2 and answer != -1:
                    mark = -1
                    answer = -1
                Total_Quiz_Marks += int(row[7])
                temp = row
                temp.pop()
                if answer == -1:
                    Unattempted += 1
                    temp.append("")
                elif answer != 'S':
                    temp.append(answer)
                    if int(answer) == int(row[6]):
                        Correct_Choices += 1
                        Marks_Obtained += int(row[7])
                    else:
                        Wrong_choices += 1
                        Marks_Obtained += int(row[8])
                    lst.remove(int(row[0]))
                else:
                    temp.append(answer)
                    Unattempted += 1
                with open(r'./individual_responses/'+quiz_number+'_'+rollno+'.csv', 'a+', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(temp)
                os.system("cls" if os.name == "nt" else "clear")

    if flag == 1:
        flag = 0
    # Inserting the users marks into the DataBase
    try:
        c.execute(
            "DELETE from project1_marks WHERE roll=? AND quiz_num=?", (rollno, quiz_number))
        conn.commit()
        c.execute("INSERT INTO project1_marks VALUES(?, ?, ?)",
                  (rollno, quiz_number, Marks_Obtained))
        conn.commit()
    except:
        print("There is some Mistake!!")
    if flag == -1:
        print("Press Ctrl+alt+e to extract marks from database and esc to get results!!")
        keyboard.wait('esc')

    if mark == -1:
        print("Time over! last answer not submitted!")
    if flag != -1:
        print("Roll No- ", rollno)
        print("Name- ", Name)
        print('Unattempted questions- ', lst)
        if flag != 1:
            print("Export Database Into CSV: (Press Ctrl+Alt+e)")
            print("Press esc to get results!")
            keyboard.wait('esc')

    # Inserting the responses into a individual csv file
    additional_col = {
        "Total": [Correct_Choices, Wrong_choices,
                  Unattempted, Marks_Obtained, Total_Quiz_Marks],
        "Legend": ["Correct Choices", "Wrong Choices",
                   "Unattempted", "Marks Obtained", "Total Quiz Marks"]
    }
    new_df = pd.DataFrame(additional_col)
    df = pd.read_csv(r'./individual_responses/' +
                     quiz_number+'_'+rollno+'.csv')
    df = pd.concat([df, new_df], axis=1)
    if os.path.isfile(r'./individual_responses/'+quiz_number+'_'+rollno+'.csv'):
        os.remove(r'./individual_responses/'+quiz_number+'_'+rollno+'.csv')
    df.to_csv(r'./individual_responses/'+quiz_number +
              '_'+rollno+'.csv', index=False)

    # Letting the user know his/her performance
    if flag == -1:
        print("Roll No- ", rollno)
        print("Name- ", Name)
        print('Unattempted questions- ', lst)
    print("Total Quiz Questions: ", Correct_Choices+Wrong_choices+Unattempted)
    print("Total Quiz Questions Attempted: ", Correct_Choices+Wrong_choices)
    print("Total Correct Question Attempted: ", Correct_Choices)
    print("Total Wrong Questions Attempted: ", Wrong_choices)
    print(f'Total Marks: {Marks_Obtained}/{Total_Quiz_Marks}')


def Login():
    """  Logging in user  """
    username = input("Enter your username/rollno: ")
    # Taking PassWord in Protected Manner
    password = gp.getpass("Enter your password: ")
    # hashed Password
    hashable_pw = bytes(password, encoding="utf-8")
    c.execute("SELECT * FROM project1_registration WHERE username=?", (username,))
    lst = c.fetchall()
    if lst == []:
        print("you are not registered!")
        n = int(input("Press 1 to register and 2 to exit: "))
        if n == 1:
            return Registration()
        else:
            exit(0)
    else:
        if lst[0][0] == username and bcrypt.checkpw(hashable_pw, lst[0][1]):
            print("Successfully logged in!!")
        else:
            print("Either Username or Password is Invalid")
            return Login()
    return username


def Registration():
    """  Registering current user  """
    name = input("Enter your Name: ")
    roll = input("Enter Roll Number: ")
    # Saving PassWord in Protected Manner
    password = gp.getpass("Enter your password: ")
    whatsapp_number = int(input("Enter WhatsApp Number: "))

    c.execute("SELECT * FROM project1_registration WHERE username=?", (roll,))
    lst = c.fetchall()

    if lst:
        print("You are already registered! Please Login!!")
        temp = int(input("Press 2 to Login and 1 to exit: "))
        if temp == 2:
            return Login()
        else:
            exit(0)

    # hashing password
    hashable_pw = bytes(password, encoding="utf-8")
    hashed_pw = bcrypt.hashpw(hashable_pw, bcrypt.gensalt())
    c.execute("INSERT INTO project1_registration VALUES(?, ?, ?, ?)",
              (roll, hashed_pw, name, whatsapp_number))
    conn.commit()
    print("You are Registered!!")
    return roll


# Creating a DataBase and connecting it to this script
conn = sqlite3.connect('project1_quiz_cs384.db')
c = conn.cursor()

# Table 1 this will store user Bio
try:
    c.execute("""CREATE TABLE project1_registration (
                username text,
                password text,
                name text,
                whatsappNumber integer
                )
            """)
except:
    pass


# Table 2 this will Store User Academic data
try:
    c.execute("""CREATE TABLE project1_marks (
                roll text,
                quiz_num text,
                total_marks integer
                )
            """)
except:
    pass

# commit the changes
conn.commit()

# Asking the user what he wants to do
Reg_log = int(input("Enter 1 to Register and 2 to Login: "))
rollno = None
if Reg_log == 1:
    # Register Him if he choses so
    rollno = Registration()
else:
    # Login
    rollno = Login()


# Creating shortcut key for users convinience during the quiz
keyboard.add_hotkey("ctrl+alt+f", quiz_submit)
keyboard.add_hotkey("ctrl+alt+e", extract_database, args=(rollno,))
keyboard.add_hotkey("ctrl+alt+g", goto)


# Fetching the name of current user from DataBase
c.execute("SELECT * FROM project1_registration WHERE username=?", (rollno,))
Name = c.fetchall()[0][2]

# Asks the user what he want to do as now he/she is Logged in
quiz_number = str(
    input("Which quiz you want to take? [q1/q2/q3] or press 0 to exit: "))
if quiz_number == '0':
    # if he choose to exit
    exit(0)
elif quiz_number == 'q1' or quiz_number == 'q2' or quiz_number == 'q3':
    # if he chooses to give a quiz that is available
    # extracting time given
    data = pd.read_csv(r'./quiz_wise_questions/'+quiz_number+'.csv')
    str = list(data.columns.values.tolist())[-1]
    te = re.findall(r'\d+', str)
    res = int(list(map(int, te))[0])
    t1 = threading.Thread(target=timer, args=(res*60,))
    t2 = threading.Thread(target=start_quiz, args=(rollno, Name, quiz_number,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
else:
    # else letting him know chosen quiz is not available
    print("Quiz number you entered is not available!! Press esc to exit and try again!! ")
    keyboard.wait('esc')

# closing the DataBase connection
conn.close()
