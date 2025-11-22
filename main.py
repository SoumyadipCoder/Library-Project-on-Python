from animations.heading import heading_box
from animations.loading import pulse as loading
from admin.auth_function import admin_signup
from student.auth_function import student_signup

def login():
    print("login")

def SignUp():
    print("SignUp")
    gmail=(input("Enter gmail:-")).strip()
    password=input("Enter password containing atleast 6 character:-")
    print("~"*15)
    loading()
    print("1. Signup\n2. Back")
    option=int(input("Enter your option:-"))
    if(option!=1):
       print("Go to main page")
       pass
    else:
        if(gmail.__contains__(".student@gmail.com")):
            student_signup(gmail=gmail,password=password)  
        elif(gmail.__contains__(".admin@gmail.com")):
            admin_signup(gmail=gmail,password=password) 
        else:
            print("Enter a valid gmail")
            SignUp()    


             



while True:
    print("="*45)
    heading_box("Children Library")
    print("="*45)
    print("1. Login")
    print("2. SignUp")
    print("3. Exit")
    print("-"*25)
    option = int(input("Enter option :- "))
    print("-"*25)
    loading()
    
    if(option == 1): login()
    elif(option == 2): SignUp()
    elif(option == 3):
        print("Thank you for choosing us ❤️  spirit up by learning 🚀")
        break
    else:
        print("Wrong option. Plz chose correct one.")
