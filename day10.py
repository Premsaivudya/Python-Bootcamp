#bank
class Bank:
      def __init__(self,n,m,balance=500.0) :
             self.accno=accno
             self.name=name
             self.balance =balance
      def deposit(self,amt):
            self.balance+=amt
            return self.balance
      def withdraw(self,amt) :
            if amt>self.balance :
                print('Balance amt is less,so cannot withdraw')
            else :
                self.balance-=amt
            return self.balance
accno=input('Enter  Acct no.:   ')
name=input('Enter name  :   ')
b=Bank(accno,name)
choice = 'yes'
while choice=='yes':
  print('d - deposit,  w- withdrawl ' )
  ch = input('Enter choice  :  ')
  if ch == 'd':
       amt = float(input('Enter amount to be deposited  :   ') )
       print('Balance amount  :  ',b.deposit(amt))
  else :
       amt = float(input('Enter amount to be withdrawn  :  '))
       print('Balance amount  :  ',b.withdraw(amt)  )
  choice= input('Do you  want to continue yes/no   :  ')

  #e-commerce
  #parent class
class Brands:              
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    #child class
class Products(Brands):       
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"
    
obj_1 = Products()          
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
print(obj_1.brand_name_3+" is an "+obj_1.prod_3)