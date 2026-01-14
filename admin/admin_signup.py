from animations.loading import pulse as loading
from admin.admin_dash import admin_main
def adminsignup(gmail,password):

    loading()
    name=input("Enter your name:-")
    id=int(input("Enter your library id:-"))
    print("Your library account is successfully created.")
    admin_main(name,gmail,id)