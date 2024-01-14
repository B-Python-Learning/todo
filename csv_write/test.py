import csv

lst = []
# Reading CSV file as a dictionary
with open('output_dict.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        lst.append(row)
    
# Writing CSV file using a dictionary
data_to_write = lst
# [
#     {'Name': 'John', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Alice', 'Age': 30, 'City': 'San Francisco'},
#     {'Name': 'Bob', 'Age': 22, 'City': 'Chicago'}
# ]

data_to_write.append(
    {
        'Name': input("Enter a name"),
        'Age': int(input("Enter your age")),
        'City': 'SG'
    }
)

# WRITE THE ENTIRE FILE 
fieldnames = ['Name', 'Age', 'City']

with open('output_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_to_write)
