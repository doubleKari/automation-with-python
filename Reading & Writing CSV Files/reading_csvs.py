import csv

with open("csv_file.txt", "r") as file:
    csv_content = csv.reader(file)
    
    for row in csv_content:
        name, phone, role = row

        print(f"Name: {name},Phone: {phone} Role: {role}")