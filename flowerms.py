#flowershop management system
import datetime
print(datetime.datetime.now().strftime("%x"))
flowers=[]
while True:
    print('''
1. Add Flower
2. Update Flower
3. Remove Flower
4. View All Flowers
5. Search Flower
6. Exit
    ''')
    choice=int(input("enter ur choice"))
    if choice==1:
          name = input("Name of Flower: ")
          qty = int(input("Quantity of Flower: "))
          price = (input("price of Flower: "))
          pay = input("Modes of Payment: ")
          date = datetime.datetime.now().strftime("%x")
          flowers.append({'name': name, 'qty': qty, 'price':price, 'pay': pay, 'date': date})
    elif choice==2:
        name = input("Name of Flower: ")
        f=0
        for i in flowers:
                  if i['name']==name:
                      f=1
                      while True:
                        print('''
1.  update Quantity
2. update price
3.update Mode of Payment
4. Exit
'''
)  
                        sub_choice = int(input("Enter Your updated choice: "))
                        if sub_choice == 1:
                                   new_qty = int(input("Enter New Quantity: "))
                                   flowers['qty'] = new_qty
                        elif sub_choice == 2:
                             new_price = (input("Enter New price: "))
                             flowers['price'] = new_price
                        elif sub_choice== 3:
                             new_pay = input(" enter updated Modes of Payment: ")
                             flowers['pay'] = new_pay
                        elif sub_choice == 4:
                            break
        if f==0:
            print('Flower Name Not Found')
    elif choice==3:
         name=input("Enter Name Of The Product :")
         f==0
         for i in flowers:
              if i['name']==name:
                   flowers.remove(i)
                   f=1
              if f==0:
                      print("Product Name Not Found")
    elif choice==4:
                print('{:<10} {:<5}{:<10}'.format('name','qty','price','date'))  
                print('_'*30)
                for i in flowers:
                     print('{:<10} {:<5}{:<10}'.format(i['name'],i['qty'],i['price'],i['date']))
    elif choice==5:
         name=input("Name Of flower :")
         f=0
         for i in flowers:
              if i['name']==name:
                    print(i)
                    f=1
              if f==0:
                     print("flower Name Not Found")
    elif choice ==6:
        break
    else:
        print("invalid choice")                                        
                            
                         
                                         
        