###1.Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.
##
##a, b, c = 11, 6.11 ,"Sheetal"
##print("assigning values of different datatypes")
##print(a)
##print(b)
##print(c)
##
##
###2.Create a variable of type complex and swap it with another variable of type integer.
##
##a = 5
##
##c = complex(a)
##print(c)
##print(type(c))
##
##b= int(a)
##print(b)
##print(type(b))
##
##
###2.Create a variable of type complex and swap it with another variable of type integer.
##
##x = 5
##y = 5+0j
##
##x,y = y,x
##print(x)
##print(type(x))
##
##print(y)
##print(type(y))
##
###3.Swap two numbers using a third variable and do the same task without using any third variable.
##
##a = 15
##b = 20
##print("before swaping, the value of a:",a)
##print("before swaping, the value of b:",b)
##
##temp = a
##a = b
##b = temp
##
##print("swap two numbers by using third variable")
##print("Value of a:",a)
##print("value of b:",b)
##
###3.without using any third variable.
##
##x = 10
##y = 5
## 
##print ("The value of x and y before swapping:")
##print("Value of x:",x," and y:", y)
## 
##x, y = y, x
## 
##print ("The value of x and y after swapping:")
##print("Value of x:",x," and y:", y)
##
##
##a = 10
##b = 12
##
##print("before swapping:")
##print("value of a:",a)
##print("value of a:",b)
##
##a,b = b,a
##
##print("after swapping:")
##print("value of a:",a)
##print("value of a:",b)
##
##
##
##
## 5.Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
##another variable called z. Add 30 to z and store the output in variable result and print result as the
##final output.
##
##
##
##    
##x = int(input("enter a 1st number:"))
##y = int(input("enter a 2nd number:"))
##
##z = x+y
##print(z)
##result = z+30
##print("add 30 to z:")
##print("Final output:",result)
##
##
##6.Write a program to check the data type of the entered values.
##
##a = 10
##b = 3.5
##c = "sheetal"
##d = [1,2,3,4,5]
##e = {9,8,7,6,5}
##f = (4,5,6,7,8)
##print(type(a))
##print(type(b))
##print(type(c))
##print(type(d))
##print(type(e))
##print(type(f))
##
##
##
##7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCAS

##
##numberOfBook = 15
##NumberOfFruits = 12
##number_of_vegetables = 20
##print(numberOfBook)
##print(NumberOfFruits)
##print(number_of_vegetables)


##8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
##again. Will it change the value? If Yes then Why?
##
##Answer: Yes, variable can be reassigned to new value.for example, its like an empty box,
##which can includes string,number or any other value.when you reassign the value, it will empty out the old value and replace it with the new value.
##
##
###9If a number is divisible by 3 it should print “Consultadd” as a string
##If a number is divisible by 5 it should print “Python Training” as a string
##If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
##string.
##
##
##n = int(input("enter the number"))
##
##if((n % 3 == 0) and (n % 5 == 0)):
##    print("Consultadd - Python Training".format(n))       
##elif n%3==0:
##    print("consultadd")
##elif n%5==0:
##    print("Python Training")
##
##Write a program in Python to perform the following operator based task:Ask user to choose the following option first:
##If User Enter 1 - Addition
##If User Enter 2 - Subtraction
##If User Enter 3 - Division
##If User Enter 4 - Multiplication
##If User Enter 5 - Average
##Ask user to enter two numbers and keep those numbers in variables num1 and num2
##respectively for the first 4 options mentioned above.
##Ask the user to enter two more numbers as first and second for calculating the average as
##soon as the user chooses an option 5.
##At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
##NOTE: At a time a user can only perform one action.
##
##
##
##def add(x, y):
##    return x + y
##
##def subtract(x, y):
##    return x - y
##
##def divide(x, y):
##    return x / y
##
##def multiply(x, y):
##    return x * y
##
##def average(x, y):
##    return (x + y)/2
##
##print("Select operation.")
##print("1.Add")
##print("2.Subtract")
##print("3.Multiply")
##print("4.Divide")
##print("5.Average")
##
##while True:
##    
##    choice = input("Choose the following option(1/2/3/4/5): ")
##    
##
##    if choice in ('1', '2', '3', '4','5'):
##        num1 = float(input("Enter first number: "))
##        num2 = float(input("Enter second number: "))
##
##        avg = average(num1, num2)
##        answer = add(num1, num2)
##        answer = subtract(num1, num2)
##        answer = multiply(num1, num2)
##        answer = divide(num1, num2)
##    
##
##        if  answer < 0:
##            print("answer is a Negative Number")
##
##
##        if choice == '1':
##            print(num1, "+", num2, "=", add(num1, num2))
##
##        elif choice == '2':
##            print(num1, "-", num2, "=", subtract(num1, num2))
##
##        elif choice == '3':
##            print(num1, "*", num2, "=", multiply(num1, num2))
##
##        elif choice == '4':
##            print(num1, "/", num2, "=", divide(num1, num2))
##
##        elif choice == '5':
##            print(num1, "+", num2, "=", average(num1, num2))
##        
##            
##        next_calculation = input(" DO you want to do next calculation? (yes/no): ")
##        if next_calculation == "no":
##          break
##
##    else:
##        
##        print("Invalid Input")
##      
##
##
##
##Write a program in Python to implement the given flowchart:
##
##a = 10
##b = 20
##c = 30
##
##avg = (a + b + c) / 3
##print("avg =", avg)
##
##if avg > a and avg > b and avg > c:
##    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
##elif avg > a and avg > b:
##    print("%d is higher than %d, %d" %(avg, a, b))
##elif avg > a and avg > c:
##    print("%d is higher than %d, %d" %(avg, a, c))
##elif avg > b and avg > c:
##    print("%d is higher than %d, %d" %(avg, b, c))
##elif avg > a:
##    print("%d is just higher than %d" %(avg, a))
##elif avg > b:
##    print("%d is just higher than %d" %(avg, b))
##elif avg > c:
##    print("%d is just higher than %d" %(avg, c))



