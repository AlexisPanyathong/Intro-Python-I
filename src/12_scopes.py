# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12
# If it is not nested in Python3, then it is considered global
def change_x():
   global x
   x = 99 

change_x()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.
# If it is nested in Python3, then it is considered nonlocal
def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()