#Import modules
import os
import csv

#Import file from relative path
csvpath = os.path.join("PyBank/Resources/budget_data.csv")

#Set variables for line count, total profit/loss, and an empty list to append change values to once they are calculated
lineCount = 0
totalProfitLoss = 0
changeList = []
changeValue = 0
startingValue = 0
averageChange = 0

#Open and read csv file
with open(csvpath, 'r', newline = "") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

    #Skip header
    next(csvreader, None)

    #Begin for loop to iterate through rows
    for row in csvreader:

        #Add one to lineCount for each row counted
        lineCount += 1
        
        #Add the value in column two for each row 
        totalProfitLoss = totalProfitLoss + int(row[1])

        #Calculate the change from one month to the next
        if startingValue == 0:

            startingValue = int(row[1])

        else:

            changeValue = int(row[1]) - startingValue

            changeList.append(changeValue)

            startingValue = int(row[1])

#Calculate the average change
averageChange = sum(changeList) / (lineCount - 1)


#Print all of the values calculated above
print("Financial Analyis")    
print("----------------------------")       
print(f"Total Months: {lineCount}")
print(f"Total: ${totalProfitLoss}")
print(f"Average Change: ${round(averageChange, 2)}")
print(f"Greatest Increase in Profits: ${max(changeList)}")
print(f"Greatest Decrease in Profits: ${min(changeList)}")
