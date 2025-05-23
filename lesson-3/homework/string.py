# 1.

fruits = ['apple', 'banana', 'lemon', 'orange', 'strawbery']

print(fruits)

print(fruits[2])
# 2.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print(combined)
# 3.

list4 = [10, 20, 30, 40, 50, 60, 70]

first = list4[0]
middle = list4[3]
last = list4[-1]

new_list = [first, middle, last]

print(new_list)
# 4. 

list3 = ['Harry Potter', 'Sherlock Holmes', 'Pirates of  caribian', 'Now you see me', 'Kingsman']

tupled = tuple(list3)

print(tupled)
# 5.

list3 = ['Harry Potter', 'Sherlock Holmes', 'Pirates of  caribian', 'Now you see me', 'Kingsman']

if 'Kingsman' in list3:
    print("Yes, the element is in the list")
else:
    print("No, the element is not in the list")
  # 6.

numbers = [1, 2, 3]
duplicate = numbers * 2
print(duplicate)
# 7.

list4 = [10, 20, 30, 40, 50, 60, 70]
list4[0], list4[-1] = list4[-1], list4[0]
print(list4)
# 8.

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice = my_tuple[3:8]

print(slice)
# 9.

next_list = [1, 5, 1, 8, 9, 1]

counted = next_list.count(1)

print(counted)
# 10.

list4 = [10, 20, 30, 40, 50, 60, 70]

finding = list4.index(30)

print(finding)
# 11.

tuple1 = (9, 8, 7, 6)
tuple2 = (5, 4, 3, 2)

result = tuple1 + tuple2

print(result)
# 12.

my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print(len(my_list))
print(len(my_tuple))
# 13.

my_tuple = (5, 10, 15, 20, 25)
converted = list(my_tuple)
print(converted)
# 14.

numbers = (9, 2, 15, 6, 1)
print(max(numbers))
print(min(numbers))
# 15. 
 
words = ("apple", "banana", "cherry")
reversed_tuple = words[::-1]
print(reversed_tuple)
