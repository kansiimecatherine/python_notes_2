# functions
# A function is a block of code that performs specific tasks or that runs when called.
#In functions we use (def) first which means define or definition

#Function calls: 

#keywords
#1. def
#2.pass: it is used when we don't have the function body

#Parameters: these are variables that are passed in the function or parentheses to perform a particular task
#Arguements: this is data or information that performs a specific task.(it is a value)

#Global variables:
marks = 99
print(marks)

# Local variables: are variables defined within the function body or scope

#examples
#1. create a function that returns the main components of functions.The output should say main components are
#parameters, and arguements

def function_basics():
    print("\nThe main components of a function are parameters,function body,and arguements "'\n\n')
function_basics()

#2. Create a function that returns your student name,regestration number and age.

def student_details(): 
    student_name = "KANSIIME CATHERINE" # This is a local variable
    reg_number = "2024/DSC/0038/SS" # This is a local variable
    student_age = 20 # This is a local variable
    print(f"\nThe student's name is {student_name} with regestration number {reg_number} and is {student_age} years old",'\n\n')
student_details()

#with parameters
#create a function that returns student's name regestration number and age as parameters.
#approach one
student_name = "KANSIIME CATHERINE"
reg_number = "2024/DSC/0038/SS"
student_age = 20 
def student_details_parameters(student_name,reg_number,student_age):
    print(f"\nThe student's name is {student_name} with regestration number {reg_number} and is {student_age} years a student at witu",'\n\n')
student_details_parameters(student_name,reg_number,student_age)

#approach two
def student_details_parameters(name,reg_number,age):
    print(f"\n The student's name is {name}, with reg_number {reg_number}, and is {age} years old")
student_details_parameters('Catherine','2024/DSC/0038/SS',20)










