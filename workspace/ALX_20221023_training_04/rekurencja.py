# def foo(a):
#     print(a)
#     return foo(a + 1)
#
#
# foo(1)


#### RecursionError: maximum recursion depth exceeded while calling a Python object
#### -> zbyt duża ilość wykonanych rekurencji


#############################################################################
#############################################################################
#############################################################################

# def foo(a):
#     print(a)
#     if a == 100:
#         return a
#     return foo(a + 1)
#
#
# foo(1)


#############################################################################
#############################################################################
#############################################################################


def silnia(n):
    if n < 0:
        raise ValueError('n musi być większe od 0')
    if n == 0:
        return 1
    return n * silnia(n - 1)


# print(silnia(-5))  # ValueError: n musi być większe od 0
# print(silnia(-500), '\n')  #  ValueError: n musi być większe od 0
print(silnia(203), '-->> 203\n')
print(silnia(20), '-->> 20\n')
print(silnia(0), '-->> 0\n')
print(silnia(1), '-->> 1\n')
print(silnia(2), '-->> 2\n')
print(silnia(3), '-->> 3\n')
print(silnia(4), '-->> 4\n')
print(silnia(5), '-->> 5\n')
print(silnia(6), '-->> 6\n')
print(silnia(7), '-->> 7\n')
print(silnia(8), '-->> 8\n')
print(silnia(9), '-->> 9\n')

#############################################################################
#############################################################################
#############################################################################
