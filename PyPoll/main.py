import os
import csv
import sys

os.getcwd

csvpath = os.path.join(".",'Resources', 'election_data.csv')
#filename = "election_data.csv"

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    vote_count = 0
    Candidates = []
    #create vote counts for each candidate and set starting valued to zero
    votes_Khan = 0
    votes_Correy = 0
    votes_Li = 0
    votes_Otooley = 0
    Winner = 0
    #allow for header row in csv file
    header = next(csvreader)
    
    #create for loop to tally votes for each candidate
    for row in csvreader:
        vote_count=vote_count + 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
        if row[2] == "Khan":
            votes_Khan = votes_Khan + 1
        if row[2] == "Correy":
            votes_Correy = votes_Correy + 1
        if row[2] == "Li":
            votes_Li = votes_Li + 1
        if row[2] == "O'Tooley":
            votes_Otooley= votes_Otooley + 1
        
    #Calculate percentage of total votes for each candidate
    KhanPercentage = (votes_Khan)/(vote_count)*100
    CorreyPercentage = (votes_Correy)/(vote_count)*100
    LiPercentage = (votes_Li)/(vote_count)*100
    OtooleyPercentage = (votes_Otooley)/(vote_count)*100


    #Initially I was thinking I needed a dictionary for the winner part but I coudlnt figure out
    #how to make it work. Please let me know if there was an easier/quicker way to do things using
    #a dictionary
    candidate_dict= {(votes_Correy): "Correy", (votes_Khan): "Khan", (votes_Li): "Li", (votes_Otooley): "O'tooley"}

    #determine which candidate has the most amount of votes. Assign name of candidate to 
    #to the highest vote amount for printing
    if int(votes_Correy) > Winner:
        Winner = int(votes_Correy)
        WinnerP= 'Correy'
    
    if int(votes_Khan) > Winner:
        Winner = int(votes_Khan)
        WinnerP = 'Khan'

    if int(votes_Li) > Winner:
        Winner = int(votes_Li)
        WinnerP = "Li"
    
    if int(votes_Otooley) > Winner:
        Winner = int(votes_Otooley)
        WinnerP = "O'Tooley"

 
    #create variable for the output so it can be used to print in terminal and into .txt file.
    output = ("Election Results \n"
    "----------------------------\n"
    f'Total Votes: {vote_count}\n'
    "----------------------------\n"
    f'Khan: {KhanPercentage}%  ({votes_Correy})\n'
    f'Correy: {CorreyPercentage}%  ({votes_Khan})\n'
    f'Li: {LiPercentage}%  ({votes_Li})\n'
    f"O'Tooley: {OtooleyPercentage}%  ({votes_Otooley})\n"
    '-----------------------------\n' 
    f"{WinnerP} is your Winner!") 

    #print output to terminal
    print(output)

#create .txt file with same information as the terminal output (must import sys)
sys.stdout=open("main_Poll_output.txt","w")
print (output)
sys.stdout.close()