#############   ASSIGNMENT- 2#########


#1. Construct a flowchart to show how to determine the greater of two given numbers.

# a,b=map(int,input().split())
# if a>b:
#     print("a is greater than b:",a)
# else:
#     print("b is greater than a:",b)
    

#2. Construct a flowchart to print the name of days.

# n=int(input("enter the between 1 to 7:"))
# if n==1:
#     print("SUNDAY")
# elif n==2:
#     print("MONDAY")
# elif n==3:
#     print("TUESDAY")
# elif n==4:
#     print("WEDNESDAY")
# elif n==5:
#     print("THURSDAY")
# elif n==6:
#     print("FRIDAY")
# else:
#     print("SATURDAY")


#4.& 5. Construct a flowchart to take selling price and cost price as input and calculate the profit and loss percentage.

# s_p,c_p=map(int,input().split())
# profit=s_p-c_p
# loss=c_p-s_p
# p_per=(profit/c_p)*100
# l_per=(loss/s_p)*100
# if s_p>c_p:
#     print(profit," &profit %:",p_per)
# elif s_p<c_p:
#     print(loss,"&loss %: ",l_per)
# else:
#     print("there is no profit and loss.") 


#6. Construct a flowchart to take two sides as input and check whether it is a rectangle or a square 


# l,b=map(int,input().split())
# if l==b:
#     print("it is a square")
# else:
#     print("it is a rectangle")


#8. Construct a flowchart to check whether a number is the smallest 4 digit number.

# a=int(input())
# if a==1000:
#     print("it is a smallest four digit number")
# else:
#     print("it is not a smallest four digit number")


#9. Construct a flowchart to check whether a number is the largest 3 digit number.

#a=int(input())
# if a==999:
#     print("it is largest digit number")
# else:
#     print("it is not a largest four digit number")



#10. Construct a flowchart to check whether a number is divisible by 7 or not.


# a=int((input()))
# if a%7==0:
#     print("yes,it is divisble by 7")
# else:
#     print("not,divisible by 7")

#11.  Construct a flowchart program to check whether a number is even or odd.

#a=int((input()))
# if a%2==0:
#     print("yes,it is even")
# else:
#     print("it is odd")


#12.  Construct a flowchart to check whether the last digit of a number (entered by user) is divisible by 3 or not.


# a=int(input())
# b=a%10
# if b%3==0:
#     print("yes")
# else:
#     print("no")



#13. Construct a flowchart to check whether a person is eligible for voting or not. Age for voting is 18 years.

# age =int(input())
# if age>=18:
#     print("yes, he is eligible")
# else:
#     print("no, he is not eligible")


#14. Construct a flowchart to display "Hello" if a number entered by the user is a multiple of five , otherwise print "Bye".

# a=int(input())
# if a%5==0:
#     print("Hello")
# else:
#     print("bye")
    


#15. Construct a flowchart to input the marks of two students in 5 subjects and check who is the topper.

# t_sub=int(input())
# i=1
# s_a,s_b=0,0
# while i<=t_sub:
#     a,b=map(int,input().split())
#     s_a+=a
#     s_b+=b
#     i+=1
# if s_a>s_b:
#     print("a is the topper")
# else:
#     print("b is the topper")



#16.Construct a flowchart to check whether a number entered is a three digit number or not.

# a=int(input())
# if a>99 and a<1000:
#     print("it is a three digit number ")
# else:
#     print("it is not a three digit number")
    

# 17. Construct a flowchart to check whether a person is a senior citizen or not(Senior citizen Age=60).

# age =int(input())
# if age >=60:
#     print("yes ,he or she is a senior citizen")
# else:
#     print("yes ,he or she is not a senior citizen")


#18.Accept the temperature in degrees Celsius of water and check whether it is boiling or not (boiling point of water in 100oC).


# temp=int(input())
# if temp >=100:
#     print("yes,it is hot" )
# else:
#     print("no,it is not  hot" )



#19.Construct a flowchart to calculate the sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


# a,b=map(int,input().split())
# sum=a+b
# if sum>=15 and sum<=20:
#     print(20)
# else:
#     print(sum)


#20. A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for the user.

