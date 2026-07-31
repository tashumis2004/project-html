Ans=True
f1= open("file handling","w")
while Ans:
    str= input("Enter friend name:")
    f1.write(str)
    Ans= input("Do you want to continue enter Yes otherwise press enter")
f1.close()
print("Data store Successfully. To check Open in note pad")
print("Bye!Bye!") 
