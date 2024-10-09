#  # ASSIGNMENT OPERATORS
# #These are operators used to assign values to variables in python.
# #the most basic is equal sign '='

# #examples
# #basic assignment
# sum = 10
# total = 100

# #combined assignment operators
# # basic assignment operators
# x = 10 # assign 10 to x
# x += 5 # same as x = x + 5; x is now 15
# x -= 3 # same as x = x - 3; x is now 12
# x *= 2 # same as x = x * 2; x is now 24
# x /= 4 # same as x = x/4; x is now 6.0
# x %= 3 # same as x =x % 3;x is now 0.0
# x **= 2# same as x = x**2;x is now 0.0
# x //= 2 # same as x = x //2; x is now 0.0
# sum = sum + 20 #same as sum+=20 
# print(sum)

# #practical: total cost of poducts in a shopping cart.
# total_cost = 0
# laptop = 600000
# mouse = 50000
# keyboard = 100000

# total_cost += laptop
# total_cost += mouse
# total_cost += keyboard
# #print(f"The tota cost of the shopping cart is:UGX {total_cost: ,}")

# #using a list
# total_cost = 0
# prices = [laptop,mouse,keyboard]# [600000,50000,100000] #list
# for price in prices:
#     total_cost += price
#     print(f"The total cost of the shopping cart is:UGX {total_cost: ,}")

#classwork assignment operator example
sum = 6
sum+=5
print(sum)

#given that you have to products a mouse and a laptop such that the price of a laptop is 300000
#and the price of the mouse 50000. Use a for loop to find the toatl sum of the products.
total_sum = 0
mouse = 50000
laptop = 300000
price_list=[laptop,mouse]#a list uses angle brackets
for price in price_list:
    total_sum+=price
print(f"The total cost of the products is:{total_sum: ,}")
# when we are only interested in the total of the products
# we remove the identation(white space) in the loops,by clearing the space.