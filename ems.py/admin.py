emp = [{'id':'2',"name":"alma","age":21,"salary":25000,"place":"ksrd","dob":"17/8/2003","password":"17/8/2003"}]

def add_emp():
    id = str(input("Enter Employee ID :"))
    f1 = 0
    for i in emp:
        if i['id'] == id:
            f1 = 1
            print(" ID already exists ") 
            return

    name = input("Enter Employee Name :")
    age = int(input("Enter Employee Age :"))
    salary = int(input("Enter Employee Salary :"))
    place = input("Enter Place :")
    dob = input("Enter Date Of Birth :")
    password = dob
    emp.append({'id': id, 'name': name, 'age': age, 'salary': salary, 'place': place, 'dob': dob, 'password': password})
    print("Employee added successfully")

def emp_update():
    id = str(input("Enter Employee ID :"))
    for i in emp:
        if i['id'] == id:
            name = input("Enter Employee Name :")
            age = int(input("Enter Employee Age :"))
            salary = float(input("Enter Employee Salary :"))
            place = input("Enter Place :")
            dob = input("Enter Date Of Birth :")
            i['name'] = name
            i['age'] = age
            i['salary'] = salary
            i['place'] = place
            i['dob'] = dob
            print("Employee updated successfully")
            return
    print(" Invalid ID ")

def delete_emp():
    id = str(input("Enter Employee ID :"))
    for i in emp:
        if i['id'] == id:
            emp.remove(i)
            print(" Employee deleted successfully ")
            return
    print("Invalid ID")

def view_profile(user):
    print('_' * 60)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name', 'Age', 'Salary', 'Place', 'DOB'))
    print('*' * 60)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(user['id'], user['name'], user['age'], user['salary'], user['place'], user['dob']))

def edit_profile(user):
    for i in emp:
        if i['id'] == user['id']:
            name = input("Enter Employee Name :")
            age = int(input("Enter Employee Age :"))
            place = input("Enter Place :")
            dob = input("Enter Date Of Birth :")
            i['name'] = name
            i['age'] = age
            i['place'] = place
            i['dob'] = dob
            print(" Profile updated successfully ")
            return
    print("Invalid ID")

def display_emp():
    print("employee details")
    print('_' * 60)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name', 'Age', 'Salary', 'Place', 'DOB'))
    print('*' * 60)
    for i in emp:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'], i['name'], i['age'], i['salary'], i['place'], i['dob']))
    print('_' * 60)