from time import sleep
from random import randint

while True:
    name = int(randint(1, 3))
    sleep(1)
    if name == 1:
        print("()(()()")
    elif name == 2:
        print("HELLO WORLD!")
    else:
        print("???")
