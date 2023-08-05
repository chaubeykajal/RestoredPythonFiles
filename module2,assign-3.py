#1. Construct a flowchart to find a maximum between three numbers. (Use minimum number of comparisons)

# a,b,c=map(int,input().split())
# if a>b:
#     max=a
#     if max<c:
#         max=c
# else:
#     max=b
#     if max<c:
#         max=c
# print(max)



#2. Validate a given year.       
# (Hints. The year in the date must be greater than zero, the months must lie between 1 and 12, and the days must lie between 1 and 31, depending on the month numbers.)

# d,m,y=map(int,input().split())
# if d>=1 and d<=31:
#     if m>=1 and m<=12:
#         print(" it is valide date & month")
#     else:
#         print("there is no{0}month in our calender".format(m))
# else:
#     print("PLEASE! enter a valid date.")
    

#3. Construct a flowchart to input electricity unit charges and calculate the total electricity bill according to the given condition:
# For the first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


# c_elec=int(input())
# if c_elec<=50:
#     tb=c_elec*0.50
# elif c_elec>50 and c_elec<=100:
#     tb=c_elec*0.75
# elif c_elec>100 and c_elec<=200:
#     tb=c_elec*1.20
# else:
#     tb=c_elec*20/100
# print(tb)



#4. Construct a flowchart to calculate the electricity bill (Accept the number of units from the user) according to the following criteria:                                                                   Unit                         Price  
# First 100 units                                                   no charge
# Next 100 units                                                  Rs 5 per unit
# After 200 units

# c_u=int(input())
# if c_u<=100:
#     bill=c_u*0
# elif c_u>100 and c_u<=200:
#     c_u-=100
#     bill=100*0+c_u*5
# else:
#     bill=0+100*5+(c_u-200)*10
    
    

#5. Accept the age, gender (‘M’,   ‘F’), and the number of days and display the wages accordingly

#If the age does not fall in any range then display the following message: “Enter appropriate age”
# g=input()
# age,w_days=map(int,input().split())
# #(please enter genger in short and capital letter! ,ex="M" or "S")

# if g=="M":
#     if age>=18 and age<30:
#         wages=w_days*700
#     elif age >=30 and age <=40:
#         wages=w_days*800
        
# elif g=="F":
#     if age>=18 and age<30:
#         wages=w_days*750
#     elif age >=30 and age <=40:
#         wages=w_days*850
# print(wages)

#6. Accept the number of days from the user and calculate the charge for the library according to the following:

# First five days:        Rs 2/day.
# Next 5 days:        Rs 3/day.
# Next 5  days:         Rs 4/day
# After 15 days:         Rs 5/day
 
# days =int(input())
# if days<=5:
#     lc=2*5
# elif days>5 and days<=10:
#     lc=2*5+(days-5)*3
# elif days>10 and days <=15:
#     lc=2*5+(5*3)+(days-10)*4
# else:
#     lc=2*5+(5*3)+(5*4)+(days-15)*5
# print(lc)                 
                  
   
#7. You have denominations of rupee notes in the following form—1, 2, 5, 10, 20, 100, 200, 500, 2000. Take any amount from the user and print the minimum number of notes needed to add up to that number.    
        

#8.Construct a flowchart to categorize the shape of a quadrilateral as either a square, rhombus, rectangle, parallelogram, or irregular quadrilateral, having input the lengths of the four sides and one internal angle.

# s1,s2,s3,s4,a=map(int,input().split())
# s_o_q,o_a=map(int,input().split())

# if s_o_q==360:
#     if s1==s2==s3==s4 and a==90:
#         print("square")
#     elif s1==s2==s3==s4 and a==o_a:
#         print("rompus")
#     elif s1==s3 and s2==s4 and a==90:
#         print("rectangle")
#     elif s1==s3 and s2==s4 and a==o_a:
#         print("parallelograme")
#     else:
#         print("only quadilateral")
# else:
#     print("not a quadilateral")

#11. A certain steel is graded according to the following conditions:
# (i) Rockwell-hardness > 50
# (ii) Carbon content > 0.7
# (iii) Tensile strength > 5600 kg/cm2
# The steel is graded as follows:
# a. Grade 10, if all the conditions are satisfied
# b. Grade 9, if conditions (i) and (ii) are satisfied
# c. Grade 8, if conditions (ii) and (iii) are satisfied
# d. Grade 7, if conditions (i) and (iii) are satisfied
# e. Grade 0, otherwise

#11. The following rules are used to calculate the bonus for the employees of an organization.
# (i) If the pay is more than $3,000, the bonus amount is fixed, and it is equal to $300.
# (ii) If the pay is more than $1,600, but less than or equal to $3,000, the bonus will be 10% of the pay subject to a maximum of $240.
# (iii) If the pay is less than or equal to $1,600, the bonus is 15% of pay, subject to a minimum of $100.
# Test cases:-
# 3050
# 1800
# 500
# -3500

salary=int(input())
if salary >3000:
    bonus=300
elif salary<=3000 and salary>1600:
    b=salary*60/100
    if b<240:
       bonus=240
    else:
        bonus=b
elif salary<0:
    bonus="no bonus"
else:
    b=salary *15/100
    if b>100:
        bonus=100
    else:
        bonus=b
print(bonus)



#r,c,t=map(float,input().split())

