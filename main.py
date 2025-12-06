from animations.heading import heading_box, heading_highlight
from animations.loading import pulse as loading
from admin.admin_signup  import adminsignup as a_signup
from student.student_signup  import studentsignup as s_signup

def login():
    print("Login")
    gmail=input("Enter your gmail:-")
    password=input("Enter  password:-")
    loading()

    if gmail.endswith(".student@gmail.com") or gmail.endswith(".admin@gmail.com") and (len(password))>6:
        print("`"*40)
        print("hi")
    else: 
        print("Invalid input.Please enter the correct details.")
        login()




def signup():
    print("Sign Up")
    gmail=input("Enter your gmail:-")
    password=input("Enter a strong password containing atleast 6characters:-")

    if (gmail.__contains__(".admin@gmail.com")) and (len(password))>6: a_signup(gmail,password)
    elif (gmail.__contains__(".student@gmail.com"))and (len(password))>6: s_signup(gmail,password)   
    else: 
        print("Invalid input.Please enter the correct details.")
        signup()

while True:
    print("="*50)
    heading_box("Arjuna Library")
    print("="*45)
    print("       !! All power is within you. !!")
    print("  !!You can do anything and everything.!!")
    print("~"*45)
    print("\n1.Login.")
    print("2.Signup.")
    print("3.Exit.")
    op=int(input("Enter your option:-"))
    
    if (op==1):login()
    elif(op==2):signup()
    elif(op==3):
        print("Thank you.Have a nice day.")
    else:print("Invalid input.Chose the correct one.")

    break