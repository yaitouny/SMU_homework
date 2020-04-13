import csv
import datetime

employee_data = r"Python-Challenge/PyBoss/employee_data.csv"
name = []
firstName = []
lastName = []
dateOfBirth = []
reformatted_date = []
ssn = []
hidden_ssn = []
states = []
empID = []

us_state_abbrev = {
	"Alabama": "AL",
	"Alaska": "AK",
	"Arizona": "AZ",
	"Arkansas": "AR",
	"California": "CA",
	"Colorado": "CO",
	"Connecticut": "CT",
	"Delaware": "DE",
	"Florida": "FL",
	"Georgia": "GA",
	"Hawaii": "HI",
	"Idaho": "ID",
	"Illinois": "IL",
	"Indiana": "IN",
	"Iowa": "IA",
	"Kansas": "KS",
	"Kentucky": "KY",
	"Louisiana": "LA",
	"Maine": "ME",
	"Maryland": "MD",
	"Massachusetts": "MA",
	"Michigan": "MI",
	"Minnesota": "MN",
	"Mississippi": "MS",
	"Missouri": "MO",
	"Montana": "MT",
	"Nebraska": "NE",
	"Nevada": "NV",
	"New Hampshire": "NH",
	"New Jersey": "NJ",
	"New Mexico": "NM",
	"New York": "NY",
	"North Carolina": "NC",
	"North Dakota": "ND",
	"Ohio": "OH",
	"Oklahoma": "OK",
	"Oregon": "OR",
	"Pennsylvania": "PA",
	"Rhode Island": "RI",
	"South Carolina": "SC",
	"South Dakota": "SD",
	"Tennessee": "TN",
	"Texas": "TX",
	"Utah": "UT",
	"Vermont": "VT",
	"Virginia": "VA",
	"Washington": "WA",
	"West Virginia": "WV",
	"Wisconsin": "WI",
	"Wyoming": "WY"
}


with open (employee_data) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")

	csv_header = next(csvfile)
	#print(f"Header: {csv_header}")

	for row in csv_reader:
		empID.append(row[0])

		name = row[1].split(" ")
		firstName.append(name[0])
		lastName.append(name[1])

		dateOfBirth = row[2]

		reformatted_date = datetime.datetime.strptime(dateOfBirth, '%Y-%m-%d').strftime('%m/%d/%y')

	
		ssn = row[3].split("-")
		hidden_ssn.append("***-**-" + ssn[2])
		#hidden_ssn = ssn.replace(ssn, "***-**",6)

		states.append(us_state_abbrev[row[4]])

cleaned_csv = zip(empID, firstName, lastName, reformatted_date, hidden_ssn, states)

output_path = r"Python-Challenge/PyBoss/output.csv"	

with open(output_path, 'w') as datafile:

	csvwriter = csv.writer(datafile)
	csvwriter.writerow(['Emp ID', ' First Name', ' Last Name', ' DOB', ' SSN', ' State'])
	csvwriter.writerows(cleaned_csv)