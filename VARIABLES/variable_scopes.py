#GLOBAL SCOPES

#1.Global variables
#These are varibles that are declared outside of any function and can be accessed throughout your entire program
#example
student_name="catherine" #global comment
print(student_name)

#Local variables
#These are variables that are declared inside a function and can only be accessed within that function.
#example
def student_details():
    student_age=21

    print(f"{student_name}{student_age}")

    student_details()