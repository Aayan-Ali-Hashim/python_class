# 90 - 100 A+ grade
# 80 - 90 A grade
# 70 - 80 B grade
# 60 - 70 C grade
# less than 60 fail

marks = int(input("Enter your marks"))
if(marks >= 90 and marks<=100):
    print("Your grade is A+")
elif(marks>=80 and marks<=90):
    print("Your grade is A")
elif(marks >= 70 and marks<=80):
    print("Your grade is B")
elif(marks>=60 and marks<=70):
    print("Your grade is C")
elif(marks<60):
    print("You are fail")
else:
    print("Input valid marks")

