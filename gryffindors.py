students =[
    {"name":"Hermoine","house":"G"},
    {"name":"Harry","house":"G"},
    {"name":"Ron","house":"G"},
    {"name":"Draco","house":"S"},
]

gryffindors =[
    student["name"] for student in students if student["house"]=="G"
]

for g in sorted(gryffindors):
    print(g)