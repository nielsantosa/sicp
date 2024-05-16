from primitive import (
    f,
    plus,
    minus,
    multiply,
    divide,
    eq,
    display,
    newline,
    cons,
    car,
    cdr,
    Cons,
    remainder,
)
from ch_1_2 import gcd

def numer(rat: Cons) -> int:
    return f(car, rat)

def denom(rat: Cons) -> int:
    return f(cdr, rat)

def make_rat(n: int, d: int) -> Cons:
    def find_gcd(n, d):
        return f(gcd, n, d)
    g = find_gcd(n, d)

    return cons(f(divide, n, g), f(divide, n, g))

def print_rat(rat: Cons) -> None:
    f(display, f(numer, rat))
    f(display, "/")
    f(display, f(denom, rat))
    f(display, "\n")

def add_rat(x: Cons, y: Cons) -> Cons:
    return (
        f(make_rat,
            f(plus,
                f(multiply, f(numer, x), f(denom, y)),
                f(multiply, f(numer, y), f(denom, x))
            ),
            f(multiply, f(denom, x), f(denom, y))
        )
    )

def sub_rat(x, y):
    return (
        f(make_rat,
            f(minus,
                f(multiply, f(numer, x), f(denom, y)),
                f(multiply, f(numer, y), f(denom, x))
            ),
            f(multiply, denom(x), denom(y))
        )
    )

def mul_rat(x, y):
    return (
        f(make_rat,
            f(multiply, f(numer, x), f(numer, y)),
            f(multiply, f(denom, x), f(denom, y))
        )
    )

def div_rat(x, y):
    return (
        f(make_rat,
            f(multiply, f(numer, x), f(denom, y)),
            f(multiply, f(denom, x), f(numer, y))
        )
    )

def eq_rat(x, y) -> bool:
    return (
        f(eq,
            f(multiply, f(numer, x), f(denom, y)),
            f(multiply, f(denom, x), f(numer, y))
        ))

def one_third():
    return f(make_rat, 1, 3)

"""
rat = f(make_rat, 2, 3)
rat2 = f(make_rat, 2, 3)
add_result = f(add_rat, rat, rat2)
sub_result = f(sub_rat, rat, rat2)
mul_result = f(mul_rat, rat, rat2)
div_result = f(div_rat, rat, rat2)
eq_result = f(eq_rat, rat, rat2)
f(print_rat, add_result)
f(print_rat, sub_result)
f(print_rat, mul_result)
f(print_rat, div_result)
f(display, eq_result)
f(newline)

f(print_rat, f(add_rat, f(one_third), f(one_third)))
"""

# Exercise 2.2
def make_point(x, y) -> Cons:
    return cons(x, y)

def x_point(point):
    return f(car, point)

def y_point(point):
    return f(cdr, point)

def print_point(point):
    f(display, "(")
    f(display, f(x_point, point))
    f(display, ", ")
    f(display, f(y_point, point))
    f(display, ")")
    f(newline)

def make_segment(start_segment, end_segment):
    return cons(start_segment, end_segment)

def print_segment(segment):
    f(display, "(")
    f(print_point, f(car, segment))
    f(display, ", ")
    f(print_point, f(cdr, segment))
    f(display, ")")
    f(newline)

def midpoint_segment(segment):
    return (
        f(make_point,
            f(divide, f(plus, f(x_point, f(car, segment)), f(x_point, f(cdr, segment))), 2),
            f(divide, f(plus, f(y_point, f(car, segment)), f(y_point, f(cdr, segment))), 2),
        )
    )

"""
start = f(make_point, 1, 2)
end = f(make_point, 3, 5)
f(print_point, start)
f(print_point, end)
segment = make_segment(start, end)
f(print_segment, segment)
f(print_point, f(midpoint_segment, segment))
"""

# 2.1.3 What is meant by data?
# Procedure as Object (MINDBLOWING)
def new_cons(x, y):
    def dispatch(m):
        if f(eq, m, 0):
            return x
        elif f(eq, m , 1):
            return y
        else:
            f(display, "ERROR Argument not 0 or 1 -- CONS")

    return dispatch

def new_car(z):
    return f(z, 0)

def new_cdr(z):
    return f(z, 1)

"""
z = f(new_cons, 2, 3)
x = f(new_car, z)
y = f(new_cdr, z)
print(z)
print(x)
print(y)
"""

# Exercise 2.4
def cons_3(x, y):
    return lambda m: f(m, x ,y)

def car_3(z):
    return f(z, lambda p, q: p)

"""
cons = f(cons_3, 2, 3)
car = f(car_3, cons)
print(cons)
print(car)
"""

# Exercise 2.6
### CHURCH NUMERALS -> THIS IS DED
def zero():
    return lambda f_n: lambda x: x
def add1(n):
    return lambda f_n: lambda x: f(f_n, f(f(n, f_n), x))

"""
add1 = add1(zero())
print(add1)
"""
