# Dictionary is ordered , changeable , and do not allow duplicate values

my_books = {                                                                                                                                                                                                                                                                 
    'book1':'Rich Dad Poor Dad',
    'book2':'Thinking grow rich',
    'book3':'Atomic Habits',
    'number':1,
    'isHepassed' : True
}
# cannot be accessed with index
# print(my_books['book3'])
# print(my_books.get('book1'))
print(my_books.keys())
print(my_books.values())

my_books['book1'] = 'Mind game'
# print(my_books)

my_books['grades'] = 'A'
# print(my_books)

print(my_books.items())
# print(my_books)