#Import modules
import os
import csv

#Import file from relative path
csvpath = os.path.join("PyPoll/Resources/election_data.csv")

#Set Variables to count total votes and votes for each candidate
lineCount = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0

#Open and read csv file
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Skip header
    next(csvreader, None)

    #Begin for loop to iterate through rows
    for row in csvreader:

        #Add one to lineCount for each row counted
        lineCount += 1

        #Add one to each candidate for each vote they get
        if row[2] == "Correy":
            CorreyVotes += 1

        elif row[2] == "Khan":
            KhanVotes += 1

        elif row[2] == "Li":
            LiVotes += 1

        elif row[2] == "O'Tooley":
            OTooleyVotes += 1

    #Calculate percent of votes each candidate recieved
    OWinPercent = round(OTooleyVotes / lineCount * 100, 3)
    LWinPercent = round(LiVotes / lineCount * 100, 3)
    CWinPercent = round(CorreyVotes / lineCount * 100, 3)
    KWinPercent = round(KhanVotes / lineCount * 100, 3)

#Set conditional to determine the winner
if OTooleyVotes > LiVotes and OTooleyVotes > CorreyVotes and OTooleyVotes > KhanVotes:
    Winner = "O'Tooley"

elif LiVotes > OTooleyVotes and LiVotes > CorreyVotes and LiVotes > KhanVotes:
    Winner = "Li"

elif CorreyVotes > OTooleyVotes and CorreyVotes > LiVotes and CorreyVotes > KhanVotes:
    Winner = "Correy"

elif KhanVotes > OTooleyVotes and KhanVotes > CorreyVotes and KhanVotes > LiVotes:
    Winner = "Khan"

#Print results
print("Election Results")
print("------------------------")
print(f"Total Vote Count: {lineCount}")
print("------------------------")
print(f"O'Tooley: {OWinPercent}% ({OTooleyVotes})")
print(f"Khan: {KWinPercent}% ({KhanVotes})")
print(f"Correy: {CWinPercent}% ({CorreyVotes})")
print(f"Li: {LWinPercent}% ({LiVotes})")
print("------------------------")
print(f"Winner: {Winner}")
print("------------------------")


# Specify the file to write to
output_path = os.path.join("PyPoll/Resources/new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the results
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(["Total Votes:", lineCount])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(["O'Tooley:", OWinPercent , OTooleyVotes])
    csvwriter.writerow(["Li:", LWinPercent , LiVotes])
    csvwriter.writerow(["Khan:", KWinPercent , KhanVotes])
    csvwriter.writerow(["Correy:", CWinPercent , KhanVotes])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(["Winner:", Winner])
    csvwriter.writerow(["--------------------"])