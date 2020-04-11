import csv

budget_data = r"03-Python/Instructions/PyBank/Resources/budget_data.csv"

totalMonths = 0
netTotal = 0
averageChange = 0
newList = []
changeList = []
maxIncrease = 0
minDecrease = 0


with open(budget_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ",")

	csv_header = next(csvfile)
	#print(f"Header: {csv_header}")

	for row in csv_reader:
		totalMonths += 1
		netTotal += int(row[1])
		newList.append(row[1])

		if int(row[1]) > maxIncrease:
			maxIncrease = int(row[1])
			bestMonth = row[0]

		elif int(row[1]) < minDecrease:
			minDecrease = int(row[1])
			worstMonth = row[0]
			

	for i in range(len(newList) - 1):
		changeList.append(int(newList[i+1]) - int(newList[i]))
	
	averageChange = round(sum(changeList) / len(changeList), 2)
 
	output = r"Python-Challenge/PyBank/Analysis summary.txt"
	f = open(output, "w")

	
	print("Financial Analysis",file = f)
	print("------------------------------------",file=f)
	print(f"Total Months: {totalMonths}",file=f)
	print(f"Total: ${netTotal}",file=f)
	print(f"Average Change: ${averageChange}",file=f)
	print(f"Greatest Decrease in Profits: {bestMonth} (${maxIncrease})",file=f)
	print(f"Greatest Decrease in Profits: {worstMonth} (${minDecrease})",file=f)
	print("\n",file=f)