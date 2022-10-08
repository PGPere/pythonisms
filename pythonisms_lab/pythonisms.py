from functools import wraps
from time import sleep, time
import time
import math


def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = '\033[1m' + "!!!!!! " + \
            return_val_from_undecorated_function.upper() + "!!!!!!" + '\033[0m'

        return emphasized

    return wrapper


def inspire(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "Love your family, work super hard, live your passion," + orig_val

    return wrapper


@emphasize
@inspire
def say(txt):
    return txt


def calculate_time(func):

    def inner1(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


@calculate_time
def factorial(num):

    time.sleep(2)
    print(math.factorial(num))


def average(x, y):
    return (x + y)/2


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance


def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)

    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)


class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            # [a,b,c] => [a] -> [b] -> [c] -> None
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):

        def value_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return value_generator()

    def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

    def __len__(self):
        # DANGER: not O(1) - better IRL to track a self.length
        return len(list(iter(self)))

    def __eq__(self, other):
        # consider https://docs.python.org/3/library/functools.html#functools.total_ordering for Data collections
        return list(self) == list(other)

    def __getitem__(self, index):

        # return list(self)[index]

        # IF you have an efficient way to track length then check here
        # if len(self):
        #     raise IndexError

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


if __name__ == "__main__":

    # foods = LinkedList(["apple", "banana", "cucumber"])

    # first_food = foods[0]

    # for food in foods:
    #     print(food)

    print('\033[1m' + 'Hello')
    print('\033[0m')

    print(say(' it is how I enjoy this world'))

    factorial(10)

    print(sqrt(1200))
