##################
# Python Functions
##################
def say_hello():
    print("Hello World")


say_hello()  # Hello World

##################
# Scope Example
##################
x = 10


def my_function():
    x = "Hello World"
    y = "foo bar"
    print(x)


my_function()  # Hello World
print(x)  # 10
print(y)  # NameError

##################
# Global Example
##################
x = 10


def my_function():
    global x
    x = "Hello World"
    y = "foo bar"
    print(x)


my_function()  # Hello World
print(x)  # Hello World


##################
# Parameters Example
##################
def my_function(parameter):
    print(f"Parameter set as -> {parameter}")


my_function("argument")


def new_function(p="Hello", q="!"):
    print(f"{p}{q}")


new_function()  # "Hello!"
new_function("World")  # World!


##################
# Keyword Arguments Example
##################
def named_arguments(a, b, c):
    print(f"{a}, {b}, {c}")


named_arguments(a="foo", b="bar", c="baz")  # foo, bar, baz

named_arguments(c="first", a="second", b="third")  # second, third, first
named_arguments(b="first", c="second", a="third")  # third, first, second


##################
# Argument Lists Example
##################
def args_list(*args):  # *args Common syntax Function accepts any number of arguments as a tuple
    for elm in args: print(elm)


args_list(1, 2)
args_list(10, 12, 15)


def named_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


named_args(a="hello", b=10, c=False)
named_args(username="Hello", password="World@1")
