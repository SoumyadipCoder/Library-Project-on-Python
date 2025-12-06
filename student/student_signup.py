from animations.loading import pulse as loading
from student.student_dash import student_main

def studentsignup(gmail,password):
    loading()
    name=input("Enter your name:-")
    id=int(input("Enter your library id:-"))
    print("Your library account is successfully created.")
    student_main()



