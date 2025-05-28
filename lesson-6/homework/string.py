# HOMEWORK SOLUTIONS

# 1. Modify String with Underscores
def modify_string(txt):
    result = ""
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3 and i < len(txt) - 1:
            if txt[i] in 'aeiou' or (i + 1 < len(txt) and txt[i + 1] == '_'):
                count = 0
            else:
                result += '_'
                count = 0
        i += 1
    return result

print(modify_string("hello"))       # hel_lo
print(modify_string("assalom"))     # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

# 2. Integer Squares Exercise
n = int(input("Enter n: "))
for i in range(n):
    print(i ** 2)

# 3. Loop-Based Exercises
# 3.1 First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2 Print pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3.3 Sum of numbers from 1 to n
num = int(input("Enter number: "))
sum_total = sum(range(1, num + 1))
print("Sum is:", sum_total)

# 3.4 Multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

# 3.5 Display numbers from list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 < num < 200:
        print(num)

# 3.6 Count digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

# 3.7 Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# 3.8 Print list in reverse
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# 3.9 Numbers from -10 to -1
for i in range(-10, 0):
    print(i)

# 3.10 Done after loop
for i in range(5):
    print(i)
print("Done!")

# 3.11 Prime numbers in a range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 25 and 50:")
for i in range(25, 51):
    if is_prime(i):
        print(i)

# 3.12 Fibonacci up to 10 terms
n1, n2 = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2
print()

# 3.13 Factorial of a number
num = int(input("Enter number: "))
fact = 1
for i in range(2, num + 1):
    fact *= i
print(f"{num}! = {fact}")

# 4. Return Uncommon Elements
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for el in c1:
        if el not in c2:
            result.extend([el] * c1[el])
    for el in c2:
        if el not in c1:
            result.extend([el] * c2[el])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
