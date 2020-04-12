import csv

election_data = r"03-Python/Instructions/PyPoll/Resources/election_data.csv"

voteCount = 0
candidates = []
names = []
vote1 = vote2 = vote3 = vote4 = 0 
percentVote1 = percentVote2 = percentVote3 = percentVote4 = 0
winnerVote = 0

with open(election_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")

	csv_header = next(csvfile)
	print(csv_header)

	for row in csv_reader:
		voteCount += 1
		candidates.append(row[2])

	for x in candidates:
		if x not in names:
			names.append(x)

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

	output = r"Python-Challenge/PyPoll/Election summary.txt"
	f = open(output, "w")

	print("Election Results", file =f)
	print("-------------------------------", file =f)
	print(f"Total Votes: {voteCount}", file =f)
	print("-------------------------------", file =f)
	#print(*names , sep = ":\n")
	print(f"{names[0]}: {percentVote1}% ({vote1})", file =f)
	print(f"{names[1]}: {percentVote2}% ({vote2})", file =f)
	print(f"{names[2]}: {percentVote3}% ({vote3})", file =f)
	print(f"{names[3]}: {percentVote4}% ({vote4})", file =f)
	print("-------------------------------", file =f)
	print(f"Winner: {winnerName} ", file =f)
	print("-------------------------------", file =f)
