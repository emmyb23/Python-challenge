# importing csv module 
import csv
import os

# Lists to store data
Month_Year = ['Jan-10','Feb-10','Mar-10','Apr-10']
Profit_Loss = ['867884','984655','322013','-69417']

from collections import Counter  

col_counts = Counter()           # or defaultdict(int)

last_value = object()            # won't show up in table
for row in csv_file:
    col_counts[row[field]] += 1
    if row[field] != last_value:
        print(col_counts[last_value])
        last_value = row[field]


# Define the function and have it accept the 'budget_data' as its sole parameter
def print_totals(csv_file):
    # For readability, it can help to assign your values to variables with descriptive names
    Month_Year = str(csv_file[0])
    Profit_Loss = int(csv_file[1])
    rows = len(group1)
    columns = len(group1[0])

   

    column = 1
    print(sum(row[column] for row in data))

    #print(f"Total months: {total_months}")
    #print(f"Total: {int(total)}")
    #print(f"Average Change: {int(ave_change)}")
    #print(f"Greatest Increase in Profit: {str(greatest_increase)}")
    #print(f"Greatest Decrease in Profit: {str(greatest_decrease)}")



with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

   

with open('Results.txt', 'w') as new_txt:
        csv_writer = csv_writer(new_txt, delimiter=",")

 


