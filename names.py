# name = input("whats ur name?")


# with open("names.txt","a") as file:
#     file.write(f"{name}\n")


# with open("names.txt","r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

