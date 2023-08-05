
print(" MERAKI QUESTION " )

# def ask_question (x):           #1
#     return (x)
# a= " who is the primre minister of India ? "
# print(ask_question(a))
# print(ask_question(a))
# print(ask_question(a))
# print(ask_question(a))
# print(ask_question(a))
# i= 1
# while i<=100:
#     print(i ," ",ask_question(a))
#     i+=1

                                 
# def maximum(x):                   #2
#     return max(x)
# list=[12,101,3,4,2,2,22,21,34,554,644,333]
# print(maximum(list))



# def sum(x):                       #3
#     add=0
#     for i in x:
#        add+=i
#     return add
# list=[1,2,3,4,5,5]
# print(sum(list))     
        
#list=[6,7,5,6,5,4,35,34,21,76,32,21]        #4
# def sorting(x):
#     for i in range (len(x)):
#         for j in range (len(x)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     return list
# print(sorting(list))

# def sorting(x):
#     y= x.sort(reverse=True)
#     return x
# print(sorting(list))
        
# print(min(max(False,-3,-4),2,7)  )         #




# def first_letter(x):             #
#     x=sorted(x)
#     for i in range (len(x)):
#         print(x[i][0])
#         print(x[i]) 
# list = ['be','have','do','say','get','make','go','know','take','see','come','think',   
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
# first_letter(list)
# list2=["kajal","chaturvedi"]
# first_letter(list2)



# def create_empty_list(n):
#     i=0
#     while i<=n:
#         return  []
#         i+=1
# print(create_empty_list(5))
        


# def greet(*names):
#     for name in names:
#         print("welcome ",names)
# greet("rinku")
       
# def max(a,b,c):
#     if a>b:
#         max=a
#         sec=b
#         if max<c:
#             sec=max
#             max=c
#         elif sec<c:
#             sec=c
#     else:
#         max=b
#         sec=a
#         if max<c:
#             sec=max
#             max=c
#         elif sec<c:
#             sec=c
#     return max,sec
# print(max(5,6,3))

             
# def max_no(n):
#     #n=int(input("total no: "))
#     no1=int(input())
#     no2=int(input())
#     if no1>no2:
#         max=no1
#         sec=no2
#     else:
#         max=no2
#         sec=no1
#     l=[]
    
#     for i in range (n-2):
#         l.append(int(input()))
        
#         if max<l[i]:
#             sec=max
#             max=l[i]
#         elif sec<l[i]:
#             sec=l[i]
#     return max,sec,l

# print(max_no(5))
        
        
        
# def list_sum(x):
#     sum=0
#     for i in x:
#         sum+=i
#     return ("the sum given list",sum )
# list=[1,2,3,4,5,6,7]
# print(list_sum(list))       
        
        
# def reverse_string(s):
#     for i in range (len(s)-1,-1,-1):
#         print(s[i],end="")   
# reverse_string("1234abcd")

    
        
# def fun():
#     return ("hello")
# print(fun())
     
        
# def add(num1: int, num2: int):
#     num3=num1+num2 
#     return num3
# num1, num2 = 5, 15    
# ans = add(num1, num2)
# print(ans)
        
# def myFun(x, y=50):
#     z=x+y
#     print(z)
# myFun(13)

# def student(*firstname):
#     print(firstname)
# student("kajal", "rupa","radha ")


############_____________DOC QUESTIONS ______________##############



######### QUESTION -1 ###########

       
# list=['abc','ad', 'xyz', 'aba', '1221'] 
# def count(x):
#     for i in range (len(list)):
#         if len(x[i])>2:
#             if x[i][0]==x[i][-1]:
#                 print(x[i])
# count(list)
############### QUESTION -2  ####################


# def three_max():
#     n,a,b=map (int,input().split())
#     if n>a:
#         max=n
#         sec=a
#         if max<b:
#             sec=max
#             max=b
            
#     else:
#         max=a
#         sec=n
#         if max<b:
#             sec=max
#             max=b
            
#     print(max,sec)
# three_max()          
        
########### QUESTION -3   #############       
        
        
# def reverse():   
#     n= input("")
#     for i in range (len(n)-1,-1,-1):
#         print(n[i]) 
# reverse()
        
        
########## QUESTION - 4 #############      
        
# list=[1,2,3,4,2,3,5,1]
# a=[]
# z=0
# for i in range (len(list)):
#     if list[i] not in a:
#         a.append(list[i])

# print(a)
          
 ###############   QUESTION - 49 ###############
 
 
# def even_odd(x):
#     for i in range (x):
#         n= int(input("enter the number: "))
#         if n%2==0:
#             print("even -",n) 
#         else: 
#             print("odd -",n)      
        
# a=int(input())  
# even_odd(a)
  
  
#############   QUESTION -  48     ####################
        
# def cube(x):
#     for i in range (x):
#         n= int(input("power: "))
#         b=int(input("base: "))
#         print(b**n)
# y=int(input())
# cube(y)
    
   
###########    QUESTION - 47  ###############  
    
# def num_gap(x): 
#     list=[0]*x                         # improve 
#     a=0
#     for i in range (x):  
#         n=int(input())
#         list[a]=n                        # create list
#         a+=1
#     list1=[]
#     for j in range (x-2):
#         d= abs((list[j]-list[j+1]))
#         c=abs((list[j+1]-list[j+2]))
#         if c==d:
#             print("yes")
#         else:
#             print("no")
#             break
# length=int(input("lenght of list :"))
# num_gap(length) 

###########    QUESTION - 46
# 
# 
# 
# 
# 
# ###############  
    
