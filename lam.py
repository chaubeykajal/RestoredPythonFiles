##### q-1

# add =lambda a: a+12
# print(add(4))

# ##### q-2 

# add =lambda a,b : a+b
# print(add(2,3)) 

# ###### q-3

# mul =lambda a,c,d,b:a*b*c*d
# print(mul(1,2,3,4))


# def mul(n):
#     return lambda a: a*n
    
# #print(mul(2))
# result=mul(3)
# print(result(8))


# ######## q-4
# list=[('English', 88,23), ('Science', 90,56), ('Maths', 97,43), ('Social sciences', 82,56)]
# list.sort(key= lambda x: x[2] )   # index 0 and 1 shows which index are arranging  
# print(list)


# ########  q-5

# models = [{'make':'Nokia', 'model':216, 'color':'Black'}, 
#           {'make':'Mi Max', 'model':2, 'color':'Gold'},
#           {'make':'Samsung', 'model': 7, 'color':'Blue'}]

# s=sorted(models,key =lambda x:x["model"])     
# print(s)

###### q - 6


# l=[1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda x : x%2 == 0,l))

# print(even)

# odd =list(filter(lambda x: x%2!=0,l))
# print(odd)


####### q -7



#l=[1,2,3,4,5,6,7,8,9]
# square= list(map(lambda x: x*x,l))
# print(square)

# l=[1,2,3,4,5,6,7,8,9 ]
# even =list(filter(lambda x:x%2==0,l))
# print(even)


# def start_with(x,n):
#     j =n.upper()
#     if x[0]==n or x[0]==j:
#         return True
#     else:
#         return False
# a= start_with("pyhton", "p")
# print(a)       
    
# n="Chaturvedi"
# c=input()
# a=c.lower()
# b=c.upper()
# start_with= lambda x: True if x[0]==a or x[0]==b else False
# print(start_with(n))
    

# import datetime 
# a=datetime. datetime .now()
# print(a)

# year= lambda x: x.year
# month = lambda x: x.month 
# day= lambda x : x .day
# t = lambda x:x.time ()
# print(year(a))
# print(month(a))
# print(day(a))
# print(t(a))

# x=1
# y=0
# z=0

# fibanacci = lambda x: x


# a="kajal"
# print("")



# def factorial(n):
#     if  n==1:
#         return 1
#     else:
#         return (n*(factorial(n-1)))
# print(factorial(5))

# def fibo(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# n=int(input("enter :"))       
# for i in range (1,n+1):
#     print(fibo(i))




        
# l0=[1,2,3,4,5,6,7,8]       
# l=[1,2,3,4,5,9,10]       
# a= list(filter(lambda x:x in l, l0))  
# print(a)    
        
        
# l=[5,7,3,8,2,9,1,-1,-4,-10,-2]
# a=len(list(filter(lambda x: x%2==0,l)))
# print(a)
# b=len(list(filter (lambda x: x%2!=0 , l)))
# print(b)
        
        
# weeks=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
# l=list(filter(lambda d: d if len(d)>=7 else "", weeks ))
# print(l)         
        
        
        
        
        
        
        
        