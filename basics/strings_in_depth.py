#1.strings are array like structured
# arrays in python are lists
# example
# marks=[90,60,70]#eg of a list in python (array)
# In arrays the first index must be 0
name="cathy"
print(name[0])
print(name[4])
#Looping through strings
#we loop through strings using a keyword "for"(for loop)
#example
for character in name:
    print(character)

address="kamokya"
for item in address:
    print(item)

#3.Slicing in strings
#This is the accessing of a range of a character in a string.
#examples
name="cathy"
print(name[1:3])#at
print(name[1:4])#ath
print(name[1:5])#athy
print(name[0:2])#ca

print(name[ :4])#cath(when you don't have the start index,the output given is based on the end index.)

message="hello"
print(message[0:3])

#negative indexing
message='hello'
print(message[-1])
print(message[-1:-5])
print(message[-1:-4])
print(message[-5:-3])
print(message[-4: ])#keep all the items after the start index.
print(message[4: ])

#4.f strings(formatted strings)
#for f strings we embedde variables in curly brackets while printing
#it automatically casts the variable values.
name="cathy"
age=21
weight= 58.4138#to reduce the decimals you use() 
print(f" my name is {name} and am {age} years old and i weigh {weight:.2f}")
total_cost=300000
print(f"A new car is at {total_cost:,}")

#string methods
#1.length #len()
#It is all about the number of characters.
name='cathy'
print(name)
print(len(name))

name="sarah"
print(name.upper)

address="from kamokya"
print(len(address))





       
