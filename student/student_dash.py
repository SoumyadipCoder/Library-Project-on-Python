from animations.heading import heading_box 


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


def student_main():
    while True:
        option = dash()
        if option == 3:
            break
