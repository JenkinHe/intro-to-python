class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house


def main():
    student=get_student()
    print(f"{student.name} from {student.house}")

def get_student():

    name =input("Name: ")
    house=input("House: ")
    student=Student(name,house)
    return student


def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ =="__main__":
    main()