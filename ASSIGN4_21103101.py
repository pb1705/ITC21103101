# Question 1
def tower_of_hanoi(num_discs,start_tower,midtower,dest_tower):
    if num_discs == 0:
        return
    tower_of_hanoi(num_discs-1,start_tower,midtower,dest_tower)
    print(f"Move the disc \'{num_discs}\' from tower \'{start_tower}\' to tower \'{dest_tower}\'")
    tower_of_hanoi(num_discs-1,midtower,dest_tower,start_tower)
tower_of_hanoi(3,"A","B","C")


#QUESTION 2
#Using loop
num_of_rows = int(input("Enter the number of rows you want\n"))
print(f"Pascal's Triangle with {num_of_rows} rows is :")
list_N = []
m = num_of_rows
for i in range(1,num_of_rows+1):

    if i == 1:
        list_N.append(1)
    elif i == 2:
        list_N.append(1)
    else:
        list_temp = []
        list_temp.append(1)
        for j in range(i-2):
            n = list_N[j] + list_N[j+1]
            list_temp.insert(j+1,n)
        list_temp.append(1)
        list_N = list_temp


    print(" "*m ,end = "")
    for k in list_N:
        print(k,end = " ")
    print()
    m = m- 1



#Using recurssion
def pascal_triangle(num_of_rows):
    print(f"Pascal's Triangle with {num_of_rows} rows is :")

    def row(num_of_rows):

        if num_of_rows == 1:
                l1 =[1]
                return l1
        elif num_of_rows == 2:
                l1 =row(1)
                l1.append(1)
                return l1
        elif num_of_rows>2:
                l1 = [1,1]
                l2 = row(num_of_rows-1)
                for i in  range(num_of_rows-2):
                    n = l2[i] + l2[i+1]
                    l1.insert(i+1,n)
                return l1
    for i in range(1,num_of_rows+1):
        print(" "*(num_of_rows-i),end ="")
        for j in row(i):
            print(j,end=" ")
        print()


pascal_triangle(num_of_rows)

#Question 3

num1 = int(input("Enter first number\n"))
num2 =int(input("Enter second number\n"))
quotient = num1//num2
remainder = num1 % num2
print(f"Quotient and remainder obtained from {num1}/{num2} are {quotient}and {remainder} respectively")
#a
print(f"a)Quotient is callable: {callable(quotient)}\nRemainder is callable: {callable(remainder)}")
#b
if quotient == 0 and remainder == 0:
    print("b)Both Remainder and Quotient are zero ")
if quotient != 0 and remainder != 0:
    print("b)Both Remainder and Quotient are non zero")
elif quotient == 0:
    print("b)Quotient is zero")
elif remainder == 0:
    print("b)Remainder is zero")
#c
list_to_Add = [4,5,6]
list_without_filter = []
for i in list_to_Add:
    n1 = i + quotient
    n2 = i + remainder
    list_without_filter.append(n1)
    list_without_filter.append(n2)
list_with_filter = list(filter(lambda x:x>4,list_without_filter))
print(f"c)The list of result with filter result >4 is{list_with_filter}")
#d
result_set = set(list_with_filter)
print("d)",type(result_set))
#e
immutable_resultset = frozenset(result_set)
print("e)Immutable set = ",immutable_resultset)
#f
max_val =  max(immutable_resultset)
hash_maxval = hash(max_val)
print(f"f)The hash value of max from result set is {hash_maxval}")


# QUESTION 4
#making class

class Student():
#making constructor
    def __init__(self,Name,Roll_no):
        self.name = Name
        self.roll_no = Roll_no
    def printdetials(self):
            return (f"The name of student is {Prranav.name} and the roll no of student is {Prranav.roll_no}")
#destructor
    def __del__(self):
       print(  "The object has been deleted successfully")
#creating instance of class
Prranav = Student("Prranav Babbar",21103101)
print(Prranav.printdetials())
del Prranav



# Question 5

# creating Employee class
class Employee():
    #creating constructor
    def __init__(self,Name,Salary):

        self.Name = Name
        self.Salary = Salary


#making instances
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
#a
employee1.Salary= 70000
print(f"a) Salary of mehak after updation {employee1.Salary} ")
#b
print("b)Deleted the record of employee Viren")
del employee3


#Question 6
#Using inbuilt function to get word count
from collections import Counter
def friendship():
    word_to_check = input("Enter the first word that is to be used for test")
    print(f"Enter the word you made from {word_to_check}")
    friends_word = input()
    def letter_count(word):
        list_for_count = list(word)
        dict_of_count = Counter(list_for_count)
        return dict_of_count
#checking if all the word used match in first word
    if letter_count(word_to_check) != letter_count(friends_word):
        print("The word you entered doesnot match the criteria friendship is fake")
    else:
        shopkeeper_check = input("Does the word make sense? Enter Yes or No ") # asking shopkeeper if the word makes sense
        if shopkeeper_check ==  "Yes":
            print("The friendship is real" )
        elif shopkeeper_check ==  "No":
            print("The friendship is fake")
friendship()