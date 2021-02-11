#The data we need to retrieve: 
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidate won 
#5. The winner of the election based on the popular vote 

#Add our dependencies. 
import csv
import os

# Assign a variable to load a file from a direct path. 
file_to_load = 'Resources/election_results.csv'
# Assign a variable to save the file given indirect access. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter 
total_votes = 0 
#Initialize candidate options and candidate votes 
candidate_options = []
#Declare an empty dictionary 
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read and print the header row
    headers = next(file_reader)
    #print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)

        #Add to the total vote count 
        total_votes +=1 

        #find all candidate names 
        candidate_name = row[2]

        #Make sure the same candidate isn't added multiple times. 
        if candidate_name not in candidate_options: 
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
       
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Determine winning vote count and candidate by: 
            # Determining if the votes/percentage are greater than 
            # the winning votes/percentage.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            winning_count = votes
            winning_percentage = vote_percentage
            # Setting the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    #print the total votes 
    #print(total_votes)

    #print the candidate list 
    #print(candidate_options)

    # Print the candidate vote dictionary.
    #print(candidate_votes)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the election\n"
    #"-------------------------\nArapahoe\nDenver\nJefferson")