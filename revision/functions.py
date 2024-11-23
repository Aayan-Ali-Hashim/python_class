# print(bin(6))

# t = str(55)
# print(type(t))

# float()
# int()
# slice()

# function to add two numbers

def sum_num(num1,num2): 
    return num1+num2


# print(sum_num(4,8))

def evenorodd(num):
    if (num%2 == 0):
        return "even number"
    else:
        return "odd number"

# print(evenorodd(34))
# print(evenorodd(7))


def greeting(name):
    return f"Hi {name}, how are you?"


# print(greeting("Omer"))

def greetingwithoutname():
    return "Hi how may I help you?"

print(greetingwithoutname())