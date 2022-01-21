#ASSIGNMENT 2

#QUESTION 1
Given_String = 'Python is a case sensitive language'
#a)
#finding the length of given string
print("a) The length of given string is ",len(Given_String))
#b)
#Reversing the string
print("b) The reversed string is \n" +Given_String[-1::-1]) #startingfrom last , with a gap of 1 reversed
#c
#Storing (a case sensitve language) as new string
new_string = Given_String[10:26]
#d
Given_String.replace(new_string,'object oriented')
#e
#Finding the index of a
print("e) The index of 'a' is :",Given_String.find('a'))
#f
#removing the white spaces
print("f) The given string with no spaces :\n"+ Given_String.replace(" ",""))

#Question 2
Name = 'Prranav Babbar'
SID = 21103101
Department = 'CSE'
CGPA = 9.9
print("Hey,%s Here!"%Name)
print("MY SID is %d" %SID)
print("I am from %s department and" %Department , "my CGPA is %f\n" %CGPA)

#Question3
a = 56 #0011 1000
b = 10 #0000 1010
#a
#using bitwise 'and'
print("a) The value of bitwise a and b =", a & b )
#b
#using bitwise 'or'
print("b) The value of bitwise a or b = ", a | b)
#c
#using bitwise 'xor'
print("c) The value of a xor b is ", a^b)
#d
#shifting a and b both left shift
a =a<<2
b= b<<2
print("d) The values of both a and b shifted left bitwise by 2 bits are %d" %a, "and %d respectively"%b)
#e
#shifting bitwise right a with 2 bits and b with 4 
a = a>>2
b = b>>4
print("e) The value of a shifted right bitwise by 2 bits is %d" %a, "and The value of b shifted right bitwise by 4 bits is %d\n"%b)

#Question 4
#getting numbers from user
num1 = int(input("Enter the first number :\n"))
num2 = int(input("Enter the second number :\n"))
num3 = int(input("Enter the third number :\n"))
if (num1 > num2 and num2 >num3) :
    largest_number = num1
elif (num2 > num1 and num1 > num3) :
    largest_number = num2
else : largest_number = num3
print("The largest number you have entered is %d \n"%largest_number)

#Question5
#To find 'name' in string entered by user
input_string = str(input("Enter a string to search for word 'name' in it:\n"))
if ('name' in input_string) :
    print("Yes")
else : print("No\n")

#Question6
#getting length of sides to check the possiblity of a triangle with the data
side_a = float(input("Enter the first side  of triangle :"))
side_b = float(input("Enter the second side  of triangle :"))
side_c = float(input("Enter the third side  of triangle :"))
#some brackets were added for ease of understanding and can be omitted
if ((side_a< (side_b + side_c)) and (side_b<(side_c + side_a)) and (side_c<(side_a + side_b))) :
    print("YES! You can construct a TRIANGLE with the data you entered")
else: print("You cannot construct a TRIANGLE with the data you entered")
