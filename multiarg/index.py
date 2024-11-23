# calculate the avg of numbers

# def avg_num(num1,num2,num3):
#     return num1+num2+num3/3

# print(avg_num(3,4,1))

def avg_num(*args):
    sum = 0
    for i in args:
        sum = i + sum
        
    return sum/len(args)

print(round(avg_num(6,2,3),1))


# nums = [4,8,1]
# sum= 0 
# for i in nums:
#     sum = i + sum 
# print(sum)


