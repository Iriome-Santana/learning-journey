import csv

"""Create a csv file"""
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["John", 30, "New York"])
    writer.writerow(["Jane", 25, "Los Angeles"])

"""Read a csv file"""
with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
"""Append a csv file"""
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Bob", 35, "Chicago"])

"""Read a csv file without header"""
with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row)

"""Read a csv file with header using DictReader"""
with open("data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        
"""Write a csv file rows using writerow"""
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["John", 30, "New York"])
    writer.writerow(["Jane", 25, "Los Angeles"])
    writer.writerow(["Bob", 35, "Chicago"])

"""Write a csv file rows using DictWriter"""
fieldnames = ["name", "age", "city"]
with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "John", "age": 30, "city": "New York"})
    writer.writerow({"name": "Jane", "age": 25, "city": "Los Angeles"})
    writer.writerow({"name": "Bob", "age": 35, "city": "Chicago"})


"""Read a csv file with header using DictReader and append to a list"""
personas = []

with open("data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        personas.append(row)
        
print(personas)
