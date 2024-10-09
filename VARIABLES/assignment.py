      #ASSIGNMENT
#1. WE HAVE THE FOLLOWING STUDENTS DETAILS AND MARKS ENTER THESE DETAILS FROM THE KEYBOARD
# student name = Ritah Liz 
# student number = SEP23/BCS/14
# Programming = 78
# Data science = 89
# Computer applications = 55
#calculate the average mark and print the answer in three decimal places.
        #solution
#while working with a keyboard you use the input function

student_name =input("Enter the student name:  ")
student_number =input("Enter the student number:\t")
programming = int(input("Enter the programming mark:\t"))
data_science = int(input("Enter the data science mark:\t"))
computer_applications =int(input("Enter the computer application mark:\t"))
total_marks = programming + data_science + computer_applications
total_number_of_subjects = 3
average_mark = total_marks/total_number_of_subjects
# or average_mark = (programming + data_science + computer_applications)/3 
print(f"The average mark of {student_name} number {student_number} is : {average_mark:.3f}")
#OR print(f"{average:.3f})
#average = round((total_marks/total_number_of_subjects),3)
#print(f"The average mark of {student_name} number {student_number} is : {average}")


#2. write a program that converts the celsius temperature to Fahrenheit,
#  the program should ask the user to enter the temperature in celsius degrees
#  then display the temperature converted to F degrees.

celsius = int(input("\nEnter temperature in celsius degrees:"))
fahrenheit = (1.8*celsius) + 32    
#print(str(celsius) +" degree celsius is equal to " + str(fahrenheit) + "degrees fahrenheit",end='\n\n')
#or
#print(f"{celsius} degree celsius is equal to {fahrenheit} degree fahrenheit",end='\n\n')
#or
print(f"The temperature {celsius} in degrees celsius is equal to : {fahrenheit} degrees fahrenheit")


#3. A car miles per gallon can be calculated with the following formula MPG = miles driven / gallons of gas used.
# write a program that asks the user for the number of miles driven and gallons used, 
# it should calculate the car's miles per gallons used and displays the results.
miles_driven = float(input("\nEnter the number of miles driven:  "))
gallons_of_gas_used = float(input("Enter gallons of gas used:  "))
MPG = miles_driven/gallons_of_gas_used
print("The Car's miles per gallons used are =", MPG,end="\n\n")  