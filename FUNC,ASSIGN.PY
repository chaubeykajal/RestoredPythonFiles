########## FUNCTION ASSIGNMENT -1 ###########

##########  QUESTION -1  ########

# def max_3(x,y,z):
#     if x>y:
#         max=x
#         if max<z:
#             max=z
#     else:
#         max=y
#         if max<z:
#             max=z
#     return(max)
# print(max_3(4,5,9))


#############  QUESTION =2  ###########


# list=(8, 2, 3, 0, 7)
# def sum(x):
#     add=0
#     for i in range (len(x)):
#         add+=x[i]
#     return(add)
# print(sum(list))

#############  QUESTION =3  ###########

# list= (8, 2, 3, -1, 7)

# def mul(x):
#     prod=1
#     for i in range (len(x)):
#         prod*=x[i]
#     return(prod)
# print(mul(list))


#############  QUESTION =4  ###########


# def reverse(x):
#     new=""
#     for i in range (len(x)-1,-1,-1):
#         new+=x[i]
#     return new
# string= "1234abcd"
# print(reverse(string))


############   QUESTION = 5 ###########

# def factorial(x):
    
#     i=x
#     fac=1
#     while i>=1:
#         fac*=i
#         i-=1
#     return fac
# x=int(input())
# print(factorial(x))


############   QUESTION = 6 ###########


# def num_alpha(u,l,n):
#         if n>=l and n<=u:
#             return ("yes")
#         else:
#             return ("no")
# print(num_alpha(2,15,3))
  
     

############   QUESTION = 7 ###########           

# def alphabet(x):
#     count_u=0
#     count_l=0
#     for i in range (len(x)):
#         if x[i]>="A" and x[i]<="Z":
#             count_u+=1
#         elif x[i]>="a" and x[i]<="z":
#             count_l+=1
#     return ("total upper alphabet in {0}".format(x),count_u,
#     "total lower alphabet in {0}".format(x),count_l)
# a='The quick Brow Fox Jumps Over the Lazy Dog.'
# print(alphabet(a))

############   QUESTION = 8 ########### 


# def unique(x):
#     uni=[]
#     for i in range(len(x)):
#         if x[i] not in uni:
#             uni.append(x[i])
#     return uni
# list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(unique (list))

############   QUESTION = 9 ########### 

# def check_prime(x):
#     i=2
#     count=0
#     while i<=x**0.5:
#         if x%i==0:
#             count+=1
#         i+=1
#     if count>0:
#         return("not a prime number")
#     else:
#         return("prime number")
# n=int(input("enter :"))
# print(check_prime(n))
        
############   QUESTION = 10  ###########    

# def even_no(x):
#     n=len(x)
#     list=[]
#     for i in range (len(x)):
#         if x[i]%2==0:
#             list.append(x[i])
#     return list
# print(even_no( [1, 2, 3, 4, 5, 6, 7, 8, 9]))
            


############   QUESTION = 11  ###########  


# def perfect_no(x):
#     sum =0
#     for i in range (1,x):
#         if x%i==0:
#             sum+=i
#     if sum==x:
#         a=str(x)+"it is a perfect number"
#     else:
#         a=str(x)+"not a perfect number"
#     return a
# for j in range(1,101):
#     print(perfect_no(j))



############   QUESTION = 12  ###########  


# def palindrome(x):
#     rev=0
#     y=x
#     while x>0:
#         rem=x%10
#         rev=(rev*10)+rem
#         x//=10
#     if y==rev:
#         print("yes, palindrome",y ,":",rev)
#     else:        
#         print("not a palindrome",y,":" ,rev)
# palindrome(151151)



###########  QUESTION = 13  #############





# def pascal_triangle(n):
#     #n=int(input())
#     i=1
#     while i<=n:
#         j=n
#         while j>=i:
#             print("-",end=" ")
#             j-=1
#         s=1 
#         j=1   
#         while j<=i:
#             print([s],end=" ")
#             s=s*(i-j)//j
#             j+=1
#         i+=1
#         print()
# pascal_triangle(5)


###########  QUESTION = 14 #############


# def pangram(x):

#     alph="abcdefghijklmnopqrstuvwxyz"
#     cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     count=0
#     list=[]
    
#     for i in  range (len(alph)):
#         if alph[i] not  in l:
#             if cap[i] not in l: 
#                count+=1
#                list.append(i)
#     if count>0:
#         print(" total missing elements aree:",count,"and missing elements are:",list)
#     else:
#         print("all are here")
      
    
# l= "the Quick broWn fOx Jumps over the laZy doG"
# pangram(l)


###########  QUESTION = 15  #############



# def string(n):
#     for i in range (n):
        


###########  QUESTION = 16  #############

# def square(n):
    
#     list=[0]*(n)
#     a=0
#     for i in range (1,n+1):
#        list[a]=(i**2)
#        a+=1
#     return list
# print(square(30))
       

###########  QUESTION = 17  #############

# def bold(x):
#     return "<b>" + x +"<b>"
# print(bold("kajal"))


# def my_fun(x):
#     if x==1:
#         return print
#     if x==0:
#         return sum
# a=my_fun(0)
# print(a)


# def rev(fun):
#     fun("yes")
# executor(print)
        

###########  QUESTION = 19  #############



# def sum(a,b):
#     return a+b
# def mul(c):
#     return sum(int(input()),int(input())) *c
# print(mul(5))


########### QUESTION =20 

# def local_count():
#     name="kajal"
#     profession ="student "
#     age ="21"
#     category="general"
#     print(name +profession)
# print(local_count.__code__.co_nlocals)     # (funcation name__code__.co_nlocals)


   
































