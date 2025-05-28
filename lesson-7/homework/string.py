## 1.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(4))  # False
print(is_prime(7))  # True
## 2.


def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total

# Test
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
## 3.

def powers_of_two(N):
    result = []
    power = 1
    while power * 2 <= N:
        power *= 2
        result.append(power)
    return result

# Test
print(powers_of_two(10))  # [2, 4, 8]
