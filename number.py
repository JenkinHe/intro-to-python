def main():
    get_int("whatss x?")



def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("not integer")
        else:
            print (f"x is {x}")
            break

main()