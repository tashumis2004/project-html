file = open("fili handing.txt", "w")
for i in range(5):
    name = input("Enter Name: ")
    file.write(name + "\n")
    
file.close()
print("Data Saved Successfully") 
