class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["G","H","R","S"]:
            raise ValueError("Invalid House")
        self.name=name
        self.house=house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse"
            case "Otter":
                return "Otter"
            case "Jack Russell Terrier":
                return "Dog"
            case _:
                return "Smoke"


def main():
    student=get_student()
    print(student.charm())

def get_student():

    name =input("Name: ")
    house=input("House: ")
    patronus = input("Patronus: ")
    return Student(name,house,patronus)


def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ =="__main__":
    main()