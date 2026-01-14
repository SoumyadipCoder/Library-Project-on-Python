from animations.heading import heading_box 


def booklist():
    print("1. 'Physics' ->H.C.Bharma")
    print("2. 'Maths' ->R.D.Sharma")
    print("3. 'Biology' ->S.P.Mandal")
    print("4. 'Chemistry' ->PW Module") 
    #print booklist DB

def profile(name,gmail,password):
    print("Profile.")
    # print profile from DB
    
def booklist_histoy():
    print("bookllist_histoy")
    # print bookllist_histoy from DB

def book_req(id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully registered.Keep learning.")

def renew_book(id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully renewed.Keep learning.")

def return_book(id):
    b_name=input("Enter book name:-")
    b_poet=input("Auther:-")
    b_code=input("Enter book code:-")
    #input data into profile DB
    print("Your book is successfully returned.Have a good day.")   


def dash():
    print("-"*25)
    heading_box("Student Dashboard")
    print("-"*24)
    print("1. Show all books.")
    print("2. Profile.")
    print("3. Book Request.")
    print("4. Renew Book.")
    print("5. Return Book.")
    print("6. logout.")

    print("-"*25)
    option = int(input("Enter option: "))
    return option

def student_main(name,gmail,id):
    while True:
        option = dash()
        if option == 6:break
        elif option ==1:booklist() 
        elif option ==2:profile(name,gmail,id)  
        elif (option==3):book_req(id)  
        elif (option==4):renew_book(id)
        elif (option==5):return_book(id)     
        else:
            print("Invalid input.Please chose the correct option.")    