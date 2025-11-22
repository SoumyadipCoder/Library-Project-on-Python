from animations.heading import heading_box
from animations.loading import pulse as loading


def login():
    print("login")

def SignUp():
    print("SignUp")

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
    
    if(option == 1): login()
    elif(option == 2): SignUp()
    elif(option == 3):
        print("Thank you for choosing us ❤️  spirit up by learning 🚀")
        break
    else:
        print("Wrong option. Plz chose correct one.")
