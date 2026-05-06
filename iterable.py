#iterable
numbers =[1, 2, 3, 4, 5]

def square (x):

    return x ** 2

numbers_squared = map(square, numbers)
print (list (numbers_squared)) #[1, 4, 9, 16, 25]

#Lets apply it with a lambda function
numbers_squared = map(lambda x: x** 2, numbers)
print (list (numbers_squared)) #[1, 4, 9, 16, 25]

#[1, 4, 9, 16, 25) this format is List
#(1, 4, 9, 16, 25) this format is Tuple
#(1, 4, 9, 16, 25) Normal display
