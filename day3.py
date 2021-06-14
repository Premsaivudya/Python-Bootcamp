from tkinter import *
import tkinter.messagebox
root =Tk()
root.title("Employee Registration Form")
root.geometry('700x400')
root.configure(background = "grey94")
label1=Label(root ,text= "Employee Registration Form ", font=("bold", 20)).grid(row =0, column=2)
Firstname = Label(root ,text = "First Name",width=20,font=("bold", 10)).grid(row = 1,column = 1)
LastName = Label(root ,text = "Last Name",width=20,font=("bold", 10)).grid(row = 2,column = 1)
Address = Label(root,text = "Address",width=20,font=("bold", 10)).grid(row = 3,column = 1)
City = Label(root ,text = "City",width=20,font=("bold", 10)).grid(row = 4,column = 1)
State= Label(root,text = "state",width=20,font=("bold", 10)).grid(row = 5,column = 1)
Country = Label(root ,text = "Country",width=20,font=("bold", 10)).grid(row = 7,column = 1)
list1 = ['India','Malaysia','Ireland','Switzerland','Australia','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=20)
c.set('Select your country')
droplist.grid(row = 7,column = 2)
Mobile = Label(root ,text = "Contact Number",width=20,font=("bold", 10)).grid(row = 8,column = 1)
Email = Label(root ,text = "Email Id",width=20,font=("bold", 10)).grid(row = 9,column = 1)
Gender =Label(root ,text = "Gender",width=20,font=("bold", 10)).grid(row = 10,column = 1)
var = IntVar()
Radiobutton(root, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
Dateofbirth =Label(root ,text = "Date Of Birth",width=20,font=("bold", 10)).grid(row = 11,column = 1)
var1 = IntVar()
var2 = IntVar()


Firstname1 = Entry(root).grid(row = 1,column = 2)
Lastname1 = Entry(root).grid(row = 2,column = 2)
Adderss1=Entry(root).grid(row = 3,column = 2)
city1=Entry(root).grid(row = 4,column = 2)
state1=Entry(root).grid(row = 5,column = 2)
Email1 = Entry(root).grid(row = 9,column = 2)
Mobile1 = Entry(root).grid(row = 8,column = 2)
Dateofbirth1 = Entry(root).grid(row = 11,column = 2)


def onClick():
    tkinter.messagebox.showinfo("Welcome", "Yor Details Submitted  Successfully !")


# Create a Button
Button(root, text="Submit", command=onClick,width=20,bg='red',fg='white').grid(row = 14,column = 2)


root.mainloop()