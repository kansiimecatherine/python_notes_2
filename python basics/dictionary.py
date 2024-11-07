# dictinary
# It has key value pair.
#syntax
# keys can never be lists,sets,tuples but they can be of type int,float,string.

#syntax- creating a dictionary
student = {
    'name':'Gilian',
    'age':22,
    'location':'muyenga'
}
print(student)

#accessing the items in the student dictionary
print(student['name'])
print(student['age'])
print(student['location'])

#print the keys of the student dictionary
print(student.keys())

# print the length of the dictionary
print(f"The length of the dictionary  is {len(student)}")

# add a key contact to the student dictionary
student['contact'] = "0700864553"
print(f"\nThe updated dictionary is : {student}",'\n\n')

#update the name Gilian to Apio Gilian
student['name'] = "Apio Gilian"
print(f"\nThe updated dictionary with a changed name to apio gilian is {student}",'\n\n')

#print all the values of a dictionary.
print(f"\nThe values of the student dictionary are : {student.values()}",'\n\n')

# remove the items in a dictionary.
student.pop('name')
print(student)