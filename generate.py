import random

coin =random.choice(['h','t'])
print(coin)

number = random.randint(1,10)
print (number)

cards =["J","Q","K"]
random.shuffle(cards)
for card in cards:
    print(card)