from math import floor
import csv
import os
import pandas as pd
import shutil


def deletion():
    # used for deletion of already created data

    return


def branch_classification(filename):
    # this function reads dat from input files and classify that according
    # to branches and creates csv files for diff. branches with stats file too.

    return


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
