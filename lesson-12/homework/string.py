import threading
from queue import Queue
import re
from collections import defaultdict


# Exercise 1: Prime Checker


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, output):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    output.extend(primes)

range_start = 1
range_end = 100
num_threads = 4
threads = []
results = []

chunk_size = (range_end - range_start) // num_threads
for i in range(num_threads):
    start = range_start + i * chunk_size
    end = start + chunk_size if i != num_threads - 1 else range_end
    t = threading.Thread(target=check_primes, args=(start, end, results))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Prime numbers:", sorted(results))


# Exercise 2: Threaded Word Count


def process_lines(lines, word_counts):
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_counts[word] += 1

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    counters = [defaultdict(int) for _ in range(num_threads)]

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Merge dictionaries
    final_count = defaultdict(int)
    for counter in counters:
        for word, count in counter.items():
            final_count[word] += count

    print("\nWord Occurrences:")
    for word, count in sorted(final_count.items()):
        print(f"{word}: {count}")



