import csv

budget_data = r"03-Python/Instructions/PyBank/Resources/budget_data.csv"

totalMonths = 0
netTotal = 0
averageChange = 0
newList = []
changeList = []


with open(budget_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ",")

	csv_header = next(csvfile)
	#print(f"Header: {csv_header}")

	for row in csv_reader:
		totalMonths += 1
		netTotal += int(row[1])
		#print(row)
		newList.append(row[1])

	
	for i in range(len(newList) -1):
		changeList.append(int(newList[i+1]) - int(newList[i]))
	averageChange = round(sum(changeList) / len(changeList), 2)
 
	
	print("\n")
	print("Financial Analysis")
	print("------------------------------------")
	print(f"Total Months: {totalMonths}")
	print(f"Total: ${netTotal}")
	print(f"Average Change: ${averageChange}")
	