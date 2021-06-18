#Q1
def number():
    a=int(input("Enter 1st Number "))
    b=int(input("Enter 2nd Number "))
    print("Addition of two numbers is ",a+b)
    print("Subtraction of two numbers is ",a-b)
    print("Division of two numbers is ",a/b)
    print("Multiplication of two numbers is ",a*b)

number()

#Q2

print()
def covid(p_name,temp=98):
    print("pateint name : ",p_name)
    print("Body temperature : ",temp)
    print()
covid('John')
covid('Peter',102) 