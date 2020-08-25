
# Example 1:
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest."

def greet_bob(greeter_func):
    return greeter_func("Bob")

# Example 2:

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() func.")

    def second_child():
        print("Printing from the second_child() func.")

    second_child()
    first_child()

# Example 3:

def parent_(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

# Simple decorator:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the func is called.")
        func()
        print("Something is happening after the func is called.")
    return wrapper

def say_whee():
    print("WHEE!")

say_whee = my_decorator(say_whee)

# Example 4

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("Sssssshhhhh! ")
    return wrapper


def say_whee2():
    print("WHEE!")

say_whee2 = not_during_the_night(say_whee2)

# To convert to pie format:

@not_during_the_night
def say_whee2():
    print("Whee!")



if __name__ == "__main__":
    # Example 1
    #print(greet_bob(say_hello))
    #print(greet_bob(be_awesome))

    # Example 2
    #parent()

    # Example 3
    #first = parent_(1)
    #second = parent_(2)
    #print(first)
    #print(second)
    #print(first())
    #print(second())

    #Simple decorator
    #say_whee()
    #print(say_whee)

    # Another example
    print(say_whee2)
    say_whee2()