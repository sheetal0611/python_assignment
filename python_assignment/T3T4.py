##Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.


##1.Create a list of 10 elements of four different data types like int, string, complex and float.

##L1 = [1,2,3,"A","B","C",3+5j,5j,1.10]
##print(L1)
##print(type(L1))

##2. Create a list of size 5 and execute the slicing structure
##l1 = [1,2,3,4,5]
##print(l1[::])
##print(l1[-2:-5])
##print(l1[1:-3])
##print(l1[3:4])


##3. Write a program to get the sum and multiply of all the items in a given list.

##from functools import reduce
##L1 = [4, 2, 3, 5, 7]
##
##result1 = reduce((lambda x, y: x * y), L1)
##result2 = reduce((lambda x, y: x + y), L1)
##print(result1)
##print(result2)


##4. Find the largest and smallest number from a given list.
##
##L1 = [ 11,45,34,67,88,25]
##print(max(L1))
##print(min(L1))


##5. Create a new list which contains the specified numbers after removing the even numbers from a
##predefined list.

##n1 = [2,4, 11, 25, 45, 20, 27, 13]
##n2 = [x for x in n1 if x%2!=0]
##print(n1)
##print(n2)


##6. Create a list of elements such that it contains the squares of the first and last 5 elements between
##1 and30 (both included).


##def printelements():
##	l = list()
##	for i in range(1,30):
##		l.append(i**2)
##	print(l[:5])
##	print(l[-5:])
##
##printelements()

##7. Write a program to replace the last element in a list with another list.
##Sample input: [1,3,5,7,9,10], [2,4,6,8]
##Expected output: [1,3,5,7,9,2,4,6,8]

##a = [1,3,5,7,9,10]
##a1 = [2,4,6,8]
##a[5:] = a1
##print(a)

##8. Create a new dictionary by concatenating the following two dictionaries:
##Sample input: a={1:10,2:20} b={3:30,4:40}
##Expected output: {1:10,2:20,3:30,4:40}

##a={1:10,2:20}
##b={3:30,4:40}
##c = {}
##for x in (a,b):c.update(x)
##print(c)


##9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
##and n(both 1 and n included).
##Sample input: n=5
##Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}


##num=int(input("Input a number "))
##d = dict()
##
##for x in range(1,num+1):
##    d[x]=x*x
##
##print(d) 


##10. Write a program which accepts a sequence of comma-separated numbers from console and
##generates a list and a tuple which contains every number in the form of string.
##Sample input: 34,67,55,33,12,98
##Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

##sequence = input("Enter some comma seprated numbers : ")
##list = sequence.split(",")
##tuple = tuple(list)
##print('Tuple :',tuple)
##print('list:',list)
##print(list,end='')
##print(tuple,end='')


##1. Write a program to reverse a string.
##Sample input: “1234abcd”
##Expected output: “dcba4321”

##def reverse(itr):
##  return itr[::-1]
##
##str1 = '1234abcd'
##print(str1)
##print("Reverse strig:",reverse('1234abcd'))


##2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
##letters.
##Sample input: “abcSdefPghijQkl”
##Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12


##def string(z):
##    y ={"upper_case":0, "lower_case":0}
##    for x in z:
##        if x.isupper():
##           y["upper_case"]+=1
##        elif x.islower():
##           y["lower_case"]+=1
##        else:
##           pass
##    print (z)
##    print ("No. of Upper case characters : ", y["upper_case"])
##    print ("No. of Lower case Characters : ", y["lower_case"])
##
##string('“abcSdefPghijQkl”')


##Create a function that takes a list and returns a new list with unique elements of the first list.

##def unique_elements(l):
##  x = []
##  for elements in l:
##    if elements not in x:
##      x.append(elements)
##  return x
##
##print(unique_elements([11,22,31,31,3,30,4,5,5,7])) 

##4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
##in a hyphen-separated sequence after sorting them alphabetically.


##print("Enter hyphen separated sequence of words:")
##list=[n for n in input().split('-')]  
##list.sort()
##print("Sorted:",'-'.join(list))


