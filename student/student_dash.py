from animations.heading import heading_box 
from student.student_signup import studentsignup

def dash():
    print("-"*25)
    heading_box("Student Dashboard")
    print("-"*24)
    print("1. Show all books.")
    print("2. Profile.")
    print("3. logout.")
    print("-"*25)
    option = int(input("Enter option: "))
    return option

def student_main(name,gmail,id):
    while True:
        option = dash()
        if option == 3:
            break
        elif option ==1:
            booklist_histoy() 
        elif option ==2:
            profile(name,gmail,id)  
        else:
            print("Invalid input.Please chose the correct option.")     



def profile(name,gmail,password):
     
    print("Profile.")
    # print profile from DB
    s_dash_board(gmail,id) 

   

def booklist():
    print("1. 'Physics' ->H.C.Bharma")
    print("2. 'Maths' ->R.D.Sharma")
    print("3. 'Biology' ->S.P.Mandal")
    print("4. 'Chemistry' ->PW Module") 
    #print booklist DB


    
def booklist_histoy():
    print("bookllist_histoy")
    # print bookllist_histoy from DB

def s_dash_board(gmail,id):
    print("1.Book Request.")
    print("2. Show Books.")
    print("3. Renew Book.")
    print("4. Return Book.")

    op=int(input("Enter option:-"))
    if (op==1): book_req(gmail,id)
    elif (op==2): booklist()
    elif (op==3):renew_book(gmail,id)
    elif (op==4):return_book(gmail,id)
    else :
        print("Invalid input.Please choose the correct option.")
        s_dash_board()

def book_req(gmail,id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully registered.Keep learning.")

def renew_book(gmail,id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully renewed.Keep learning.")

def return_book(gmail,id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully returned.Have a good day.")   

