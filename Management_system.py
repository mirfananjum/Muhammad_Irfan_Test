import admin
import connection
import new_user



running=True
while running==True:
    
    print("....Select your role....\n..1: Admine....\n..2: company owner..\n..3: user..\n..0: stop..")
    select=int(input("enter your post:"))
    if select==1:
        user=input("enter your username")
        password=input("enter your password")
        if admin.authenticate(user,password)==True:
            print("you log in ")
            condition=True
            while condition==True:
                print("....1: create new company....\n....2: create owner table for company....0: stop operations....")
                choice=int(input("enter your choice"))
                if choice==1:
                    database_name = input("enter your company name")
                    new_user.create_database(database_name)
                elif choice == 0:
                    print("exit")
                    condition=False
                else:
                    condition=False

    elif select==2:
        password=input("enter your password")
        username=input("enter your username")
        if connection.login_owner(username,password)==True:
            print("owner log in")
            run=True
            while run==True:
                
                print("....1: create user account....\n....2: manage income....\n....3: manage reports....\n....0: stop operations....")
                    
                choice= int(input("enter your choice"))
                
                
                if choice == 1:
                    print("create_user_account")
                    user_name=input("enter user name")
                    user_password=input("enter user password")
                    user_email=input("enter user email")
                    connection.create_user(user_name,user_password,user_email)
                    
                elif choice == 2:
                    print("manage income")
                    runni=True
                    while runni==True:
                        print("....1: Create new income table....\n....2: insert data....\n....3: display income data....\n....0: exit")
                        choice=int(input("Enter your choice"))
                        if choice==1:
                            print("create new income table")
                            table_name = input("enter table name")
                            column_definitions = [
                                ("id", "INT PRIMARY KEY AUTO_INCREMENT"),
                                ("amount", "DECIMAL(10, 2) NOT NULL"),
                                ("created_date", "DATE")
                            
                            ]
                            connection.create_table(table_name,column_definitions)
                            
                        elif choice==2:
                            print("insert income")
                            data=[
                                (2034.00, "2024-11-01"),
                                (2512.00, "2023-05-12")
                                
                            ]
                            connection.insert_data(data)
        
                        elif choice==3:
                            print("display income data")
                            table = input("enter table name")
                            connection.display_data(table)
                        elif choice==0:
                            runni=False
                        else:
                            print("invalid choice")
                            runni=False    
                        
                elif choice == 3:
                    print("manage reports")
                    start_date = "2010-11-12"
                    end_date = "2024-11-01"
                    orders = connection.fetch_data_by_date_range(start_date, end_date)
                    for order in orders:
                        print(order)
                elif choice == 0:
                    print("exit")
                    run=False
                else:
                    print("invalid operation")
                    run=False
        else:
            print("no")
        
    elif select==3:
        password=input("enter your password")
        username=input("enter your username")
        if connection.login_user(username,password)==True:
            print("user log in")
            runn=True
            while runn==True:
                
                print("....1: display income data....\n....2: display report....0: exit")
                choice=int(input("Enter your choice"))
                if choice==1:
                    print("display income data")
                    table = input("enter table name")
                    connection.display_data(table)
                elif choice == 2:
                    print("display report")
                    start_date = "2010-11-12"
                    end_date = "2024-11-01"
                    orders = connection.fetch_data_by_date_range(start_date, end_date)
                    for order in orders:
                        print(order)
                elif choice==0:
                    print("exit")
                    runn=False
                else:
                    runn=False
                
        else:
            print("no")
       
    elif select==0:
        print("exit")
        running=False
    else:
        running=False