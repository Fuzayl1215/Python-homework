## 1.

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example test
print(is_leap(2000))  # True
print(is_leap(1900))  # False
## 2.

n = int(input("Enter a number (1 to 100): "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
## 3.

def get_even_numbers_with_if_else(a, b):
    # Make sure a is smaller or equal to b
    if a > b:
        a, b = b, a

    result = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
    return result

# Example usage
print(get_even_numbers_with_if_else(3, 10))  # Output: [4, 6, 8, 10]
## 3(2)

def get_even_numbers_no_if(a, b):
    return list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1)))

# Example usage
print(get_even_numbers_no_if(3, 10))  # Output: [4, 6, 8, 10]
