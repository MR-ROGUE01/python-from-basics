# importing the csv module
import pandas as pd
import csv

# field names
fields = ['Name', 'Email']

# data rows of csv file
rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
        ['Sanchit', 'sanchit.gfg@gmail.com'],
        ['Aditya', 'aditya.gfg@gmail.com'],
        ['Sagar', 'sagar.gfg@gmail.com'],
        ['Prateek', 'prateek.gfg@gmail.com'],
        ['Sahil', 'sahil.gfg@gmail.com']]

# name of csv file
filename = "email_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    
    # writing the fields
    csvwriter.writerow(fields)
    
    # writing the data rows
    csvwriter.writerows(rows)
    
data = pd.read_csv('email_records.csv')
print(data)