##
##4. Write a program in Python to break and continue if the following cases occurs:
##    If user enters a negative number just break the loop and print “It’s Over”
##If user enters a positive number just continue in the loop and print “Good Going”
##
##
##while True:
##    num = int(input("enter value"))
##    if num > 0:
##        print("Going Good")
##        continue
##    else:
##        print("its over")
##        break
##
##
##5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
##multiple of 5, between 2000 and 3200.
##
##
##numbers=[]
##
##for x in range(2000, 3200):
##    
##    if (x%7==0) and (x%5!=0):
##        numbers.append(str(x))
##        
##print (','.join(numbers))
##
##
##
##      
##x=123
##
##for i in x:
##    print(i)
##
##Answer:The output is Error..for i in x:
##TypeError: 'int' object is not iterable
##
##i = 0
##while i <5:
##    print(i)
##    i += 1
##    if i == 3:
##        break
##    else:
##        print("error")
##
##the output will be,
##0
##error
##1
##error
##2
##
##
##count = 0
##while True:
##   print(count)
##   count += 1
##if count >= 5:
##    Break
##
##The output will be an Error
##
##7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
##Expected output: 0 1 2 4 5
##Note: Use ‘continue’ statement
##
##
##
##for x in range(6):
##    if (x == 3 or x==6):
##        continue
##    print(x,end=' ')
##
##
##8. Write a program that accepts a string as an input from the user and calculate the number of digits
##and letters.
##
##
##val = input("Input a string")
##
##int=str=0
##
##for x in val:
##
##    if x.isdigit():
##        int=int+1
##
##    elif x.isalpha():
##        str=str+1
##
##print("Letters", str)
##print("Digits", int)
##
##
##Write a program such that it asks users to “guess the lucky number”. If the correct number is
##guessed the program stops, otherwise it continues forever.Modify the program so that it asks users whether they want to guess again each time. Use two
##variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
##to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
##The program continues as long as a user has not answered “no” and has not guessed the correct
##number)
##
##lucky_num= 7
##
##guess = int (input ("Guess the lucky number: "))
##while True:
##
##    if lucky_num != guess:
##        print ("wrong number!")
##
##        guess = int(input ("Do you want to guess again: "))
##        
##    elif lucky_num == guess:
##        print ("correct guess!")
##        break
##
##
##Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
##such as The program asks for five guesses (no matter whether the correct number was guessed or not). If the
##correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
##After the fifth guess it stops and prints “Game over!”.
##


#####################BOTH ARE TRUE


##
##guess_num = 7
##
##number_of_tries = 1
##
##guess = int (input ("Guess the lucky number: "))
##while guess_num != guess:
##
##              
##    if number_of_tries == 5:
##        break
##    
##    
##    guess = int(input ("Please guess again: "))
##    number_of_tries += 1
##
##
##if guess_num == guess:
##    print ("good guess!")
##    
##else:
##    print ("try again")
##    
##print ("Game Over")
##


##
##In the previous question, insert break after the “Good guess!” print statement. break will terminate
##the while loop so that users do not have to continue guessing after they found the number. If the user
##does not guess the number at all, print “Sorry but that was not very successful”.
##




    
##
##guess_num = 7
##
##number_of_tries = 1
##
##guess = int (input ("Guess the lucky number: "))
##while guess_num != guess:
##
##              
##    if number_of_tries == 5:
##        break
##    
##    
##    guess = int(input ("Please guess again: "))
##    number_of_tries += 1
##
##
##if guess_num == guess:
##    print ("good guess!")
##    
##    
##else:
##    print ("Sorry,but that was not very successful")
