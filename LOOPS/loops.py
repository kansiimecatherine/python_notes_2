#LOOPS
   #for loops
# # This is used to iterate or loop through sequences like [lists,strings,sets,tuples,dictionary]

#examples(using for loops)
name = "kansiime"
for item in name:
    print(item)
    
#Looping through lists
#number two
marks = [60,70,80]
for mark in marks:
    print(mark)

#using the function
def total_marks():
    marks = [60,70,80]
    sum=0
    for mark in marks:
        sum+=mark
    print(f"The total mark is : {sum}",'\n\n')
total_marks()