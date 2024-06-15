students =[
    {"name":"Hermoine","house":"G"},
    {"name":"Harry","house":"G"},
    {"name":"Ron","house":"G"},
    {"name":"Draco","house":"S"},
    {"name":"Padma","house":"R"},
]

houses=set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)