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
