class Student:
    def __init__(self,name,house):
        self.name=name# also calls setter
        self.house=house# calls setter
    #public and private instances work on the honor system
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name=input("Name:")
        house =input("House: ")
        return cls(name,house)
    

def main():
    student=Student.get()
    print(student)



if __name__ =="__main__":
    main()