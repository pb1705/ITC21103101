#Question  1
n1= float(input("Enter the value of n1 "))
n2= float(input ("Enter the value of n2 "))
n3 = float(input("Enter the value of n3 "))
sum = float(n1+n2+n3)
average = float(sum/3)
print(average)


#Question 2
noofdependants=int(input("Enter The No of dependants : "))
dependantdeduction= noofdependants*3000
Grossincome=float(input("Enter Your Total Income $"))
standarddeduction = 10000
Taxableincome= Grossincome -dependantdeduction-standarddeduction
tax= float(0.2*Taxableincome)
print("You owe tax of $",tax)

#Question 3
Name = str(input("Enter the name of the student :"))
SID=int(input("Enter the SID of the student : "))
Gender=str(input("Enter the gender of the student : \n enter M for male \n F for female\n  U for unkown : \n "))
course_name = str(input("Enter  course name :"))
CGPA=float(input("Enter student's CGPA : "))
list = [SID ,Name, Gender,course_name,CGPA]
print(list)

#Question 4
marks1=float(input("Enter the marks of student 1 :"))
marks2=float(input("Enter the marks of student 2 :"))
marks3=float(input("Enter the marks of student 3 :"))
marks4=float(input("Enter the marks of student 4 :"))
marks5=float(input("Enter the marks of student 5 :"))
list =[marks1, marks2,marks3,marks4,marks5]
list.sort()
print(list)


#Question 5
#a
List_Provided= ['Red','Green','White','Black','Pink' ]
print(List_Provided)
List_Provided.remove('Black')
print(List_Provided)
#b
LIST_PROVIDED_=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
LIST_PROVIDED_.remove('BLACK')
LIST_PROVIDED_.remove('PINK')
LIST_PROVIDED_.insert(3, 'PURPLE')
print("UPDATED LIST = \n", LIST_PROVIDED_)