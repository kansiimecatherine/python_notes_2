#LISTS                                #TUPLES
# 1.mutable                            1.immutable
# 2.indexed                            2.indexed
# 3.ordered                            3.ordered
# 4.[]                                 5.()          

#LISTS AND TUPLES
products = ['pen','pencil','book'] # a list

colors = ('red','green','pink')# a tuple
# questions.
                #LISTS
# Add rubber to the product list
products.append('rubber')
print(products)

# Inserting a ruler on the second position
products.insert(1,'ruler')
print(products)

# display the length 
length = len(products) #in length we embedde everthing inside the parantheses
print(f"The length of the list is : {length}")

          #TUPLES
# add purple
# we cannot modify items in a tuple but it can be modified by concatination.
# inorder to update a tuple you should first concat it or convert it to a list.

colors = ('red','green','pink')
new_colors = list(colors)
print(new_colors)
new_colors.append('purple')
print(new_colors)

colors = tuple(new_colors)

#example two
fruits = ('apple',)
print(fruits,type(fruits)) # the output type is a str without a comma but if you add a comma it becomes a tuple.