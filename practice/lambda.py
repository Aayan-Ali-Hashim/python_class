# def number_adder(a,b):
#     return a + b


# mysum = number_adder(2,5)

# print(mysum)


def myfunc(n):
  return lambda a : a * n

# n = 2
# a = 3


mydoubler = myfunc(2)

print(mydoubler(3))


