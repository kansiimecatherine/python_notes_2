#WHAT ARE LISTS
# CRUD 
# U-update
# D-delete
# R-read

# In lists we use angle brackets[].
# Lists are used to store multiple values or items in a single variable
#X-TICS ARE:
# mutable
# Index

# Examples
student_names = ['Cathy','Golden','Mary','Valleria','Anatoraih']# string types(strings)
student_marks = [99,78,98,79,88] # int types(intergers)
data = ['cathy',90,'kamokya']#mixed types
#positive indexing
print(student_names[0]) # first item
print(student_names[1])# second item
print(student_names[2])#third item
print(student_names[3])#forth item
print(student_names[4]) # fifth item

# negative indexing
print(student_names[-5])
print(student_names[-4])
print(student_names[-3])
print(student_names[-2])
print(student_names[-1])

#at the end
student_names.append('Michelle') #adding a new item to the list
print(student_names)

 # the particular position
student_names.insert(2,'Faith')
print(f"\nThe updated list is {student_names}",'\n\n')

     #Assignment
#Given a sample list,student_names =["Sandra","Patricia","Phionah","Anitah"]
#and student_marks = [80,56,78,90]
#Print Patricia,faith,phionah and anitah
#Add masha at the forth position
#Update the name Phionah to Phionah Aladinah
# Display the length of the student's list
# Print all the student names using a for loop
# Calculate the total marks for the student marks variable and the answer is 304 