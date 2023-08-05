# count=0
# i=2
# def prime_no(x,i):
#     global count
#     if  i==x+1:
#         if count>1:
#             return ("it is not a prime no:",x,count)
#         else:
#             return ("it is  a prime no:",x )
#     else:
#         if x%i==0:
#             count+=1
#             return prime_no(x,i+1) 
#         else:
#             return prime_no(x,i+1) 
# a=int(input())
# print(prime_no(a,i))


# def prime(x,i):
#     global count
#     if i==x**0.5:
#         if count>1:
#             print("not a prime ")
#         else:
#             print("prime")
#     else:
#         if x%i==0:
#             count+=1
    
#     return prime(x,i+1)
    
    
    
    
# count=0   
# a= int(input())
# print(prime(a,1))








###########  QUESTION --14  ##########

# even=[]
# odd=[]
# def even_odd(x):
#     global i 
#     if i==x+1:
#         return even, odd
#     else:
#         if i%2==0:
#             even.append(i)
#             i+=1
#             return even_odd(x)
#         else:
#             odd.append(i)
#             i+=1
#             return even_odd(x)
# i=int(input("enter the initial point of range :"))
# n=int(input("enter the limit: "))
# print(even_odd(n))



####### binary to decimal     


# def binary(x):
#     if x==0:
#         return 
#     else:
#         n=x%2
#         (binary(x//2))
#     return(n)
# a=int(input())
# print(binary(a))





# a=[[1,2,3],
#    [2,3,4],
#    [4,5,6]]
# b=[[1,2,3],
#    [3,4,0],
#    [1,2,2]]
# list=[]
# for i in range(len(a)):
#     sum =0
#     l=[]
#     for j in range (len(a)):
#         for k in range (len(a[i])):
#             mul =a[j][k]*b[k][j]
#             sum+=mul
#         l.append(sum)
#     list.append(l)







def f(x):
    if x==10:
        print(x)
        return 10
    f(x+1)
    print(x)
    
    
    
    
print(f(1))



def power(a,y):
    if y==0:
        return 1
    if y==1:
        return a
    if y%2==1:
        return a*(pow(a,y//2)*pow(a,y//2))
    else:
        return pow(a,y//2)*pow(a,y//2)
    
print(power(2,5))



def rev(x,i):
    if i==len(x)-1:
        print(x[i])
        return 
    rev(x,i-1)
a="kajal"
print(rev(a,1))






def palin(x,i,j):
    
    if i>=j:
        return True
    if x[i]!=x[j]:
        return False
    return palin(x, i+1,j-1)
a="madam"
print(palin(a,0,len(a)-1))





t=int(input())
for i in range (t):
    n=int(input())
    a=[]
    b=[]
    
    c=list(map(int,input().split()))
    maximum=max(c)
    for j in range (len(c)):
        if c[0]==maximum :
            print(-1)
            
        elif c[j]!=maximum :
            a.append(c[j])
        elif c[j]==maximum :
            d=c[j:]
            b.append(d)
            
print(a,b)



















































