a = [1,3,4,12,56,78,80] 
# '''What is a list?
# To store multiple values in a single variable '''
# # b = ["harry",12,"coding",17.9]

# #How to access list items?
# # print(b[0])
# # print(b[3])
# # print(len(b))
# # print(len(a))
# # print(type(b))

# # b = ["harry",12,"coding",17.9]
# # print(b[3])
# # print(b[-1])
# # list slicing
# # print(b[0:2])
# # print(b[0:3])
# # print(b[:3])
# # print(b[1:])
# #Changing list items 
b = ["harry",12,"coding",17.9]
# b[0] = "aayan"
# print(b)
# b.insert(1,50)
# print(b)
# b.remove(12)
# print(b)
# b.append(30)
# print(b)
print(b)
b.extend(a)
a.extend(b)
print(a)
print(b)


#Accessing elements of list
numbers = [23,78,45,90]
print(numbers[1])
a = numbers[3]
print(a)