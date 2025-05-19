# 1.

name = input("Fuzayl: ")
birth_year = int(input("2006: "))
current_year = 2025
age = current_year - birth_year
print(f"{name}, you are {age} years old.")
# 2.

txt = 'LMaasleitbtui'
car_name = txt[1:12:2]
print(car_name)
# 3.

txt = 'MsaatmiazD'
car_name = txt[0:9:2]
print(car_name)
# 4. 

txt = "I'am John. I am from London"
start = txt.find("from")
residence = txt[start + 5:]
print(residence)
# 5.

text = input("Barcelona")
reversed_text = text[::-1]
print(reversed_text)
# 6.

text = input("Barcelona").lower()
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print(count)
# 7.

numbers = list(map(int, input("1, 6, 9, 4, 5, 2, 7").split()))
print(max(numbers))
# 8.

word = input("kiyik")
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
# 9.

email = input("barcelona1899@gmail.com")
domain = email.split('@')[-1]
print(domain)
# 10.

import random
import string

length = int(input("10"))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)
