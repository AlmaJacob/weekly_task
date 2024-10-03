from user import login
from emp import add_emp, emp_update, delete_emp, view_profile, edit_profile, display_emp

while True:
    print("""
          1. Login
          2. Exit
          """)
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        f, user = login()
        # Admin login
        if f == 1:
            while True:
                print("""
                      1. Add Employee
                      2. Update Employee
                      3. Delete Employee 
                      4. Display Employee Details
                      5. Logout
                      """)

                sub_choice = int(input("Enter your choice: "))
                
                if sub_choice == 1:
                    add_emp()
                elif sub_choice == 2:
                    emp_update()
                elif sub_choice == 3:
                    delete_emp()
                elif sub_choice == 4:
                    display_emp()
                elif sub_choice == 5:
                    print("Log out")
                    break

        elif f == 0:
            print(" Invalid Username and Password ")
        # User login page
        elif f == 2:
            while True:
                if user['dob'] == user['password']:
                    print("Create a New Password")
                    password = input("Enter new Password: ")
                    user['password'] = password
                    print("Password changed successfully")
                else:
                    print("""
                        1. View Profile
                        2. Edit Profile
                        3. Logout
                        """)
                    sub_choice_user = int(input("Enter your choice: "))
                    
                    if  sub_choice_user == 1:
                        view_profile(user)
                    elif  sub_choice_user == 2:
                        edit_profile(user)
                    elif sub_choice_user == 3:
                        print("Log out")
                        break
    elif choice== 2:
        print("Exit")
        break
    else:
        print("Invalid choice")