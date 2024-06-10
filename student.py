def main():
    student=get_student()
    if student["name"]=="Padma":
        student["house"]="RavenClaw"
    print(f"{student['name']} from {student['house']}")

def get_student():

    name=input("Name: ")
    house=input("House: ")
    return {"name":name,"house":house}


def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ =="__main__":
    main()