class Student:
    ...


def main():
    student=get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student=Student()
    student.name =input("Name: ")
    student.house=input("House: ")
    return student


def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ =="__main__":
    main()