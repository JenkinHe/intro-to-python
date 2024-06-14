class Student:
    def __init__(self,name,house):
        self.name=name# also calls setter
        self.house=house# calls setter
    #public and private instances work on the honor system
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["G","H","R","S"]:
            raise ValueError("Invalid house")
        self._house=house
    

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