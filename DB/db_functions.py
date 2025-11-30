import ast

def read_db(role:str ="student")->dict:
    db_file = ""
    if(role == "admin"):
        db_file = "C:/Users/subha/OneDrive/Desktop/Vai/Code/Python/Library-Project-on-Python/DB/admin_db.txt"
    else:
        db_file = "C:/Users/subha/OneDrive/Desktop/Vai/Code/Python/Library-Project-on-Python/DB/student_db.txt"
    with open (db_file, "r") as file:
        file_data = file.read()
        return ast.literal_eval(file_data)

def find_user_password(email:str, role:str = "student"):
    db_data = read_db(role)
    return db_data.get(email)

def create_user(email:str, password:str, role:str = "student"):
    db_data = read_db(role)
    db_data[email] = password
    db_file = ""
    if(role == "admin"):
        db_file = "C:/Users/subha/OneDrive/Desktop/Vai/Code/Python/Library-Project-on-Python/DB/admin_db.txt"
    else:
        db_file = "C:/Users/subha/OneDrive/Desktop/Vai/Code/Python/Library-Project-on-Python/DB/student_db.txt"
    with open(db_file, 'w') as db:
        db.write(str(db_data))


create_user('sjnj', '3382')