##1. Write a program in Python to allow the error of syntax to be handled using exception handling.

##try:
##    eval("hey =")
##
##except SyntaxError:
##   print("How are you??")




####2. Write a program in Python to allow the user to open a file by using the argv module. If the
##entered name is incorrect throw an exception and ask them to enter the name again. Make sure
##to use read only mode.

##import sys
##  
##print("This is the name of the program:", sys.argv[0])
##  
##print("Argument List:", str(sys.argv))





##3. Write a program to handle an error if the user entered a number more than four digits it should
##return “The length is too short/long !!! Please provide only four digits”


##while True:
##
##     try:
##        number = int(input("enter a number: "))
##        
##     except ValueError as ve:
##        print("Please provide only four digit!!!")
##    
##     if number > 9999:
##            print(" the length is too long! Please provide only four digit")
##
##     else:
##        break
##
##print("The number you have entered is:", number)
             

##4.Create a login page backend to ask users to enter the username and password. Make sure to
##ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
##should not be more than 3 times.



##print('Enter correct username and password combo to continue')
##count = 1
##
##password = ""
##username = ""
##
##while count<5:
##    password!='sheetal123' and username!='sheetal' and count <= 3
##    
##    username = input("Enter username: ")
##    password = input("Enter password: ")
##
##    if password=='Sheetal123' and username=='jsheetal':
##    
##             print('Access granted')
##             count=5
##
##    else:
##                
##            print('Access denied. Try again.')
##            count+=1




##6. 
##6.Read doc.txt file using Python File handling concept and return only the even length string from
##the file. Consider the content of doc.txt as given below:
##Hello I am a file
##Where you need to return the data string
##Which is of even length
##Make sure you return the content in The same link as it is present.




##try:
##    fp = open(r"C:\Users\sheet\OneDrive\Desktop\SHEETAL\doc.txt", "r")
##    print(fp.read())
##    fp.close()
##except FileNotFoundError:
##    print("Please check the path")





##1 Write a program in Python to find out the character in a string which is uppercase using list
##comprehension.

##strng = "ConSuLtaDD"
## 
##print("The string is : " + str(strng))
## 
##res = [char for char in strng if char.isupper()]
## 
##print("The uppercase characters are : " + str(res))


##2 Write a program to construct a dictionary from the two lists containing the names of students and
##their corresponding subjects. The dictionary should map the students with their respective subjects.
##Let’s see how to do this using for loops and dictionary comprehension.




##students = ["smit", "Jaya", "Rayyan"]
##subjects = ['CSE', 'Networking','Operating System']
##  
##print ("students : " + str(students))
##print ("subjects : " + str(subjects))
##  
##res = dict(zip(students, subjects))
##  
##print ("Result of  dictionary is : " +  str(res))

##3. Learn More about Yield, next and Generators

##4. Write a program in Python using generators to reverse the string.
##Input String = “Consultadd Training”


##def reverse_string(strng):
##    length = len(strng)
##    for i in range(length-1, -1, -1):
##        yield strng[i]
##
##for char in reverse_string("Consultadd Training"):
##    print(char,end='')
      



##5.Write an example on decorators.




##def decorate(fun):
##    def f1():
##        print(" I am decorated through this function")
##        fun()
##    return f1
##def simple():
##    print("I am simple function")
##
##simple()









        

