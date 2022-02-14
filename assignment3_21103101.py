# Question 1

str_input = input("Enter the string you want to get the count of words ")
str_input = str_input.lower()
list_for_count = str_input.split() # to include both upper and lower as same
dict_of_count = {} # creating a empty dictionary to store the count
if len(list_for_count) == 1: # using if else to get output for single word or string
    for i in list_for_count[0]:
         dict_of_count[i] = list_for_count[0].count(i)  # using count function to count the character in string

else:
    for i in list_for_count:
        if i in dict_of_count:
            dict_of_count[i] = dict_of_count[i] + 1
        else:
            dict_of_count[i] = 1
print(dict_of_count)


# Question 2
def nextdate():
    day = int(input("Enter the day corresponding to your date"))
    month = int(input("Enter the month corresponding to your date"))
    year = int(input("Enter the year corresponding to your date"))
    monthwith30days = [4, 6, 9, 11] # storing in list months with 30 days
    monthwith31days = [1, 3, 5, 7, 8, 10, 12] # storing in list months with 31 days
    if 1 <= day <= 31 and 1 <= month <= 12 and 1800 <= year <= 2025:
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)): # leap year condition
            if day < 29:
                day = day + 1
                print("Next date is : %d/02/%d" % (day, year))
            elif day == 29:
                print("Next date is : 01/03/%d" % year)
            elif day > 29 :
                print("ERROR! Enter valid inputs")
                nextdate()
        elif month == 2 and not((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)): # if year is not leap year
            if day < 27:
                day = day + 1
                print("Next date is : %d/02/%d" % (day, year))
            elif day == 28:
                print("Next date is : 01/03/%d" % year)
            elif day > 28:
                print("ERROR! Enter valid inputs")
                nextdate()
        elif month in monthwith30days:
            if day <= 29:
                day = day + 1
                print("Next date is : %d/%d/%d" % (day, month, year))
            elif day == 30:
                month = month + 1
                print("Next date is : 01/%d/%d" % (month, year))
            elif day == 31:
                print("ERROR! Enter valid inputs")
                nextdate()
        elif month in monthwith31days:
            if day <= 30:
                day = day + 1
                print("Next date is : %d/%d/%d" % (day, month, year))
            elif day == 31 and month != 12:
                month = month + 1
                print("Next date is : 01/%d/%d" % (month, year))
            elif day == 31 and month == 12:
                year = year + 1
                print("Next date is : 01/01/%d" % year)
    else:
        print("Enter valid inputs")
        nextdate()
nextdate()


#QUESTION 3
list_input = []  # creating a list for storing numbers to be squared
num_of_inputs = int(input("Enter the total number of inputs you want to give"))
i = 1
# Using while loop to get multiple entries
while i <= num_of_inputs:
    print(f"Enter the {i}th number you want square of")
    num_to_be_squared = int(input())
    list_input.append(num_to_be_squared)  # adding to the list the input entered
    i = i + 1
list_to_be_printed = []  # creating a list for storing number and its square
for i in list_input:
    n = i**2
    list_to_be_printed.append((i, n))  # adding number and it's square to the list as tuple
print(list_to_be_printed)


#QUESTION 4
def grading():
    GRADE_POINTS = int(input("Please enter your \'grade points\':"))  # getting grade points and using if elif
    if GRADE_POINTS >= 4 and GRADE_POINTS <= 10:
        if GRADE_POINTS == 10:
            print("Your Grade is \'A+\' and Outstanding Performance")
        elif GRADE_POINTS == 9:
            print("Your Grade is \'A\' and Excellent Performance")
        elif GRADE_POINTS == 8:
            print("Your Grade is \'B+\' and Very Good Performance")
        elif GRADE_POINTS == 7:
            print("Your Grade is \'B\' and Good Performance")
        elif GRADE_POINTS == 6:
            print("Your Grade is \'C+\' and Average Performance")
        elif GRADE_POINTS == 5:
            print("Your Grade is \'C\' and Below Average Performance")
        elif GRADE_POINTS == 4:
            print("Your Grade is \'D\' and Poor Performance")
    else:
        print("ENTER VALID GRADE POINTS")
        grading()
grading()



# QUESTION 5
z = 6
for i in range(z):
    for j in range(i):
        print(" ",end ="")
    for j in range(2*(z-i)-1):
        print(chr(65+j),end = "")
    print()
print("\n")



#QUESTION 6

# creating an empty dictionary for storing names
dict_sidnames = {}
loop = True  # infinite while loop till user want to stop storing data
while loop:
    SID = int(input("Enter the sid of student\n"))
    NAME = input("Enter the name of the student\n")
    if SID in dict_sidnames.keys():
        print("Error! SID is already stored")
    else:
        dict_sidnames[SID] = NAME
    print("Do you want to continue enter\'Y\' to continue and \'N\' to exit")
    iterator = input()
    if iterator == "Y":
        loop = True
    elif iterator == "N":
        loop = False  # using condition to stop the loop from further iterations when user enter N
# a

#  printing dictionaries
print("a)", dict_sidnames)

# b

# using inbuilt sorted function to sort the dictionay and using lamba/anonymous function as key
# sorting by names
print("b)", {k: v for k, v in sorted(dict_sidnames.items(), key=lambda listfor_sorting: listfor_sorting[1])})

# c

# sorting by SIDs
print("c)", {k: v for k, v in sorted(dict_sidnames.items())})
# d
# searching the name in dict for the sid entered by user
SEARCH = int(input("Enter the SID to search for the name of the student "))
print("d)", dict_sidnames[SEARCH])


# Question 7
# defining a function that would return the value of the series at nth place
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# getting the value of nth place till which user want the series to be printed


num = int(input("Enter the number you want the fibonacci series upto"))

# printing the series
for i in range(1, num + 1):
    print(fib(i), end=" ")



# Question 8
print()

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

#  a
# finding elements thar are in only set1 and set2 not in both
Set1_2 = set1.union(set2) - set1.intersection(set2)
print("a)", Set1_2)

# b
# set of elements that occur only once that is only in set 1 or  only in set 2 or only in set3
set1_2_3 = Set1_2.union(set3) - set3.intersection(Set1_2)
print("b)", set1_2_3)

# c
# set of elements which are present in exactly 2 of 3sets
set_2_of_123 = ((set1.intersection(set2)).union(set1.intersection(set3))).union(set2.intersection(set3)) - ((set1.intersection(set2)).intersection(set3))
print("c)", set_2_of_123)

# d
# set of elements in range 1 to 10 that are not in set 1
set4 = set()
for i in range(1, 11):
    if i not in set1:
        set4.add(i)
print("d)", set4)

# e
# set of elements in range 1 to 10 that are not in set 1,set 2 or set 3
set5 = set()
for i in range(1, 11):
    if i not in (set1.union(set2)).union(set3):
        set5.add(i)
print("e)", set5)
