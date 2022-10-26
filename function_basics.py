import math

def print_hello():
    """Print hello at screen"""
    print("Hello!")

def get_hello():
    """Return hello string
    :return Returns string value"""
    return "Hello"

def ask_name_and_greet_user():
    """
    Ask user name and print question with it.

    If name is Thanos print another text.
    """
    name = input("Insert your name please: ")
    name = name.capitalize()
    if name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name}. Would you like to have a hamburger")



def calculate_hypotenuse_length(a: int, b: int) -> float:
    """
    Calculate hypotenuse lenght
    :param a: Integer value
    :param b: Integer value
    :return: Float value = calculate lenght
    """
    c = math.sqrt(a ** 2 + b ** 2)
    return c

result = calculate_hypotenuse_length(3, 4)
print(result)


def calculate_cathetus_lenght(a, c):
    b = math.sqrt(c**2 - a**2)
    return b

result = calculate_cathetus_lenght(3, 5)
print(result)
  """
    Calculate cathehetus lenght. """
#ask_name_and_greet_user()
print_hello()
greeting = get_hello()
print(greeting)