##5. Write a program that accepts a sequence of lines as input and prints the lines after making all
##characters in the sentence capitalized.



##lines = []
##while True:
##    s = input()
##    if s:
##        lines.append(s.upper())
##    else:
##        break;
##for sentence in lines:
##    print(sentence)





##6. Define a function that can receive two integral numbers in string form and compute their sum and
##print it in the console.


##def add(x,y):
##    z = int(x) + int(y)
##    return z
##
##num1 = "10"
##num2 = "20"
##
##
##sum = add(num1,num2)
##print("sum = ",sum)


##7.Define a function that can accept two strings as input and print the string with the maximum length
##in the console. If two strings have the same length, then the function should print both the strings line
##by line.


##def length(str1, str2):
##	if (len(str1) == len(str2)):
##		print(str1)
##		print(str2)
##
##	elif (len(str1) < len(str2)):
##		print(str2)
##	
##	else:
##		print(str1)
##
##stri1 = input(str("enter First String: "))
##stri2 = input(str("enter Second String: "))
##
##length(stri1, stri2)



##8. Define a function which can generate and print a tuple where the values are square of numbers
##between 1 and 20 (both 1 and 20 included).


##def printTuple():
##    list = [i ** 2 for i in range(1, 21)]
##    print(tuple(list))
##
##printTuple()


##9. Write a function called showNumbers that takes a parameter called limit. It should print all the
##numbers between 0 and limit with a label to identify the even and odd numbers.


##def shownumber(limit):
##
##        for i in range(0, limit):
##                if i==0:
##                   print(i,end=" ")
##                   print("EVEN")
##
##                elif i%2==0:
##                   print(i,end=" ")
##                   print("EVEN")
##
##                else:
##                   print(i,end=" ")
##                   print("ODD")
##print(shownumber(4))


##Write a program which uses filter() to make a list whose elements are even numbers between 1
##and 20 (both included)


##list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20] 
##is_even = lambda x: x % 2 == 0 
##list2 = list(filter(is_even, list1))
##print("\nfiltered Even numbers from the list:")
##print(list2)



##11. Write a program which uses map() and filter() to make a list whose elements are squares of even
##numbers in [1,2,3,4,5,6,7,8,9,10].


##list1 = [1,2,3,4,5,6,7,8,9,10]
##is_even = lambda x: x % 2 == 0 
##list2 = list(filter(is_even, list1))
##result = map(lambda x: x * x, list2)
##print(list(result))


##12. Write a function to compute 5/0 and use try/except to catch the exceptions

##def throws():
##        return 5/0
##try:
##        throws()
##except ZeroDivisionError:
##        print ("division by zero!")
##except Exception:
##        print ('Caught an exception')
##finally:
##        print ('In finally block for cleanup')

##13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
        

##from functools import reduce
##from operator import concat
##
##list =['1','2','3','4','5','6','7']
##flatlist = reduce(concat, list)
##print(flatlist)


##14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
##Make sure to use only higher order functions.
 
##def shout(text):
##        return text.upper()
##    
##print(shout("The following are the multiple of 7"))
##    
##nl=[]
##for x in range(0,1000):
##    if (x%3!=0) and (x%7==0):
##        nl.append(str(x))
##print (','.join(nl))
##
##yell = shout
##print(yell("This is higher order function"))



##15. Write a program in Python to multiply the elements of a list by itself using a traditional function
##and pass the function to map() to complete the operation.


##def square(n):
##    return n*n
##my_list = [1,2,3,4,5,6,7,8,9,10]
##updated_list = map(square, my_list)
##print(updated_list)
##print(list(updated_list))
##    

##16. What is the output of the following codes:

##def foo():
##        try:
##                return 1
##        finally:
##                return 2
##                k = foo()
##                print(k)
##
##output: k is not defined


##16. What is the output of the following codes:

##def a():
##        try:
##                f(x, 4)
##        finally:
##                print('after f')
##                print('after f?')
##a()


##output: f is not defined
