# This is how to commit the code to GitHub
# git add . && git commit -m "Code update" && git push


def DisplayMenu():

    exit = False
    print("Welcome to the School ID System")
    print("-------------------------------")
    print("1. Get Student Details by ID")
    print("2. Print Report: List students by tutor group")
    print("3. Print Report: List students by year group")
    print("4. Print Report: List students by student address")
    print("5. Logout")

    choice = input("Please select an option (1-5): ")
    choice = int(choice)
 
    return choice

def login():
    
    success = False
    userName = input("Enter your username: ")
    password = input("Enter your password: ")

    if userName == "Leeman" and password == "password":
        print("Login successful!")
        success = True
    else:
        print("Login failed.")
        success = False

    return success

while not login():
    print("Please try again.")

while DisplayMenu() != 5:
    pass

print("You have logged out successfully. Goodbye!")