# if r>50 and c>0.7 and t>5600:
#     print("grade:",10)
# elif r>50 and c>0.7:
#     print("grade:",10)
# elif c>0.7 and t>5600:
#     print("grade:",8)
# elif r>50 and t>5600:
#     print("grade:",7)
# else:
#     print("grade:",0)
    

#12.Find whether a given year is a leap year.


# year=int(input())

# if year%4==0 and year%100!=0:
#    print("{}is a leap year".format(year))
# elif year%400==0 and year%100==0:
#    print("{}is a leap year".format(year))
# else:
#     print("{}is not a leap year".foramt(year))


# year=int(input())
# if year%100==0:
#     if year%4==0:
#         if year%400==0:
#             print("yes,it is a leap year")
#         else:
#             print("no,it is not a leap year")
#     else:
#         print("Yes,it is a leap year")
# else:
#     print("no,it is not a leap year")


#15. Accept three integers representing the angles of a triangle in degrees to determine whether they form a valid set of angles of a triangle. If it is not a valid set, then generate a message and terminate the process. If it is a valid set, then the process determines whether it is equiangular (all three angles are the same). It also determines if the triangle is right-angled (has one angle with 90 degrees), obtuse-angled (one angle above 90), or acute-angled (all three angles are below 90 degrees). Finally, it shows the conclusion about the triangle.


# a,b,c=map(int,input().split())
# if a>0 and b>0 and c>0:
#     if a+b+c==180:
#         if a==b==c:
#             print("equiangular traiangle ")
#         elif a==90 or b==90 or c==90:
#             print("right angle triangle")
#         elif a<90 or b<90 or c<90:
#             print("acute angle")
#         elif (a>90 and a<180) or (b>90 and b<180) and (c>90 and c<180):
#             print("obtuse angle")
#     else:
#         print("it is not a triangle")
# else:
#     print("A traiangle has positive  and greater than zero angle")

#16. Accept the lengths of the three sides of a triangle to validate whether they can be the sides of a triangle and then classify the triangle as equilateral (all three sides are equal), scalene (all three sides are different), or isosceles (exactly two sides are equal), and then to see whether it is a right-angled triangle (the sum of the squares of two sides is equal to the square of the third side.)


# a,b,c=map(int,input().split())
# if (a+b)>c and (b+c)>a and (a+c)>b:
#     if a==b==c:
#         print("equilateral triangle")
#     elif a==b!=c:
#         print("issosceles triangle")
#     else:
#         print("scalene triangle")
# else:
#     print("it is not a traingle")
    


#9. The grades in a certain class are determined by coursework and a written examination. Both components of the assessment carry a maximum of 50 points.
# (i) A student must score a total of 45% or more in order to pass
# (ii) A total grade of 44% is moderated to 45%
# (iii) Each component must be passed with a minimum of 20 points
# (iv) If a student scores 45% or more, but does not achieve the minimum grade in one component, he is given a technical fail of 44%, which is not moderated to 45%.



    
    
    
    
    
    
#17.Write a program to check if the given number is divisible by 5, 11, both or none.
# If it is divisible by 5 then print 5
# If it is divisible by 11 then print 11
# If it is divisible by 5 and 11 then print “Both”
# If it is not divisible by 5 and 11 then print “None”
 
 
# a=int(input())
# if a%5==0:
#     print("divisible by 5")
# elif a%11==0:
#     print("it is divisible by 11")
# elif a%5==0 and a%11==0:
#     print("both")
# elif a%5==0 and a%11==0:
#     print("none")
    
    
#18. Find the second max of 3 numbers. (Use minimum number of comparisons)

# max=0
# s_max=0
# l=[]
# i=0
# while i<3:
#     a=int(input())
#     if max<a:
#         s_max=max
#         max=a
#     elif s_max<a and max>a:
#         s_max=a
#     l.append(a)
#     i+=1
# print(l,"greatest and second greatest numbre from the list is= ",max,s_max)


#19. Find the second max of 4 numbers. (Use minimum number of comparisons)

# max=0
# s_max=0
# l=[]
# i=0
# while i<4:
#     a=int(input())
#     if max<a:
#         s_max=max
#         max=a
#     elif s_max<a and max>a:
#         s_max=a
#     l.append(a)
#     i+=1
# print(l,"greatest and second greatest numbre from the list is= ",max,s_max)


#20.Find the third max of 4 numbers. (Use minimum number of comparisons)



# max=0
# s_max=0
# t_max=0
# l=[]
# i=0
# while i<4:
#     a=int(input())
#     if max<a:
#         t_max=s_max
#         s_max=max
#         max=a
#     elif s_max<a and max>a:
#         t_max=s_max
#         s_max=a
#     elif t_max<a and s_max>a:
#         t_max=a
#     l.append(a)
#     i+=1
# print(l,"greatest and second greatest numbre from the list is= ",max,s_max,t_max)


#21. Find the maximum occurring number out of the given 5 numbers. 


# l=[]
# d=[]
# max=0
# for i in range (5):
#     a=int(input())
#     l.append(a)
#     if a not in d:
#         d.append(a)
# j=[]
# for i in range (len(d)):
#     c=l.count(d[i])
#     if max<c:
#         max=c
#         j=d[i]
# print(j,max)






















































































































































































































































