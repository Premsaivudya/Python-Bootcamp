f = open(r"30 days 30 hour operations","w+")
f.write("I have completed 10 days succesfully")
f.close()
f1 = open(r"30 days 30 hour operations","a+")
f1.writelines(" Premsai") 
f1 = open(r"30 days 30 hour operations","r")
print(f1.read())
f1.close()