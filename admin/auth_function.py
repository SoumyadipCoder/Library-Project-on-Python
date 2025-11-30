from animations.loading import loading
from DB.db_functions import find_user_password, create_user
from admin.Dashboard import admin_dashboard

def admin_signup(password,gmail):
    loading()
    check_password = find_user_password(gmail, 'admin')
    print("Password", check_password)
    if check_password != None:
        print("-"*15)
        print("User already exist. Please login")
        pass
    else:
        create_user(gmail, password, 'admin')
        print("-"*15)
        print("User account created successfully 🎉.")
        admin_dashboard()
