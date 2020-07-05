import os

import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print("Financial Analysis")
    print("-------------------------")
    

    for row in csvreader:
        total_months = [len(list(csvreader))]
        print("Total Months: " + str(total_months))


