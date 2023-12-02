#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a = ()
    t_b = ()
    if len(tuple_a) < 2:
        t_a = tuple_a + (0, 0)
    else:
        t_a = tuple_a[:2]
    if len(tuple_b) < 2:
        t_b = tuple_b + (0, 0)
    else:
        t_b = tuple_b[:2]
    return t_a[0] + t_b[0], t_a[1] + t_b[1]
