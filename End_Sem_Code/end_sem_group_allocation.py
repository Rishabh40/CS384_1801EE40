from math import floor
import csv
import os
import pandas as pd
import shutil


def deletion():
    # used for deletion of already created data
    if os.path.isdir(r'./groups/'):
        shutil.rmtree(r'./groups/')
    os.mkdir(r'./groups/')
    return


def branch_classification(filename):
    # this function reads dat from input files and classify that according
    # to branches and creates csv files for diff. branches with stats file too.
    with open(r'./'+filename, 'r') as file:
        mp = csv.reader(file)
        header = []
        dic = {}
        for row in mp:
            if header == []:
                header = row
            else:
                branch = row[0][4:6]
                branch = branch.upper()
                if dic.get(branch) == None:
                    if os.path.isfile(r'./groups/'+branch+'.csv'):
                        os.remove(r'./groups/'+branch+'.csv')
                    with open(r'./groups/'+branch+'.csv', 'a+', newline="") as file:
                        mp = csv.writer(file)
                        mp.writerow(header)
                    dic[branch] = 0
                dic[branch] += 1
                with open(r'./groups/'+branch+'.csv', 'a+', newline="") as file:
                    mp = csv.writer(file)
                    mp.writerow(row)
        with open(r'./groups/branch_strength.csv', 'w', newline="") as file:
            mp = csv.writer(file)
            mp.writerow(["BRANCH_CODE", "STRENGTH"])
        Data = []
        for branch in dic.keys():
            Data.append([branch, dic[branch]])
        Data = sorted(Data, key=lambda x: int(x[1]), reverse=True)
        for row in Data:
            with open(r'./groups/branch_strength.csv', 'a+', newline="") as file:
                mp = csv.writer(file)
                mp.writerow(row)
    return len(Data), Data


def group_classification(number_of_groups, no_of_branches, Data):
    # this function is used to divide students into given no. of groups
    # and then finally creating those groups csv's along with stats file

    return


def group_allocation(filename, number_of_groups):
    # Entire Logic
    # You can add more functions, but in the test case, we will only call the group_allocation() method,
    deletion()
    no_of_branches, Data = branch_classification(filename)
    group_classification(number_of_groups, no_of_branches, Data)
    return


filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)
