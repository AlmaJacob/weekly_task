emp = []

def login():
    username = input("Enter your Username :")
    password = input("Enter your Password :")
    f = 0
    user = ''
    if username == "admin"and password == 'admin':
        f = 1
        print("Login successfully")
    for i in emp:
        if i['id'] == username and i['password'] == password:
            f = 2
            user = i
    return f, user