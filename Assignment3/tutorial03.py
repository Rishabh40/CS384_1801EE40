import csv
import re
import shutil
import os


def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/gender'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'gender')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'gender')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "gender":
                with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/gender/female.csv', 'a', newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
                with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/gender/male.csv', 'a', newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
            elif row[4] == "Female":
                with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/gender/female.csv', 'a', newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
            else:
                with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/gender/male.csv', 'a', newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass