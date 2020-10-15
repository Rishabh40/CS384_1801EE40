import csv
import re
import shutil
import os
import datetime


def date_validation(day, month, year):
    isValidDate = True
    try:
        datetime.datetime(int(year),
                          int(month), int(day))
    except ValueError:
        isValidDate = False
    if year < 1995 or year > 2020:
        isValidDate = False
    return isValidDate


def course():
    # Read csv and process
    pass


def country():
    # Read csv and process
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/country'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'country')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'country')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                country_path = os.path.join(
                    'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/country', row[2]+'.csv')
                if not os.path.isfile(country_path):
                    with open(country_path, 'a', newline='') as file:
                        head = csv.writer(file)
                        head.writerow(header)
                with open(country_path, 'a', newline='') as file:
                    data = csv.writer(file)
                    data.writerow(row)
    pass


def email_domain_extract():
    # Read csv and process
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/email_domain'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'email_domain')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'email_domain')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        pattern = re.compile(
            r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                if re.match(pattern, row[3]):
                    temp = row[3][row[3].index('@')+1:]
                    domain = temp[:temp.index('.')]
                    domain_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/email_domain', domain+'.csv')
                    if not os.path.isfile(domain_path):
                        with open(domain_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(domain_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
                else:
                    domain_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/email_domain', 'misc.csv')
                    if not os.path.isfile(domain_path):
                        with open(domain_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(domain_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
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
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'dob')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'dob')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                pattern = row[5].split('-')
                day = int(pattern[0])
                month = int(pattern[1])
                year = int(pattern[2])
                if date_validation(day, month, year):
                    range1_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'bday_1995_1999.csv')
                    range2_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'bday_2000_2004.csv')
                    range3_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'bday_2005_2009.csv')
                    range4_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'bday_2010_2014.csv')
                    range5_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'bday_2015_2020.csv')
                    if year >= 1995 and year <= 1999:
                        if not os.path.isfile(range1_path):
                            with open(range1_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range1_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2000 and year <= 2004:
                        if not os.path.isfile(range2_path):
                            with open(range2_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range2_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2005 and year <= 2009:
                        if not os.path.isfile(range3_path):
                            with open(range3_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range3_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2010 and year <= 2014:
                        if not os.path.isfile(range4_path):
                            with open(range4_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range4_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2015 and year <= 2020:
                        if not os.path.isfile(range5_path):
                            with open(range5_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range5_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                else:
                    mics_path = os.path.join(
                        'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/dob', 'misc.csv')
                    if not os.path.isfile(mics_path):
                        with open(mics_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(mics_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


def state():
    # Read csv and process
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/state'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'state')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'state')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                state_path = os.path.join(
                    'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/state', row[7]+'.csv')
                if not os.path.isfile(state_path):
                    with open(state_path, 'a', newline='') as file:
                        head = csv.writer(file)
                        head.writerow(header)
                with open(state_path, 'a', newline='') as file:
                    data = csv.writer(file)
                    data.writerow(row)
    pass


def blood_group():
    # Read csv and process
    path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics'
    if os.path.isdir(path):
        spe_path = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/blood_group'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'blood_group')
        os.mkdir(curr_path)
    else:
        parent_dir = 'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'blood_group')
        os.mkdir(final_path)
    with open('C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/studentinfo_cs384.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                blood_path = os.path.join(
                    'C:/Users/RISHABH AGARWAL/Downloads/SEM 5/CS384-Python/CS384_1801EE40/Assignment3/analytics/blood_group', row[6]+'.csv')
                if not os.path.isfile(blood_path):
                    with open(blood_path, 'a', newline='') as file:
                        head = csv.writer(file)
                        head.writerow(header)
                with open(blood_path, 'a', newline='') as file:
                    data = csv.writer(file)
                    data.writerow(row)
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass


dob()
email_domain_extract()
country()
state()
gender()
blood_group()
