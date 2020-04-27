import csv 

election_data = r"Python-Challenge/PyPoll/election_data.csv"

voteCount = 0
candidates = []
names = []
vote1 = vote2 = vote3 = vote4 = 0
percentVote1 = percentVote2 = percentVote3 = percentVote4 = 0
winnerVote = 0

#open and read in the csv file 
with open(election_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")

	csv_header = next(csvfile)
	#print(csv_reader)

	for row in csv_reader:
		#find the total numbers of votes
		voteCount += 1
		candidates.append(row[2])

	for x in candidates:
		if x not in names:
			names.append(x)

	#calculate the percentages of votes of each candidate
	for i in range(len(candidates) - 1):
		if candidates[i] == names[0]:
			vote1 += 1
			percentVote1 = round(100 * vote1/len(candidates), 3)

		elif candidates[i] == names[1]:
			vote2 += 1
			percentVote2 = round(100 * vote2/len(candidates), 3)

		elif candidates[i] == names[2]:
			vote3 += 1
			percentVote3 = round(100 * vote3/len(candidates), 3)
		else:
			vote4 += 1
			percentVote4 = round(100 * vote4/len(candidates), 3)

	#finding the name of candidates with max votes 
	if percentVote1 > winnerVote:
		winnerVote = percentVote1
		winnerName = names[0]

	if percentVote2 > winnerVote:
		winnerVote = percentVote2
		winnerName = names[1]
	
	if percentVote3 > winnerVote:
		winnerVote = percentVote3
		winnerName = names[2]

	if percentVote4 > winnerVote:
		winnerVote = percentVote4
		winnerName = names[3]

	#print statements
	print("Election Results")
	print("-------------------------------")
	print(f"Total Votes: {voteCount}")
	print("-------------------------------")
	#print(*names , sep = ":\n")
	print(f"{names[0]}: {percentVote1}% ({vote1})")
	print(f"{names[1]}: {percentVote2}% ({vote2})")
	print(f"{names[2]}: {percentVote3}% ({vote3})")
	print(f"{names[3]}: {percentVote4}% ({vote4})")
	print("-------------------------------")
	print(f"Winner: {winnerName} ")
	print("-------------------------------")

#print output in a csv file
output = r"Python-Challenge/PyPoll/Election Data.csv"

with open(output, "w") as datafile:

	csvwriter = csv.writer(datafile)

	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-------------------------------'])
	csvwriter.writerow([f'Total Votes: {voteCount}'])
	csvwriter.writerow(['-------------------------------'])
	csvwriter.writerow([f'{names[0]}: {percentVote1}% ({vote1})'])
	csvwriter.writerow([f'{names[1]}: {percentVote2}% ({vote2})'])
	csvwriter.writerow([f'{names[2]}: {percentVote3}% ({vote3})'])
	csvwriter.writerow([f'{names[3]}: {percentVote4}% ({vote4})'])
	csvwriter.writerow(['-------------------------------'])
	csvwriter.writerow([f'Winner: {winnerName}'])
	csvwriter.writerow(['-------------------------------'])