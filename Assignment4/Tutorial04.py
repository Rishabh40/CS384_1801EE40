# Importing Required Libraries
import csv
import os
import shutil
import re


# Defining Patterns
Roll_Pattern = re.compile(r'^[0-9]{4}[A-Za-z]{2}[0-9]{2}$')
Credit_Sem_Pattern = re.compile(r'^[0-9]+$')
CourseCode_Pattern = re.compile(r'^[A-Z]{2}[0-9]{3}$', re.IGNORECASE)
Grade_Pattern = re.compile(r'AA|AB|BC|BB|CC|CD|DD|I|F', re.IGNORECASE)


# Check if Grades Folder Already Exists, If yes Delete and finally Remake
if(os.path.isdir(r'./grades')):
    shutil.rmtree('./grades')
os.makedirs('./grades')


# List containing all Roll Nos.
List_of_Rolls = []


# Creating a Misc file that will store all invalid cases
Misc_Head = ['Roll Number', 'Subject', 'Credit', 'Type', 'Grade', 'Semester']
with open('./grades/misc.csv', 'a', newline='') as file:
    f = csv.writer(file)
    f.writerow(Misc_Head)


# Opening the DataBase and Creating all Individual Files
with open('./acad_res_stud_grades.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != 'sl':
            if re.fullmatch(Roll_Pattern, row[1]) and re.fullmatch(Credit_Sem_Pattern, row[2]) and re.fullmatch(Credit_Sem_Pattern, row[5]) and re.fullmatch(CourseCode_Pattern, row[4]) and re.fullmatch(Grade_Pattern, row[6]):
                # If a valid Case Create individual files
                File_Name = row[1]+'_individual.csv'
                if not os.path.isfile('./grades/'+File_Name):
                    List_of_Rolls.append(row[1])
                    with open('./grades/'+File_Name, 'a', newline='') as Roll_file:
                        f = csv.writer(Roll_file)
                        f.writerow(['Roll: '+row[1]])
                        f.writerow(['Semester Wise Details'])
                        f.writerow(
                            ['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                entry = [row[4], row[5], row[8], row[6], row[2]]
                with open('./grades/'+File_Name, 'a', newline='') as Roll_file:
                    f = csv.writer(Roll_file)
                    f.writerow(entry)
            else:
                # Invalid Case
                with open('./grades/misc.csv', 'a', newline='') as invalid:
                    f = csv.writer(invalid)
                    f.writerow([row[1], row[4], row[5],
                                row[8], row[6], row[2]])


# Now we are Creating overall files and also deleting some individual files where
# In between semesters are missing
Data = []
for roll in List_of_Rolls:
    # iterating in all roll calls
    with open('./grades/'+roll+'_individual.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if re.fullmatch(CourseCode_Pattern, row[0]):
                Data.append(row)

    sorted_data = sorted(Data, key=lambda l: int(l[4]))

    Data.clear()  # Clear current roll data
    Prev_sem = '0'  # Imaginary sem to check in between missing sems
    status = True   # Valid Status
    for row in sorted_data:
        if int(row[4])-int(Prev_sem) > 1:
            status = False
            break
        Prev_sem = row[4]
    if status == False:
        for row in sorted_data:
            Inv_row = [roll, row[0], row[1], row[2], row[3], row[4]]
            with open('./grades/misc.csv', 'a', newline='') as file:
                f = csv.writer(file)
                f.writerow(Inv_row)
        os.remove('./grades/'+roll+'_individual.csv')  # removing invalid file
        continue
