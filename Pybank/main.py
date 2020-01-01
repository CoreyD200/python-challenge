#Pybank challenge. Corey Davidson
# 12/23/2019

import os
import csv
import sys

csvpath = os.path.join(".",'Resources', 'budget_data.csv')
filename = csvpath

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months = 0
    total_net = 0
    profitloss_amt = 0
    pl_list = []
    #accomodate header row
    header = next(csvreader)
    #move down one row to enable starting point from row above
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    greatest_profit = 0
    greatest_loss = 0

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        profitloss_amt = int(row[1]) - prev_net
        pl_list.append(profitloss_amt)
        prev_net = int(row[1])
        if profitloss_amt > greatest_profit:
            greatest_profit = profitloss_amt
            greatest_gain_date = row[0]
        elif profitloss_amt < greatest_loss:
            greatest_loss = profitloss_amt
            greatest_loss_date= row[0]
        


# get average from list that was created
def Average(pl_list):
    return sum(pl_list)/len(pl_list)


#declare variable of "output" for print statements. This allows to use the variable to write to the file 
output= (f"Total Months: {total_months} \n"
f'Net profit: ${total_net} \n'
f"Average Change: ${Average(pl_list)} \n"
f"Greatest gain was ${greatest_profit} which occurred {greatest_gain_date} \n"
f"Greatest loss was ${greatest_loss} which occurred {greatest_loss_date} \n")

#print out put to terminal
print (output)

#create .txt file and print output in to text file. "import sys" for this to work
sys.stdout=open("main_output.txt","w")
print (output)
sys.stdout.close()