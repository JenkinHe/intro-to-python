class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["G","H","R","S"]:
            raise ValueError("Invalid House")
        self.name=name
        self.house=house

    def __str__(self):
        return f"{self.name} from {self.house}"
    @property
    def house(self):
        return self.house
    
    @house.setter
    def house(self,house):
        if house not in ["G","H","R","S"]:
            raise ValueError("Invalid house")
        self.house=house
    

def main():
    student=get_student()
    print(student)

def get_student():

    name =input("Name: ")
    house=input("House: ")
    return Student(name,house)


def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ =="__main__":
    main()