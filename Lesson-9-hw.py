# 1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 2. Person Class
from datetime import date
class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = date.fromisoformat(birthdate)

    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else 'Cannot divide by zero'

# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius ** 2
    def perimeter(self): return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

# 5. Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root: return Node(value)
            if value < root.value: root.left = _insert(root.left, value)
            else: root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root: return False
            if root.value == value: return True
            return _search(root.left, value) if value < root.value else _search(root.right, value)
        return _search(self.root, value)

# 6. Stack Data Structure
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def is_empty(self): return not self.items

# 7. Linked List Data Structure
class LinkedListNode:
    def __init__(self, data): self.data = data; self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key: self.head = temp.next; return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp: prev.next = temp.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print('None')

# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self): self.items = []
    def add_item(self, name, price): self.items.append((name, price))
    def remove_item(self, name): self.items = [item for item in self.items if item[0] != name]
    def total_price(self): return sum(price for _, price in self.items)

# 9. Stack with Display
class StackWithDisplay:
    def __init__(self): self.stack = []
    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else None
    def display(self): print(self.stack)

# 10. Queue Data Structure
class Queue:
    def __init__(self): self.queue = []
    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.pop(0) if self.queue else None

# 11. Bank Class
class Bank:
    def __init__(self): self.accounts = {}

    def create_account(self, name, balance=0):
        if name not in self.accounts:
            self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def get_balance(self, name):
        return self.accounts.get(name, "Account not found")
