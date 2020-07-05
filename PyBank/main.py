#Import dependencies
import os

import csv

#Define variables
total_months = []
profit_loss = []

month_count = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

#Store csv file path
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')


#Open csv in read mode
with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csv_header = next(csvfile)
             
    #Read through each row of data after the header
    for row in csv_reader:

        #Count of months
        month_count = month_count + 1

        #Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (month_count == 1):
            #Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss

        else:

            #Find change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            #Add each month to the total_months[]
            total_months.append(row[0])

            #Add each profit_loss_change to the profit_loss[]
            profit_loss.append(profit_loss_change)

            #Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #Sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss)
    average_profit_loss = round(sum_profit_loss/(month_count - 1), 2)

    #Highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss)
    lowest_change = min(profit_loss)

    #Find the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss.index(highest_change)
    lowest_month_index = profit_loss.index(lowest_change)

    #Assign best and worst month
    best_month = total_months[highest_month_index]
    worst_month = total_months[lowest_month_index]

#Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


#Export text file with results
budget_analysis = os.path.join("Analysis", "budget_analysis.txt")
with open(budget_analysis, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")


