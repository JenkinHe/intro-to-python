import sys

if len(sys.argv)<2:
    sys.exit("too few args")
# elif len(sys.argv)>2:
#     sys.exit("too many args")

# print("Hello my name is",argv[1])

for arg in sys.argv[1:]:
    print("hello, my name is",arg)