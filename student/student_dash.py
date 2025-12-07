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
            bookllist() 
        elif option ==2:
            profile(name,gmail,id)  
        else:
            print("Invalid input.Please chose the correct option.")     



def profile(name,gmail,password):
    print(f"Name:-{name}")
    print(f"Id:-{id} ")  
    print("1.Request for book.")
    print("2.Return for book.")   
    print("3.Previous history.")        
    print("4.Back to main page.")

    op=0
    if op==1:
        requestBook()
    elif op==2:
        returnBook()
    elif op== 3:
        history()
    #elif op== 4:

    else:
        print("1223321")              


def bookllist():
    print("1. 'Physics' ->H.C.Bharma")
    print("2. 'Maths' ->R.D.Sharma")
    print("3. 'Biology' ->S.P.Mandal")
    print("4. 'Chemistry' ->PW Module") 
