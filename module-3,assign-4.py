#1. Draw a flowchart to find the sum of the first n natural numbers, where n is any given integer.

# n=int(input())
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
print(sum)


#2. Draw a flowchart to find the sum of the first 15 even natural numbers.


# n=int(input())
# i=1
# a=int(input())
# sum=0


# while True:
#     if a==n:
#         break
#     elif i%2==0:
#         print(i)
#         sum+=i
#         a+=1
#     i+=1
# print(sum)


#3. Construct a flowchart to show how consecutive even numbers starting from 2 are summed up until the sum just exceeds 1000 and then show the sum and the number of even numbers added.

# i=2
# sum=0
# while sum<=1000:
#     if i%2==0:
#         #print(i)
#         sum+=i
#     i+=1
# print(sum)



#4. Construct a flowchart to print the numbers below 100 that are divisible by 7.

# i=1
# while i<=100:
#     if i%7==0:
#         print(i)
#     i+=1

#5. Construct a flowchart to show how to find the product of n natural numbers.


# n=int(input())
# i=1
# mul=1
# while i<=n:
#     mul*=i
#     i+=1
# print(mul)

#6. Draw a flowchart to show how to find all even natural numbers that are divisible by 7 in a given range. (Input lower and upper limit of the range from the user)

# i=2
# n=int(input())
# while i<=n:
#     if i%7==0:
#         print(i)
#     i+=2


#7. Construct a flowchart to find the sum of the squares of the first 9 natural numbers that are divisible by 3.

# a=0
# n=int(input())
# i=1
# sum=0
# while True:
#     if a==n:
#         break
#     elif i%3==0:
#         square=i**2
#         sum+=square
#         a+=1
#     i+=1
# print(sum)


#8. Construct a flowchart to calculate the sum of the following series where n is input. 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/n

# i=1
# n=int(input())
# sum=0
# while i<=n:
#     sum+=1/i
#     i+=1
# print(sum)


#9. Construct a flowchart to show how to find the sum of all the numbers that are divisible by P but not divisible by Q within a given range. (Input lower limit, upper limit, P, and Q from the user)


# u,l,p,q=map(int,input().split())
# while l<=u:
#     if u%p==0 and u%q!=0:
#         print()
#     l+=1


#10. Draw a flowchart to show how to obtain the HCF and LCM of two numbers. (input two numbers from the user)

# x,y=map(int,input().split())
# i=1

# while i<=min(x,y):
#     if x%i==0 and y%i==0:
#         hcf=i
#     lcm=(x*y)//hcf
#     i+=1
    
# print(lcm,hcf)


#11. Draw a flowchart to show how the sum of the digits of a given number can be obtained. (Input the number from the user)
 
# n=int(input())
# s=str(n)
# sum=0
# for i in range(len(s)):
#     sum+=int(s[i])
# print(sum)


#12.  Draw a flowchart to show the logic of obtaining the reversed form of a given whole number. (Input the number from the user)

# n=int(input())
# s=str(n)
# new=""
# for i in range (len(s)-1,-1,-1):
#     new+=s[i]
# print(new)


#13.Construct a flowchart to show how the factors of a given number can be obtained. (Input the number from the user)

# n=int(input())
# i=1
# while i<=n**0.5:
#     if n%i==0:
#         print(i, n//i)
#     i+=1


#14. Construct a flowchart to show how to determine whether a given number is a perfect number.  (Input the number from the user)


# i=1
# n=int(input())
# sum=0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("yes, perfect number")
# else:
#     print("no , not a perfect number")

 
#34. Some two-digit numbers have the property that the sum of the squares of the numbers equals the sum of the squares of the numbers with reversed digits (for example, 482 + 522 + 632= 842 + 252 + 362). Construct a flowchart to show how to determine all such two-digit numbers.









#35. Construct a flowchart to determine all the permutations of some given number n. (n input from the user)


#a,b,c=map(int,input().split())
# for i in range (1,4):
#     for j in range (1,4):
#         for k in range(1,4):
#             if (i!=j!=k) and i!=k!=j :
#                 print(i,j,k)


n=5          
d={"a":5,"b":2,"c":6,"d":4,"e":3,"f":6}
s=max(d.values())
l=list(d.keys())
k=list(d.values())
for i in range (len(l)):
    if k[i]==s:
        print(l[i])
    




















































































