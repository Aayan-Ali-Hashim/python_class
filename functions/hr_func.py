# # print numbers from 1 to n
# n = int(input("Enter a number\n"))
# # start from 1 and stop at n
# print("The numbers are:")

# def concat(n):
#     a = []
#     for i in range(1,n+1):
#         a.append(str(i))
#     return "".join(a)



def concat(n):
    a = []
    for i in range(1,n+1):
        a.append(str(i))
    return a

print(concat(4))