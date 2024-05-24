import os
import csv
import json

FILES_PATH_DIR = os.path.join(os.path.abspath(".."), "data_files")
USERS_FILE = os.path.join(FILES_PATH_DIR, "users.json")
BOOKS_FILE = os.path.join(FILES_PATH_DIR, "books.csv")
RESULT_FILE = os.path.join(FILES_PATH_DIR, "result.json")


def get_required_data_from_dict(required: list, data: dict) -> dict:
    return {key.lower(): value for (key, value) in data.items() if key.lower() in required}


def get_books_from_file(file_name) -> list:
    required_fields = ["title", "author", "pages", "genre"]
    with open(file_name, "r") as f:
        return [get_required_data_from_dict(required_fields, b) for b in csv.DictReader(f)]


def get_users_from_file(file_name) -> list:
    required_fields = ["name", "gender", "address", "age"]
    with open(file_name) as f:
        return [get_required_data_from_dict(required_fields, u) for u in json.load(f)]


def added_books_to_users(books: list, users: list) -> list:
    user_counter = 0
    for book in books:
        users[user_counter]["books"].append(book)
        user_counter = user_counter + 1 if user_counter < len(users) - 1 else 0
    return users


def dump_data_to_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)
    pass


if __name__ == "__main__":
    users_list = [{**u, **{"books": []}} for u in get_users_from_file(USERS_FILE)]
    books_list = get_books_from_file(BOOKS_FILE)

    users_list = added_books_to_users(books_list, users_list)
    dump_data_to_json(users_list, RESULT_FILE)