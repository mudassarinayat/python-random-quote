import random
from typing import TextIO

f: TextIO = open('quotes.txt')
quotes = f.readlines()
f.close()
print(quotes[0])

last = 13
rnd = random.randint(0, last)
last = len(quotes) - 1
print(quotes[rnd])
