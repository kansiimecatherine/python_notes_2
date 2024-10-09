#1. write the program that takes two numbers as input and displays their sum,difference,product and thier quotient.
#2. write a program that compares two integers and prints wheather the first number is greater than,less than or equal to the second number.
#3.write a program that checks if a given number is between 10 and 20 (20 is inclusive) using logical operators.
#4. write the program that prints the squares of all intergers from 1 to 10 using a for loop.

# solutions
#.no 1 # while printing a string in operations we have to cast or change the string to either int or float.
number_one=int(input("enter the first number:"))
number_two=int(input("enter the second number:"))
sum = number_one + number_two
print(f"The sum of{number_one} and {number_two} is : {sum}")
print("The sum is " + str(sum))

#difference
difference = number_two - number_one
print("The difference of two numbers is " + str(difference))

#product
product = number_one * number_two
print("The product of two numbers is " + str(product))

#quotient
quotient = number_two / number_one
print(f"The quotient of {number_one} and {number_two} is :{quotient}")

#modulus
modulus = number_two % number_one
print(f"The modulus of {number_one} and {number_two} is : {modulus}")

#floor division
floor_division = number_two // number_one
print(f"The floor division of {number_one} and {number_two} is : {floor_division}")

# Number two
#comparison operators(use the if)
if number_one > number_two :
    print(f"{number_one} is greater than {number_two} ")
elif number_one < number_two :
    print(f"{number_one} is greater than {number_two}")
else :
    print(f"They are equal")


   ###NUMBER THREE
    
given_number = int(input("Enter the given number:"))
if 10 < given_number <= 20 :
        print(f"{given_number} is between ")
else:
     print(f"{given_number} is not between")


     ###NUMBER FOUR 
for integers in range (1, 11):
     print(f"The square of {integers} is : {integers**2} ")
     # OR
#for k in range(1, 11): # same as 1,2,3,4,5,6,7,8,9,10
     # print(f"{integers}^2 = {integers**2}")
# OR
#for w in range(1, 11):
   #  square = w**2
   #  print(f"The square of {w} is : {square}") 
     

#write a simple program that asks the user for their total age, if the age is greater or equal to 18 print
#  " your an adult and qualified, else tell them your not qualified. 
age = int(input("Enter your age please:"))
if age >= 18:
     print("Your an adult")
else:
     print("You are not qualified.")


                   




