def multiply(a, b):
    if b == 1:
        return a
    else:
        small_output = multiply(a, b - 1)
        return a + small_output


print multiply(4, 7)
