import csv

budget_data = r"Python-Challenge/PyBank/budget_data.csv"

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
	
	print("Financial Analysis")
	print("------------------------------------")
	print(f"Total Months: {totalMonths}")
	print(f"Total: ${netTotal}")
	print(f"Average Change: ${averageChange}")
	print(f"Greatest Decrease in Profits: {bestMonth} (${maxIncrease})")
	print(f"Greatest Decrease in Profits: {worstMonth} (${minDecrease})")
	print("\n")



output = r"Python-Challenge/PyBank/Analysis summary.txt"
with open(output, "w") as file:

	
	file.write("Financial Analysis\n")
	file.write("------------------------------------\n")
	file.write(f"Total Months: {totalMonths}\n")
	file.write(f"Total: ${netTotal}\n")
	file.write(f"Average Change: ${averageChange}\n")
	file.write(f"Greatest Decrease in Profits: {bestMonth} (${maxIncrease})\n")
	file.write(f"Greatest Decrease in Profits: {worstMonth} (${minDecrease})\n")
	file.write("\n")