'''
import requests


def username(username):
    response = requests.get("https://jsonplaceholder.typicode.com/users", params={'username': username})
    return response.json()[0]['id']


def post(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={'userId': user_id})
    return response.json()


def comments(post_id):
    response = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': post_id})
    return response.json()


name = input()
for i in post(username(name)):
    for j in comments(i['id']):
        print(j['email'])
'''

'''
from abc import ABC, abstractmethod


class Telegram:

    def __init__(self):
        self.__observers = set()

    def register(self, observer):
        self.__observers.add(observer)
        self.account(observer.name)
        self.notify_1(observer)

    def delete_acc(self, observer):
        self.__observers.remove(observer)
        self.admin_acc(observer.name)
        self.notify_2(observer)

    def notify_1(self, observer):
        observer.get_notification()

    def notify_2(self, observer):
        observer.delete_account()

    def admin_acc(self, name):
        print('{} удалил аккаунт'.format(name))

    def account(self, name):
        print('{} получил сообщение'.format(name))


class AbstractObserver(ABC):
    @abstractmethod
    def get_notification(self):
        pass


class Email(AbstractObserver):

    def __init__(self, name):
        self.name = name

    def get_notification(self):
        print('уведомление получено на email')

    def delete_account(self):
        print('email: аккаунт удалён ')


user_1 = Email('user_1')
user_2 = Email('user_2')
user_3 = Email('user_3')
user_4 = Email('user_4')

telegram_platform = Telegram()

telegram_platform.register(user_1)
telegram_platform.register(user_2)
telegram_platform.register(user_3)

telegram_platform.delete_acc(user_1)
'''
from threading import Thread
from time import sleep, time
from random import randint
from queue import Queue



if __name__ == '__main__':
    threads = [Thread(target=game, args=(person,)) for person in range(1, 21)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
