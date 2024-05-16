# everything can be define as procedure plus arguments
def f(func, *args):
    return func(*args)

# define primitive procedure
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    result = a / b
    if result.is_integer():
        return int(result)
    return a / b

# define primitive logical
def eq(a, b):
    return a == b

def gt(a, b):
    return a > b

def lt(a, b):
    return a < b

def f_or(a, b):
    return True if (a or b) else False

def f_and(a, b):
    return True if (a and b) else False

# define primitive display
def display(n):
    print(n, end="")

def newline():
    print()

# define primitive conditional

# define primitive let

### 2.1.1
### primitive pair object
class Cons:
    """
    primitive construct for pair in Lisp
    """
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def car(self):
        return self.a

    def cdr(self):
        return self.b

    def __str__(self):
        return f"({self.a} {self.b})"

def car(cons):
    return cons.car()

def cdr(cons):
    return cons.cdr()

def cons(a, b):
    return Cons(a, b)

### 2.2
### primitive list
def f_list(*args):
    args = list(args)
    if not args:
        return None
    first = args.pop(0)
    return cons(first, f_list(*args))

def null_list(the_list) -> bool:
    return True if not the_list else False

### primitive remainder
def remainder(num, divisor):
    return num % divisor

