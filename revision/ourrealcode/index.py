
def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if(num1 >= 1):
        return num1 / num2


# entry point of Python
if __name__ == "__main__":
    print(f"the sum of 2 and 4 is {addition(2,4)} ")
    print(f"the minus of 10 and 2 is {subtraction(10,2)}")
    print(f"the multiplication of 3 and 5 is {multiplication(3,5)}")
    print(f"the division of 9 and 3 is {division(9,3)} ")