#Create another Python project, repeat the Question 2b and 2c from Laboratory Wk01.
#Question2B

#prompt user to key in module code
code = input("Please enter the module code CSCXXXX: ")

match code:
    case "CSC1010":
        print("Computer Network")
    case "CSC1009":
        print("Object-Oriented Programming") 
    case "CSC1008":
        print("Data Structures & Algorithms")
    case "CSC1007":
        print("Operating System")
    case "CSC1006":
        print("Mathematics 2")

#Question2C

#loop from 102 to 65
for i in range(102, 65, -1):
    if i % 2 != 0 :
        print(i)     