# def num_gap(x): 
#     list=[0]*x                         # improve 
#     a=0
#     for i in range (x):  
#         n=int(input())
#         list[a]=n                        # create list
#         a+=1
#     list1=[]
#     for j in range (x-2):
#         d= abs((list[j]-list[j+1]))
#         c=abs((list[j+1]-list[j+2]))
#         if c==d:
#             print("yes")
#         else:
#             print("no")
#             break
# length=7  #int(input("lenght of list :"))
# num_gap(length) 



    
###########b QUESTION -45   ####################


# def my_fun(x):
#     list=[0]*x
#     a=0
#     for i in range (x):
#         n=int(input("elements "))
#         list[a]=n
#         a+=1                          # create list   
#                                                        
#     l=[]  
#     for j in range (x):
#         if list[j]%2==0:
#             l.append(list[j]*100)
#         else:
#             l.append(list[j]*(-1))
#     print(list)
#     print(l)
# t= int(input("length of list: "))
# my_fun(t) 
        
############### QUESTION - 44 and 43  #############      
        
# def last_n(t):
#     list=[0]*t 
    
#     a=0 
#     for i in range (t):
#         e= input("element: ")
#         list[a]=e                         # creating list
#         a+=1 
#     count=0       
#     n=int(input())
#     i=t-1
#     while i>=0:
#         if count==n:
#             break
#         else:
#             print(list[i])   
#             count+=1 
#         i-=1

# g=int(input("length of list: "))       
# last_n(g) 

        
        


############### QUESTION - 42  ############# 
# def summation(t):   
#         a=len(t)
#         list=[]
        
#         for i in range ((len(t))):
#             sum=0
#             for j in range ((len(t[i]))):
#                 sum+=int(t[i][j])
#             list.append(sum)
#         print(list)
# l=['12','34','56','32','1311','432']
# for i in ran
# summation (l)
        
            
            
# list=[[1,4,5],
#       [0,1,2],
#       [1,2,3]]


# for i in range (len(list)):
    
#     sum_r=0
#     sum_c=0
#     for j in range (len(list[i])):
#         sum_r+=list[j][i]
#         sum_c+=list[i][j] 
#     print(sum_c,sum_r)   
        
# a=[[4,3,2],
#    [6,1,9],
#    [11,-1,4],
#    [12,-6,-2]]        
# b=[[7,9,13]
#    ,[2,0,3]
#    ,[10,4,1]
#    ,[6,-2,3]] 
# list=[]
# sum=0       

# for i in range (len(a)):
#     l=[]
#     for j in range (len(a[i])):
#         sum=a[i][j]+b[i][j]
#         #print(sum)
#         l.append(sum)
#     list.append(l)
# print(list)
        
######### matrix sum ###########       
        
# a=[[4,3,2],
#    [6,1,9],
#    [11,-1,4],
#    [12,-6,-2]]        
# b=[[7,9,13]
#    ,[2,0,3]
#    ,[10,4,1]
#    ,[6,-2,3]] 
# list=[]
# sum=0       
# for i in range ()       
        
########### docstring ##############

# def add(a,b):
#    #'''sum of only two variables '''
#    return a+b
#    '''sum of only two variables '''
# print(add.__doc__) 
# print(print.__doc__)  
# import math
# print(math.__doc__) 
# import pickle 
# print(pickle.__doc__)   
        
# def name(x):
#    for i in range (x):
#       print("hello,",i)
# greet(name())       
        
        
######### lamda ############

# smallest = lambda a,b:a+b if a%2==0 else b-a   
# print(smallest(3,4))     
        
# l=[1,2,3,4,5,6,7,8,9,10]
# even =list(filter(lambda x:(x%2==0) ,l))    
# print(even)       

############# QUESTION - 41   #################

# list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]  
# def max_index(x):
#     a=0
#     max=0
#     max_element=[0]
#     for i in range (len(list)):
#         count=0
#         for j in range (len(list[i])):
#             count+=1  
#         if max<count:
#             max=count
#             max_element[a]=(max,list[i])
#     return max_element
# print(max_index(list))
        
        
        
#############  QUESTION -40 #############


# def integer_square(x):
#     # change the type of integer type list
#     l=str(x)
#     for i in range(len(l)):
#         print(int(l[i])**2,end="")
# a=9119
# integer_square(a)
        
#############  QUESTION -39  #############  

# list=[23,54,-65,-43,53,32,2,21]
# def max_in_list(x):
#     max=x[1]
#     min=x[1]
#     for i in range (len(x)):
#         if max<x[i]:
#             max=x[i]
#         if min>x[i]:
#             min=x[i]
#     return max , min   
        
# print(max_in_list(list))   

 
        
################  QUESTION - 38   ################      
        
        
# def divisibilty_test(x):
    
#     for i in range(2,min(x)):
#         factor=0
#         factors=[]
#         for j in range (len(x)):
        
           

        
# def reverse(x,n):
#     if n==0:
#         return x[0]
        
#     else:
#         print(x[n],end="")
#         reverse(x,n-1)
# x= "AMERICA"
# n=len(x)-1
# reverse(x,n)


# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6) 
        
        
        
# def me(**kwargs):
#     print("my name is :" + kwargs["name"])
#     return(" age & status is :"+ kwargs["age"]+ kwargs["status"])
    
# print(me (name ="kajal",age="20", status="student"))
        
############  PASCAL TRIANGLE   ############
        
# n=5
# i=1
# while i<=5:
#     for j in range (n+1,i,-1):
#         print(" ",end="")
#     c=1
#     j=1
#     while j<=i:
#         print([c],end="")
#         c=c*(i-j)//j
#         j+=1
#     i+=1
#     print()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        