import re

email = input("whats ur email?").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username,domain=email.split('@')

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")