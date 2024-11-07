# Range function (range())
# PARAMETER VALUES
# range(start,stop,step)

#syntax
# using a loop print all numbers from 0 to 6
#by default a range has a start and to know the stop parameter you just update it by adding 1(+1)

# numbers = range(7)
# for number in numbers:
#     print(number) 

# for num in range(7):
#     print(num)  

# # number two
# for n in range(11):# numbers from 1 to 10
#     print(n)

# #number three
# for i in range(1,21): # numbers from 1 to 20
#     print(i)  

#print the following range of even numbers.
#(2,4,6,8,10)

def even_number():
    for even in range(2,11,2): # the minimum step should always be 1
        print(even)   
even_number()

# odd numbers (0,3,5,7,9)
def odd_numbers():
    for odd in range(0,10,2): # the minimum step should always be 1
        print(odd)   
odd_numbers()



