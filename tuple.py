# new=[]
# list=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# for i in list:
#   if i!=():
#     new.append(i)
# print(new)
    
# string="python 3.0"
# print(tuple(string))

# mul=1
# tuple=(2, 4, 8, 8, 3, 2, 9)
# for i in tuple:
#     mul*=i
# print(mul)

# new=()
# tuple=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# for i in range (len(tuple)):
#     sum=0
#     for j in i:
#         sum+=j
#         averge=sum/len()
#         new.add()
# print(new)

#----------------------------------------------------------------------------------------------

# str1=[1,4,5,3,6,4]                          #1
# def reverse_s(x):
#      #return(x[::-1])           # reverse funtion is not working?
#      return(x.reverse())
# print(reverse_s(str1))


# str3=[1,4,5,3,6,4]                        #2
# print(reverse_s(str3))
# def factorial(x):
#     fac=1
#     i=1
#     while i<=x:
#         fac*=i
#         i+=1
#     return fac
# print(factorial(5))   
        
# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)        # how it is working -factorial (n-1)
# n=int(input("number: "))
# print(factorial(n))
           
       
# k=53                                   #3
# def membership(x):
#     if k in range(20,x):
#         return "yes"
#     else:
#         return "no"
# n=int(input("enter the no.: "))
# print(membership(n))



# k=3
# if k in range(0,5):
#     print("y")
# else:
#     print("n")

# string="KAJal CHatuVEdI"                     #4
# def alphabet(x):
#     count_l=0
#     count_u=0
#     for i in x:
#         if i.isupper():
#             count_l+=1
#         elif i.islower():
#             count_u+=1
#     print(count_l,count_u)

# alphabet(string)
 
 
# def unique(x):                                  #4
#     new=[]
#     for i in range(len(x)):
#         if x[i]not in new:        
#             new.append(x[i])
#     return new    
# n= [12,3,45,21,23,21,45,34,23,54,54]
# print(unique(n))


# def max_number(x,y):                      #5
#     if x>y:
#         return " maximum number is :", x
#     else:
#         return " max number is:" ,y
# print(max_number(45,36))    


# def max_number(x,y,z):              #6
#     if x>y:
#         if x>z:
#             return " maximum number is :", x
#         else:
#             return "max:" ,z
    
#     else:
#         if y>z:
#             return " max number is:" ,y
#         else:
#             return "max",z
# print(max_number(45,36,75))   

# def multiplication(x):
#     mul=1
#     for i in range (1,x):
#         mul*=i 
#     return mul
# print(multiplication(4))


# def submission(x):                  #8
#     sum=0
#     for i in x:
#         sum+=i
#     return(sum)
# n=n= [2,3,4,2,2,1,5,4,3,5,4]
# print(submission(n))
            

# def prime(x):                      #9
#     count=1
#     for i in range (2,x+1):
#         if x%i==0:
#             print(i, end=" ")
#             print()
#             count+=1
#     if count<=2:
#         return ("prime")
#     else:
#         return ("not prime")
# n = int(input(" take any number: "))
# print(prime(n))
        

# def even_number(x,y):           #10
#     even=[]
#     for i in range (x,y):    
#         if i %2==0:
#             even.append(i)
#     return(even)
# print(even_number(10,50))


# def perfect(x):                    #11
#     sum=0
#     for i in range (1,x):
#         if x%i==0:
#             sum+=i
#     if sum==x:
#         return "perfect number" 
#     else:
#         return "not perfect"
# print(perfect(13))


# def palindrome(x):
    #if x==int:
    # rev=0
    # y=x
    # while x>0:                   # for integer
    #     rem= x%10
    #     rev=(rev*10)+rem
    #     x//=10
    # return rev==y
    # #elif x==str:
#     for j in x:                     # for string
#         z=x[::-1]
#     return x==z
# print(palindrome("madam"))



for i in range(int(input())):
    n=int(input())
    s=input()
    d={}
    for j in range (n):
        for k in range (1,n):
            a=s[j:k+1]
            if a not in d:
                d[a]=1
            elif a=="":
                pass
            else:
                d[a]+=1
    print(d)
    l=[]            
    for k,m in d.items():
        j=len(k)
        #if m>=1:
            if l>1 and len(k)>0:
                mx=0
                l.append(len(k)-1)
            else:
                l.append(m)
    print(max(l))           