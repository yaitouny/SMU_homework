import csv

election_data = r"03-Python/Instructions/PyPoll/Resources/election_data.csv"

voteCount = 0
candidates = []
names = set()

with open(election_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")

	csv_header = next(csvfile)
	print(csv_header)

	for row in csv_reader:
		voteCount += 1
		candidates.append(row[2])
	for x in candidates:
		names.add(x)
			

	
	print("Election Results")
	print("-------------------------------")
	print(f"Total Votes: {voteCount}")
	print("-------------------------------")
	print(*names, sep = "\n")