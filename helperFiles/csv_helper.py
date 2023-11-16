from datetime import datetime
now = datetime.now()
import csv
from csv import writer

def create_csv(file_name):
    date_time = now.strftime("%m-%d-%Y, %H-%M-%S")
    file = open("{} - {}.csv".format(file_name,date_time), "w", newline='')
    return file

def add_data(file_name,fieldnames,rows):
    file = create_csv(file_name)
    # creating a csv dict writer object 
    writer = csv.DictWriter(file, fieldnames = fieldnames) 
    # writing headers (field names) 
    writer.writeheader() 
    # writing data rows 
    writer.writerows(rows)

def add_a_row(fileName, dataList):
    # Pre-requisite - Import the writer class from the csv module
    # from csv import writer
    
    # The data assigned to the list 
    # list_data=['03','Smith','Science']
    
    # Pre-requisite - The CSV file should be manually closed before running this code.

    # First, open the old CSV file in append mode, hence mentioned as 'a'
    # Then, for the CSV file, create a file object
    with open(fileName, 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(dataList)  
        # Close the file object
        f_object.close()

def openCSV(fileName):
    file = open(fileName, 'r')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
            rows.append(row)
    file.close()
    return rows