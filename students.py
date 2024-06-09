import csv

name = input("whats ur name?")
home = input("whats ur home?")

with open("students.csv","a",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})