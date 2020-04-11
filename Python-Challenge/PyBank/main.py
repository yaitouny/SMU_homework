import csv

budget_data = r"03-Python/Instructions/PyBank/Resources/budget_data.csv"

totalMonths = 0
netTotal = 0
averageChange = 0
changeList = []
change = 0

with open(budget_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ",")

	csv_header = next(csvfile)
	#print(f"Header: {csv_header}")

	for row in csv_reader:
		totalMonths += 1
		netTotal += float(row[1])

		changeList.append(row[1])
		for i in range(len(changeList) - 1):
			change = float(netTotal[i+1])-float(netTotal[i])
	
	print("\n")
	print("Financial Analysis")
	print("------------------------------------")
	print(f"Total Months: {totalMonths}")
	print(f"Total: ${netTotal}")
	#print(f"Average Change: ${averageChange}")
	print(change)