# cost=int(input())
# discount=int(input())
# if cost>1000:
#     price=(cost*discount)/100
#     net_cost=cost-price
#     print(net_cost)
# else:
#     print(cost)
    


#21. A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years. Ask users for their salary and year of service and print the net bonus amount.

# salary, s_year=map(int,input().split())
# if s_year>5:
#     bonus=salary*5/100
#     print(bonus)
# else:
#     print("no bonus")


#22. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.Take following input from the user. Number of classes held. Number of classes attended. And print, percentage of class attended. Is the student allowed to sit in the exam or not.

# a_classes,t_c=map(int,input().split())
# per =(a_classes/t_c)*100
# print(per)
# if per>=75:
#     print("yes he will allowed to sit in the exam")
# else:
#     print("no ,he will be not allowed to sit in the exam.")


#23. Take an integer N as input and check whether it ends with 3 or 7. If it ends with 3, print “ends with 3”, if it ends with 7, print “ends with 7”, otherwise print the number itself.

# a=int(input())
# r=a%10
# if r==3:
#     print("ends with 3")
# elif r==7:
#     print("ends with 7")
# else:
#     print(a)


#24. Construct a flowchart to take two numbers as input and print their difference if the first number is greater than the second number, otherwise print their sum.

# a,b=map(int,input().split())
# if a>b:
#     print("difference of a &$b is ",a-b)
# else:
#     print("addition of a&b:",a+b)
    
#25. Construct a flowchart to obtain a number N and increment its value by 1 if the number is divisible by 4, otherwise, decrement its value by 1.


# a=int(input())
# if a%4==0:
#     print(a+1)
# else:
#     print(a-1)
    
#26. Construct a flowchart to obtain the length (L) and breadth (B) of a rectangle and check whether its area is greater or perimeter is greater or both are equal.

# l,b=map(int,input().split())
# area=l*b
# perimeter=2*(l+b)
# if area>perimeter:
#     print("area is greater than perimeter")
# elif area<perimeter:
#     print("perimeter is greater than area ")
# else:
#     print("both are equally")
    


#28. Construct a flowchart to check if a given number is one digit or two digit or three digits or more than three digits.

# a=input()
# b=len(a)
# print("it is {0} digit number".format(b))

#30. Construct a flowchart to check whether a number is negative, positive or zero.

# a=int(input())
# if a>0:
#     print("a is a positive number")
# elif a<0:
#     print("a is a negative number"))
# else:
#     print("a is equals to zero")


#31. Accept any city from the user and display the monument of that city.
                #   City                                 Monument
                #   Delhi                               Red Fort
                #   Agra                                Taj Mahal
                #   Jaipur                              Jal Mahal


# city=input()
# if city=="Delhi":
#     print("RED FORT")
# elif city=="Agra":
#     print("Taj Mahal")
# elif city=="Jaipur":
#     print("Jal Mahal")
# else:
#     print("please enter the correct city!")
    

#33. Construct a flowchart to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%


salary=int(input())
g_salary=0
net_salary=0
if salary>=10000:
    hra=(salary*20)/100
    da=(salary*80)/100
    print(salary+hra+da)
elif salary<=20000:
    hra=(salary*25)/100
    da=(salary*90)/100
    print(salary+hra+da)

else:
    hra=(salary*20)/100
    da=(salary*25)/100
    print(salary+hra+da)













#34. A teacher has divided her classroom into groups of 5 based on their roll numbers. The last roll number of each group has been elected as the leader of the group who will manage the tasks performed by the group. Write a program for the teacher to enter the roll number of the student and check if he/she is a Group Leader or not?


# roll_no=int(input())

# if roll_no%5==0:
#     print("he will become the leader")

# else:
#     print("he will become the leader")



#35. Roller Coasters require children to have a minimum height of 5 feet. Any child below this height is generally not allowed on them. Write a program to accept a child’s height in inches and display if he or she will be allowed to ride or not. 

# a=int(input())
# if a>=5:
#     print("he is allowed to ride")
# else:
#     print("he is not allowed to ride")











#36. Construct a flowchart to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 

# cost=int(input())
# if cost>100000:
#     tax=(cost*15)/100
# elif cost>50000 and cost<=100000:
#     tax=(cost*10)/100
# else:
#     tax=(cost*5)/100
# print(tax)

































































































































