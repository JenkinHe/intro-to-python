students =[
    {"name":"Hermoine","house":"G"},
    {"name":"Harry","house":"G"},
    {"name":"Ron","house":"G"},
    {"name":"Draco","house":"S"},
]

def is_gryffindor(s):
    return s["house"]=="G"

gryffindors = filter(is_gryffindor,students)

for g in sorted(gryffindors,key=lambda s:s["name"]):
    print(g["name"])