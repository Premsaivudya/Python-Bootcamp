#DAY 6
#Write a Python script to merge two Python dictionaries

Batsmens={"Virat Kohli":"Opener","Devdutt Padikkal":"Opener",
          "Glenn Maxwell":"Top Order","Rajdat Patidar":"Top/Middle Order",
          "Ab De villiers":"Middle Order/Wicket Keeper"}
All_Rounders={"Washington Sundar":"Top Order/Off Spin","Harshal patel":"Middle Order/Medium Fast",
              "Daniel Sams":"Middle Order/Medium Fast","Kyle Jamieson":"Bottom Order/Medium Fast"}
Bowlers={"Mohammed SIraj":"Medium Fast","Yuzvendra Chahal":"Leg Spin"}
Bench={"Daniel Christian":"Middle Order/Medium Fast","Kane Richardson":"Medium fast",
       "Adam Zampa":"Middle Order/Off Spin","Mohhamed Azharuddeen":"Top Order",
       "Finn Allen":"Top Order/Wicket Keeper","Pavan Deshpande":"Medium Fast",
       "Shabaz Ahmed":"Bottom Order/Off Spin"}

#merging teo teo dictionaries
print("\n Batsmen are:",Batsmens)
print("\n All Rounders are:",All_Rounders)
print("\n Bowlers are:",Bowlers)
print("\n Bench Players are:",Bench)
Batting_Order={}
#using copy() method
Batting_Order=Batsmens.copy()
#using update() method
Batting_Order.update(All_Rounders)
print("\n Batting order is:",Batting_Order)

#Write a Python program to remove a key from a dictionary


#deleting a key(Dwayne Bravo,Krishnappa Goutham,Cheteswar pujara:Ruled out dua to injury)
#using del function
del Bench["Kane Richardson"]
#using pop function
Bench.pop("Shabaz Ahmed")
#using popitem function
Bench.popitem()
print("\n Updated Bench Players are:",Bench)

#Write a Python program to map two lists into a dictionary
Substitute=['Sachin Baby','Suyas Prabudesai','Srikar Bharath']
Role=['Top Order/Wicket Keeper','Fast Medium','Leg Spin']
print("\n Substitute list is:",Substitute)
print("\n Their role is:",Role)
Subs={}
for key in Substitute:
    for value in Role:
        Subs[key]=value
        Role.remove(value)
        break
print("\n The Sustitues are:",Subs)

#Write a Python program to find the length of a set

Openers={"Virat Kohli","Devdutt Padikkal","Finn Allen","Mohhamed Azharuddeen","Washington Sundar","Rajdat Patidar"}
print("\n No of Openers are:",len(Openers))
print("\n", Openers)

# Write a Python program to remove the intersection of a 2nd set from the 1st set

Batting_Capability={"Virat Kohli","Devdutt Padikkal","Glenn Maxwell","Rajdat Patidar","Ab De villiers",
                    "Washington Sundar","Harshal patel","Daniel Sams","Kyle Jamieson"}
All_Round_Capability={"Washington Sundar","Harshal patel","Daniel Sams","Kyle Jamieson"}
Bowling_Capability={"Washington Sundar","Harshal patel","Daniel Sams","Kyle Jamieson",
                    "Mohammed SIraj","Yuzvendra Chahal"}
print("\n Players having Batting_Capability:",Batting_Capability)
print("\n Players having All_Round_Capability:",All_Round_Capability)
print("\n Players having Bowling_Capability:",Bowling_Capability)
Pure_Batsmens=Batting_Capability-All_Round_Capability
print("\n Pure Batsmens are:", Pure_Batsmens)