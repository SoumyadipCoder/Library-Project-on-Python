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

def student_main(gmail):
    while True:
        option = dash()

        if option == 3:
            break
        elif option ==1:
            bookllist() 
        elif option ==2:
            profile(gmail)  
        else:
            print("Invalid input.Please chose the correct option.")     



def profile(name):
    print(f"Name:-{name}")
    print(f"Id:-{id} ")  
    print("4.Back to main page.")


def bookllist():
    print("1. 'Physics' ->H.C.Bharma")
    print("2. 'Maths' ->R.D.Sharma")
    print("3. 'Biology' ->S.P.Mandal")
    print("4. 'Chemistry' ->PW Module") 
