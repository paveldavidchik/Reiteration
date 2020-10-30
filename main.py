import random


n: int = 10
random_set = set()
number = random.randint(0, n)
while number not in random_set:
    random_set.add(number)
    number = random.randint(0, n)
print(len(random_set) + 1)
