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
    group_data = [[0 for i in range(no_of_branches+2)]
                  for j in range(number_of_groups+1)]
    group_data[0][0] = "group"
    group_data[0][1] = "total"
    for i in range(2, no_of_branches+2):
        group_data[0][i] = Data[i-2][0]
    padd = len(str(number_of_groups))
    for i in range(1, number_of_groups+1):
        zeros = padd-len(str(i))
        group_data[i][0] = "Group_G"+'0'*zeros+str(i)+".csv"
    left = []
    for i in range(len(Data)):
        entry = int(floor(Data[i][1]/number_of_groups))
        for j in range(1, number_of_groups+1):
            group_data[j][i+2] = entry
        left.append(Data[i][1]-number_of_groups*entry)
    x = 1
    for i in range(len(left)):
        while left[i] > 0:
            group_data[x][i+2] += 1
            left[i] -= 1
            if x == number_of_groups:
                x = 1
            else:
                x += 1
    for i in range(1, number_of_groups+1):
        for j in range(2, no_of_branches+2):
            group_data[i][1] += group_data[i][j]
    if os.path.isfile(r'./groups/stats_grouping.csv'):
        os.remove(r'./groups/stats_grouping.csv')
    with open(r'./groups/stats_grouping.csv', 'w', newline="") as file:
        mp = csv.writer(file)
        mp.writerows(group_data)
    for i in range(1, number_of_groups+1):
        with open(r'./groups/'+group_data[i][0], 'w', newline="") as file:
            mp = csv.writer(file)
            mp.writerow(["Roll", "Name", "Email"])
    for i in range(2, no_of_branches+2):
        data = pd.read_csv(r'./groups/'+group_data[0][i]+'.csv')
        curr = 0
        for j in range(1, number_of_groups+1):
            df = data.iloc[curr:curr+group_data[j][i]]
            rows = df.values.tolist()
            curr += group_data[j][i]
            with open(r'./groups/'+group_data[j][0], 'a+', newline="") as file:
                mp = csv.writer(file)
                mp.writerows(rows)
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
