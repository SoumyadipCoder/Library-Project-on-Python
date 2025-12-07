from animations.loading import pulse as loading

def studentsignup(gmail,password):
    from student.student_dash import student_main
    loading()
    name=input("Enter your name:-")
    id=int(input("Enter your library id:-"))
    print("Your library account is successfully created.")
    student_main(name,gmail,id)



