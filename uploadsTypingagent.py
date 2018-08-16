#!/usr/bin/env python3
'''Creates the import files for Seesaw using an exports from
Veracross. Use Google Sheets to transform the Excel files to CSV to preserve
the UTF-8 encoding of the text. The file fieldsSeesaw.py containing
the export file field names must be in the same folder as this program.
Import file names are set in the main function and the path of their location
is set using the 'inputs' variable.
Export file names should not be altered since ASM is expecting specific
file names. The path of their location is set using the 'results' variable.
****DO NOT CHANGE THE NAMES OF THE RESULT FILES.****
'''

#Import code desired from the standard library.
import csv
from sys import argv
from pathlib import Path
from getpass import getuser
from collections import defaultdict
#Import the fieldnames for the export files.
from fieldsTypingagent import typingagentFields as fields


def createClasses(inFile, outFile):
    #Create a CSV export file by processing the existing data files.
    with open(inFile, 'r') as dataIn, open(outFile, 'w') as dataOut:
        reader = csv.DictReader(dataIn)
        writer = csv.DictWriter(dataOut, fieldnames=fields(),
                                quoting=csv.QUOTE_ALL)
        #Put the header row of fields at the top of the output file.
        #Put the header row of fields at the top of the output file.
        writer.writeheader()
        #Output data to the file for all users.
        for row in reader:
            new = defaultdict(dict)
            new['Teacher Email'] = row['Teacher Email Address']
            new['Teacher First Name'] = row['CLASS: Teacher First Name']
            new['Teacher Last Name'] = row['CLASS: Teacher Last Name']
            new['Class Name'] = row['Class ID']
            new['Grade Level'] = row['Grade Level']
            new['Sign In Mode'] = 'Class Code'
            if (row['Grade Level']) is '6': new['Sign In Mode'] = 'Google'
            first = row['STUDENT: First Name']
            last = row['STUDENT: Last Name']
            new['Student Name'] = f'{first} {last}'
            new['Student ID'] = row['STUDENT: Email 1'][:row['STUDENT: Email 1'].find('@')]
            new['Student Email'] = row['STUDENT: Email 1']
            new['Student Password'] = ''
            new['Co-Teacher 1 Email'] = 'Class Code'
            new['Co-Teacher 1 First Name'] = 'Username'
            new['Co-Teacher 1 Last Name'] = 'First Name'
            new['Co-Teacher 2 Email'] = 'Last Name'
            new['Co-Teacher 2 First Name'] = 'Password'
            new['Co-Teacher 2 Last Name'] = 'Grade'
            new['Co-Teacher 3 Email'] = 'Action'
            new['Co-Teacher 3 First Name'] = ''
            new['Co-Teacher 3 Last Name'] = ''
            new['Co-Teacher 4 Email'] = ''
            new['Co-Teacher 4 First Name'] = ''
            new['Co-Teacher 4 Last Name'] = ''
            new['Co-Teacher 5 Email'] = ''
            new['Co-Teacher 5 First Name'] = ''
            new['Co-Teacher 5 Last Name'] = ''
            writer.writerow(new)
    return        #Output data to the file for all users.


def main():
    print()
    inputs = Path(f'downloads')
    results = Path('uploads')
    #Export files from Veracross in CSV format, UTF-8
    sourceClasses = f'{inputs}/VCtypingagent.csv'
    #CSV files for upload into Seesaw
    resultClasses = f'{results}/typingagent.csv'
    #Run functions to create the files
    createClasses(sourceClasses, resultClasses)
    print('Files are complete.')
    print()
    return


if __name__ == '__main__': main()
