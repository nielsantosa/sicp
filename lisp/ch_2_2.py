from primitive import (
    f,
    cons,
    car,
    cdr,
    f_list,
    null_list,
    plus,
    multiply,
)

def length(the_list):
    if f(null_list, the_list):
        return 0
    else:
        return f(plus, 1, f(length, f(cdr, the_list)))

"""
l = f(f_list)
print(f(length, l))
"""

def append(list1, list2):
    if f(null_list, list1):
        return list2
    else:
        return f(cons, f(car, list1), f(append, f(cdr, list1), list2))

"""
list1 = f(f_list, 1, 4, 9, 16)
list2 = f(f_list, 1, 3, 5, 7)
result = f(append, list1, list2)
print(result)
"""

### Mapping over list
def scale_list(the_list, factor):
    if f(null_list, the_list):
        return
    else:
        return f(cons, f(multiply, f(car, the_list), factor),
                f(scale_list, f(cdr, the_list), factor))

"""
l = f(f_list, 1, 2, 3)
res = f(scale_list, l, 3)
print(res)
"""

# abstract this into map-proc
def map(proc, the_list):
    if f(null_list, the_list):
        return
    else:
        return (
            f(cons,
                f(proc, f(car, the_list)),
                f(map, proc, f(cdr, the_list))
            )
        )

def scale_list_new(the_list, factor):
    return f(map, lambda x: f(multiply, x, factor), the_list)

l = f(f_list, 1, 2, 3)
res = f(scale_list_new, l, 3)
print(res)
