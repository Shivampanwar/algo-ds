import time


def fibonacci1(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


def fibonacci2(n, array):
    if n == 1 or n == 0:
        return 1
    elif array[n] is not 0:
        return array[n]
    else:
        output = fibonacci2(n - 1, array) + fibonacci2(n - 2, array)
        array[n] = output
        return output


def fibonacifinal(n):
    array = []
    array.append(1)
    array.append(1)
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])
    output = array[n]
    del array
    return output


start = time.time()
a = fibonacci1(30)
end = time.time()
print ("Time taken to do without dp is {}".format(str(end - start)))
start = time.time()
array = []
for i in range(61):
    array.append(0)
a = fibonacci2(60, array)
end = time.time()
print ("Time taken to do with dp is {}".format(str(end - start)))
print fibonacifinal(5)
