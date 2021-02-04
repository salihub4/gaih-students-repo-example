print("Welcome to User Login Page")

username = "salih"
password = "abc123"

login_user = input("Please Enter Your Username:")
login_pass = input("Please Enter Your Password:")

if (login_user == username) and (login_pass != password):
        print("Password is wrong")
        
elif (login_user != username) and (login_pass == password):
        print("Username is wrong")
        
elif (login_user != username) and (login_pass != password):
        print("Check username and password incorrectly.")
else :
        print("Login to the system is successful...")