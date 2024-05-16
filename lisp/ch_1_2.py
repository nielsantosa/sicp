from primitive import (
    f,
    eq,
)

def gcd(n1, n2):
    if f(eq, n2, 0):
        return n1
    else:
        return f(gcd, n2, f(remainder, n1, n2))
