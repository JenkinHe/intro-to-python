import re

url = input("URL: ").strip()


# username= url.removeprefix("https://twitter.com/","")
# print(f"Username: {username}")

username=re.sub(r"^https?://twitter\.com/","",url)
print(f"Username: {username}")