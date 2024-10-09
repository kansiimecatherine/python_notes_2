# logical operators
# these are specific keywords in python that help us to connect and compare different conditions

#main logical operators
# and : both conditions must be true
# or: atleast one of the conditions must be true
# not: reverses the truth value of a condition

#example
x= True
y= False
print(x and y)#false
print(x or y)#true
print(not x)#false(negation)

#example two(practical)
#Wite a simple script that checks if a person can access a vip of a club based on their age,
# and their membership status
age = int(input("Enter the age:"))
is_member = input("Are you a club member? (yes/no):").lower() == 'yes'

if age >= 18 and is_member:
    print("Welcome to the VIP section!")
elif age >= 18 and not is_member:
    print("You need to be a club member to access the VIP section")
else:
    print("Sorry,you must be 18 or older to enter the VIP section")



