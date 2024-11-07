#RETURN VALUES
#we use a return keyword instead of a print function.
#create a simple function that returns my name

#approach one
def my_name():
    return "Catherine"
my_name()
# To view the output
name = my_name()
print(name)


 #approach two
def my_name_approach2():
    name = "KANSIIME CATHERINE"
    return name
my_name_approach2()



def my_age():
    age = 21
    return age
print(f"My name is {my_name_approach2()} and i am {my_age()} years old ")

# or
def my_name_approach3(name):
    return name
my_name_approach3("Catherine")

        #QUESTION
# Create a function that calculates the area of a triangle the base and the height must be the function parameters
#approach one
def area_of_triangle(base,height):
    area =(1/2*base*height)
    print(f"\nThe area of a triangle with base {base} and height {height} is {area}",'\n\n')
area_of_triangle(2,3)

#approach two
#as an input function
base = int(input("\nEnter the base:   "))
height = int(input("Enter the height:  "))
def triangle_area(base,height):
    area = int(1/2*base*height)
    print(f"\nThe area of a triangle with base {base} and height {height} is {area}",'\n\n')
triangle_area(base,height)

#without parameters
def TriangleArea():
    base = int(input("\nEnter the base:   "))
    height = int(input("Enter the height:  "))
    area = int(1/2*base*height)
    print(f"\nThe area of a triangle with base {base} and height {height} is {area} ",'\n\n')
TriangleArea()




