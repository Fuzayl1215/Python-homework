import json

# Task 1: Read and print student details
with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

import requests

# Task 2: Weather data for Tashkent
API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(f"City: {data['name']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Weather: {data['weather'][0]['description']}")

import json

def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)

def update_book(title, new_author):
    books = load_books()
    for book in books:
        if book["title"] == title:
            book["author"] = new_author
    save_books(books)

def delete_book(title):
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)

# Example usage:
add_book("New Book", "John Smith")
update_book("New Book", "Jane Doe")
delete_book("New Book")

import requests
import random

API_KEY = "your_omdb_api_key"  # Replace with your OMDB API key

def get_movie_by_genre(genre):
    # Randomly pick a popular movie keyword for variety
    keywords = ["love", "war", "space", "ghost", "city", "dream"]
    keyword = random.choice(keywords)
    
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={keyword}&type=movie"
    response = requests.get(url)
    data = response.json()
    
    if data.get("Search"):
        filtered = [movie for movie in data["Search"] if genre.lower() in movie.get("Title", "").lower()]
        if filtered:
            selected = random.choice(filtered)
            print(f"Recommended Movie: {selected['Title']} ({selected['Year']})")
        else:
            print("No matching movies found.")
    else:
        print("No movies found.")

# Example usage
get_movie_by_genre("comedy")
