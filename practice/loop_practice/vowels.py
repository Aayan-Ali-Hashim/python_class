my_name = "Courtney Harris" # String that we will count the number of vowels in
vowels = "aeiouAEIOU"
count = 0 # initialization 
for char in my_name:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


