# 1. 
# Original dictionary
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# Define a function to get value from item
def get_value(item):
    return item[1]

# Sort in ascending order
asc_sorted = dict(sorted(my_dict.items(), key=get_value))
print(asc_sorted)

# Sort in descending order
desc_sorted = dict(sorted(my_dict.items(), key=get_value, reverse=True))
print(desc_sorted)
# 2.

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)
# 3.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {**dic1, **dic2, **dic3}
print(merged)
# 4.

n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)
# 5.

squares = {x: x**2 for x in range(1, 16)}
print(squares)
# 6.

my_set = {1, 2, 3}
print(my_set)
# 7.

colors = {"red", "blue", "green"}

for color in colors:
    print(color)
# 8.

my_set = {1, 2, 3}
my_set
my_set.add(4)
my_set.update([5, 6])
print(my_set)
# 9.

my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)
# 10.

my_set = {1, 2, 3}

my_set.discard(2) 
my_set.discard(5)  

print(my_set)
