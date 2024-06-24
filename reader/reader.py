import json
import csv
from files import *

book_file = get_path(filename='books.csv')
user_file = get_path(filename='users.json')


def distribute_books(users, books):
    book_count = len(books)
    if book_count % len(users) == 0:
        books_per_user = book_count // len(users)
    else:
        books_per_user = book_count // len(users) + 1

    for user in users:
        user['books'] = books[:books_per_user]
        books = books[books_per_user:]

    return users


with open(user_file) as f:
    users = json.load(f)

with open(book_file) as f:
    books = []
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        book = {
            'title': row['Title'],
            'author': row['Author'],
            'genre': row['Genre'],
            'pages': int(row['Pages']),
            'publisher': row['Publisher']
        }
        books.append(book)

distributed_users = distribute_books(users, books)

with open('result.json', 'w') as f:
    json.dump(distributed_users, f, indent=4)
