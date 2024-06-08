def main():
    get_int()



def get_int():
    while True:
        try:
            x = int(input("whats x?"))
        except ValueError:
            print("not integer")
        else:
            print (f"x is {x}")
            break

main()