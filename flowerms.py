#flowershop management system
import datetime

flowers=[]
while True:
    print('''
1. Add Flower
2. Update Flower
3. Remove Flower
4. View All Flowers
5. Search Flower
6.view available flowers
7. Exit
    ''')
    choice=int(input("enter ur choice"))
    if choice==1:
          flower_name = input("Name of Flower: ")
          flower_qty = (input("Quantity of Flower: "))
          price = (input("price of Flower: "))
          pay = input("Modes of Payment: ")
          flower_sts=input('available or unavailable ')
        
          flowers.append({'flower_name': flower_name, 'flower_qty': flower_qty, 'price':price, 'pay': pay,'flower_sts': flower_sts})
    elif choice==2:
        flower_name = input("Name of Flower: ") 
        f=0
        for i in flowers:
                  if i['flower_name']==flower_name:
                      f=1
                      while True:
                        print('''
1.  update Quantity
2. update price
3.update Mode of Payment

4.updated flower_sts 
5. Exit
'''
)  
                        sub_choice = int(input("Enter Your updated choice: "))
                        if sub_choice == 1:
                            new_qty = int(input("Enter New Quantity: "))
                            i['flower_qty'] =new_qty
                        elif sub_choice == 2:
                             new_price = (input("Enter New price: "))
                             i['price'] =new_price
                        elif sub_choice== 3:
                             new_pay = input(" enter updated Modes of Payment: ")
                             i['pay'] =new_pay
                        elif sub_choice == 4:
                             new_sts = input(" enter updated sts of flower(available or unavailable): ")
                             i['flower_sts'] =new_sts
                        elif sub_choice==5:
                                 
                            break
                        else:
                            print("invalid choice")
        if f==0:
            print(' Not Found')
    elif choice==3:
         flower_name=input("Enter Name Of The flower :")
         f==0
         for i in flowers:
              if i['flower_name']==flower_name:
                    f=1
                    flowers.remove(i)
                  
         if f==0:
               print(" Not Found")
    elif choice==4:
                print('_'*30)
                print('{:<15} {:<10}  {:<20} {:<15}'.format('flower_name','flower_qty','price','flower_sts'))  
                print('_'*30)
                for i in flowers:
                     print('{:<15} {:<10}  {:<20} {:<15}'.format(i['flower_name'],i['flower_qty'],i['price'],i['flower_sts']))
    elif choice==5: 
         flower_search=input(" enter Name Of flower you want :")
         print('_'*30)
         print('{:<15} {:<10}  {:<20}'.format('flower_name','flower_qty','price','flower_sts'))  
         print('_'*30)
         for i in flowers:
               if i['flower_name']==flower_search:
              
                     print('{:<15} {:<10}  {:<20} {:<15}'.format(i['flower_name'],i['flower_qty'],i['price'],i['flower_sts']))
                     
               else:      
                     print(" Not Found")
    elif choice ==6:
          print('_'*30)
          print('{:<15} {:<10}  {:<20} {:<15}'.format('flower_name','flower_qty','price','flower_sts'))  
          print('_'*30)
          for i in flowers:
                if i['flower_sts']=='available':
                     print('{:<15} {:<10}  {:<20} {:<15}'.format(i['flower_name'],i['flower_qty'],i['price'],i['flower_sts']))
    elif choice==7:
                     break
    else:
                     print("invalid option")     
                                              
                            
                         
                                         
        