from animations.heading import heading_box 


def profile(gmail):
    print("admin profile print")
    #print admin profile by gmail

def a_show_book():
    print("booklist")
    #print booklist from db 

def new_book_donate(id):
    while True:
        donator=input("Enter donator's name:-")
        donator_gmail=input("Enter donator's gmail:-")
        d_id=input("Enter donator's id:-")
        if (donator_gmail).endswith(".donator@gmail.com") and d_id.isdigit():break
        print("Wrong input data.")

def dash():
    print("-"*25)
    heading_box("Admin Dashboard")
    print("-"*24)
    print("1. Profile.")
    print("2. Admin show books..")
    print("3. New book donate.")
    print("4. Accept new requests.")
    print("5. Accept renew requests.")
    print("6. Accept return requests.")
    print("7. Send notification for delay.")
    print("8. logout.")
    print("-"*25)
    option = int(input("Enter option: "))
    return option

def admin_main(name,gmail,id):
    while True:
        option = dash()
        if option ==1:profile(gmail) 
        elif option ==2:a_show_book() 
        elif option==3:new_book_donate(id)  
        elif option==4:acc_new_req(id)
        elif option==5:acc_renew_req(id)
        elif option ==6:acc_return_req() 
        elif option ==7:delay_sms(name,gmail,id)  
        elif option == 8:break  
              
        else:
            print("Invalid input.Please chose the correct option.")    