from django.db import models

import json


def _get_users():
    with open('main/db.json', 'r') as file:
        file = json.load(file)
    return file


def _write_to_db(db: list):
    with open('main/db.json', 'w') as file:
        new_db = json.dumps(db)
        file.write(new_db)


def search_user(username: str) -> bool | dict:
    file = _get_users()
    for user in file:
        if user['username'] == username:
            return user

    return False


def correct_password(user: dict, password) -> bool:
    if user['password'] == hash(password):
        return True

    return False


def add_user(username: str, password: int) -> None:
    list_user = _get_users()
    user = {"username": username, "password": hash(password), "tasks": []}
    list_user.append(user)

    _write_to_db(list_user)


def get_tasks(username: str) -> list:
    tasks = search_user(username)["tasks"]
    return tasks


def add_task(username: str, task: str) -> None:
    file = _get_users()

    for user in file:
        if user['username'] == username:
            user['tasks'].append(task)

            _write_to_db(file)
            break


def del_task(username: str, task: str) -> None:
    users = _get_users()

    for user in users:
        if user['username'] == username:
            user['tasks'].remove(task)
            _write_to_db(users)
            break
