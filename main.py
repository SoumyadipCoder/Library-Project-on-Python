from animations.heading import heading_box, heading_highlight
from animations.loading import pulse as loading
from admin.auth_function import admin_signup
from student.auth_function import student_signup

def login():
    gmail_=input("Enter gmail:-")
    password_=input("Enter password :-")
    if (((len(password_))>6) & ((gmail_.__contains__(".student@gmail.com")) | ((gmail_.__contains__(".admin@gmail.com"))))):
        
        loading()
        print("profile exists.")
    else :
        print("Invalid input. Please enter a valid input...")
        login()


def SignUp():
    heading_highlight("SignUp")
    gmail=(input("Enter gmail:-")).strip()
    password=input("Enter a strong password containing atleast 6 character:-")
    print("~"*15)
    loading()
    if len(password)>6 and (gmail.__contains__(".student@gmail.com") or gmail.__contains__(".admin@gmail.com")):
        print("1. Signup\n2. Back")
        print("-"*15)
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
        print("Invalid inputs. Please enter a valid input.")
        print("~"*15)
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
    
    if(option == 1): 
        login()
    elif(option == 2): 
        SignUp()
    elif(option == 3):
        print("Thank you for choosing us ❤️  spirit up by learning 🚀")
        break
    else:
        print("Wrong option. Plz chose correct one.")
