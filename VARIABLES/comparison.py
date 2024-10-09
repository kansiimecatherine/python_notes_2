  #stored user credentials
username ="catherine"
password = "cathie12"
#user input
inputted_username =input("Enter your username:")
inputted_password =input("Enter your password:")
#validating login credentials
if inputted_username == username and inputted_password == password:
    print("Login was successfully!")
elif inputted_username != username:
    print("Login failed,invalid username")
else:
    print("Login failed,invalid password")  