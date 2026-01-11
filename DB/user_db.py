import ast

def read_db(role:str = "student"):
    db_file = ''
    if role == "admin":
        db_file = 'admin_user_db.txt'
    else:
        db_file = 'stu_user_db.txt'
    with open (db_file, 'r') as db:
        return ast.Dict(db.read())

def write_db( data:dict, role:str = 'student'):
    db_file = ''
    if role == "admin":
        db_file = 'admin_user_db.txt'
    else:
        db_file = 'stu_user_db.txt'
    with open (db_file, 'w') as db:
        db.write(str(data))

#def find_db(email:str):
        



# def creat_entity():

