import random

print("Random 0-1:", random.random())
print("Random integer 1-10:", random.randint(1, 10))

names = ["Ali", "Dana", "Arman", "Aruzhan"]
print("Random name:", random.choice(names))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)