# All numbers
import numpy as np

#numbers = np.random.randrange(1, 101, 5)

#print("Unsorted:", numbers)

#sorted_numbers = np.sort(numbers)

#print("Sorted:", sorted_numbers)



#Odd numbers
import random

numbers = []

for _ in range(10):
    numbers.append(random.randrange(0, 100, 2))

print("Unsorted:", numbers)

sorted_numbers = np.sort(numbers)

print("Sorted:", sorted_numbers)
