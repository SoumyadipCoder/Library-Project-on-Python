from animations.loading import pulse as loading

def studentsignup(gmail,password):
    from student.student_dash import student_main
    loading()
    print("Your library account is successfully created.")
    student_main(gmail)

