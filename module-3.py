############  ASSIGNMENT -1 ################

#Construct a flowchart to show how the sum of two numbers can be obtained.
# (Input 2 numbers from the user)
# Dry run: 
# 28,32
# 876,23
# -234,-56

# ans] a,b=map(int,input().split())
#print(a+b)


#   Construct a flowchart to show the procedure for obtaining the average of two given numbers.
# (Input 2 numbers from the user)
# 56,56
# 20,25
# 78,-78

#ans]  a,b=map(int,input().split())
#print((a+b)//2)


#   Construct a flowchart to show how to obtain the daily wage of a worker on the basis of the hours worked during the day.
# (Daily wage of a worker is determined by hours worked per day and the hourly wage rate. Input the number of hours worked from the user and the hourly wage rate)
# 7,400
# 6,300
# 9,380


# ans]  day= int(input("how many  days have you worked:"))
# p_hw=int(input())
# w_h=int(input("enter the working hour iin your company per day:"))

# t_wages=p_hw*w_h*day
# print(t_wages)

#4.  Construct a flowchart to show how to obtain the area of a triangle on the basis of the base and height.
# (Input the base and height of the triangle from the user)
# 4,3
# 16,23
# 7,9

# ans]  b,h=map(int,input().split())
# area_t=1/2*(b*h)
# print(area_t)



#5. Construct a flowchart to show the steps in finding the simple interest on a given amount at a given rate of interest.
# (Input amount, rate of interest and time from the user)
# 2250,4,3
# 6097,3,5
# 2336,2.5,4


# ans] p,r,t=map(int,input().split())
#print((p*r*t)//100)

#6. If P amount of money is invested for N years at an annual rate of interest I, the money grows to an amount T, where T is given by T = P (1 + I/100)N. Construct a flowchart to show how T is determined.
# 1000, 2, 2
# 1500, 5, 1
# 100, 10, 3

#ans]  p,n=map(int,input().split())
# t=p*((1+1/100)**n)
# print(t)

#7. & 8.Construct a flowchart to show how to interchange the values of two variables.
# 20,30
# 45,67
# 34,43

#ans] a,b=map(int,input().split())
# a,b=b,a
# print(a,b)


#9. Construct a flowchart to show how to interchange the values of two variables without using a third variable.
# 20,30
# 45,67
# 34,43

# see above

#10. Construct a flowchart to print a Welcome message. Take input from the user and on the output window print ‘Welcome ____’.(Blank to  be filled by the input taken from User ).
# There
# Hello
# back

#ans] message=input()
#print("welcome",message)


#11.  Construct a flowchart to add, subtract, divide and multiply two integers a and b

# ans]  a,b =map(int,input().split())
# opertor=input()
# if opertor=="+":
#     print(a+b)
# elif opertor=="-":
#     print(a-b)
# elif opertor=="*":
#     print(a*b)
# elif opertor=="/":
#     print(a/b)


#12. Construct a flowchart to calculate the area and perimeter of a rectangle.

# l,b=map(int,input().split())
# area=l*b
# perimeter=2*(l+b)
# print("Area of a rectangele = ", area)
# print("Perimeter of a rectangle=",perimeter)



#13. Construct a flowchart to calculate the semiperimeter of a triangle.

# a,b,c=map(int,input().split())
# semiperimeter_o_t=(a+b+c)//2
# print(semiperimeter_o_t)


# 14. Construct a flowchart to calculate the area  and circumfrence of a circle.

# r=int(input())
# area_o_c=3.14*(r**2)
#c_cum=2*3.14*r
# print(area_o_c)
#print(c_cum)

#15.Given the circumference of a circle, construct a flowchart to calculate the Diameter. 



# area=int(input())
# d=area//2*3.14*4
# print(d)

 

#16.&17. Construct a flowchart to calculate the lateral surface area and Total surface area of a cube

# l=int(input())
# vol=l**3
# TSA=6*(l**2)
# print("volume of cube=", vol)
# print("TSAof cube=",TSA)



#18.&19.Construct a flowchart to find the volume, lateral surface area and Total surface area of a cuboid.


# l,b,h=map(int,input().split())
# vol=l*b*h
# LSA=2*h*(l*b)
# TSA=2*(l*b+b*h+l*h)
# print("volume of cuboid=",vol)
# print("LSA of cuboid=",LSA)
# print("TSA of cuboid=",TSA)



#20.  Construct a flowchart to display the last digit of a number.

# a=int(input())
# print(a[-1])
# print(a%10)

#21.Construct a flowchart to calculate remainder when a is divided by b. 

# a,b=int(input())
# print(a%b)


#22.Construct a flowchart to calculate the quotient when a is divided by b


#a,b=int(input())
# print(a/b)

#23. Construct a flowchart to Calculate the selling price of a product if MRP  and discount are given(Input MRP and discount from user).


# mrp,discount=map(int,input().split())
# s_p=(mrp*discount)//100
# print(s_p)


#24.& 25. Construct a flowchart to calculate the square and cube of a number.

# a=int(input())
# print(a**2,a**3)


#26.Construct a flowchart to calculate how many books we can buy if we have x Rs .   (Cost of a book = Rs. y)(input x,y from user) 

# x,y=map(int,input().split())
# a=x//y
# print("we can buy books=",a)

#27. From the remaining amount in the above question , How many Pens can be bought if one pen costs Rs. 5. Construct a flowchart.


#x,y=map(int,input().split())
# a=x*y
# print("we can buy pens=",a)


# 28.& 29. Construct a flowchart to calculate the total marks obtained by a student in examination. (Subjects : - Hindi, Maths, English, Science, Computer) 


# t_sub,maths,eng,hindi, sci,com=map(int,input().split())
# total_m=maths+eng+hindi+sci+com
# per=(total_m/(t_sub*100))*100
# print(t_sub,per)


# 30.  Construct a flowchart to determine the acceleration due to gravity (g), where g can be obtained from the following formula.


# t,l=map(int,input().split())
# g=((t/2*3.14)**2)/l
# print(g)



#31.  A store sells Vadapavs & Samosas. They want a system where they enter the number of Vadapavs (V) and Samosas (S) a customer buys and a bill with the final price is automatically calculated and displayed. A Vadapav costs 12₹, while a Samosas costs 15₹. Write a program to create such a system.

# v_p,s_p,v_unit,s_unit =map(int,input().split())
# t_v_charges=v_p*v_unit
# t_s_charges=s_p*s_unit


# print(t_s_charges+t_v_charges)


#32. Write a program to take two numbers A and B as input from the user and print the number closest to (but less than) A which is completely divisible by B.


# a,b =map(int,input().split())
# x=a%b
# print(a-x)


#33. Construct a flowchart to obtain the Fahrenheit equivalent of a temperature given in Celsius where the relationship between the two scales of temperature .

unit=input()
temp=int(input())
if unit=="f" or unit=="F":
    celsius=(temp-32)*5/9
    print("temperature in celsius:-",celsius)
elif unit=="c" or unit=="C":
    fehrenheit=((temp*9)/5)+32
    print("temperature in fehrenheit:-",fehrenheit)
else:
    print("please enter the coeeect unit:(")












