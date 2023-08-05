# list=[2,3,4,5,6,6,7,7,87,6,454,433] 
# list2=[]                                #1
# for i in range (len(list)-1,0,-1):
#     list2.append(list[i])
# print(list2)    


# list=[]
# n = int(input(" enter the total items in list: "))
# i=0
# while i<=n:
#     x = int(input(" enter the items in list: "))
#     list.append(x)
#     i+=1
# for j in range (len(list)):
#     min=list[0]
#     for k in range (len(list)):
#         if min>list[k]:
#             min=list[k]
#     c=min
# l=[0]*5                         # insertion sort
# for i in range (len(l)):
#     a=int(input())
#     l[i]=a
# for j in range (1,len(l)):
#     t=l[j]
#     k=j-1
#     while k>=0 and t<l[k]:

#     min=list[j]
#     list[j]=c
# print(list)

# list=[2,3,4,5,6,6,7,7,87,6,454,433]


# for i in range (len(list)):
#     for j in range (len(list)-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)



# sum=0
# n= int(input (" enter the total number: "))
# i=1
# list=[0]*n
# for i in range (len(list)):
#     x=int(input (" enter the total number: "))
    
#     list[i]=x
#     i+=1
# print(list)

# for j in range (len(list)):        #mean
#     sum +=list[j]
#     mean=sum//n
# print(mean)


# if n%2!=0:                         # median
#     index=(n+1)//2
#     median= index
# else:
#     index =(n//2)
#     index2=(n//2+1)//2
#     median= (index+index2)//2
# print(median)

# mode= (3 * median) -(2 * mean)     # mode
# print(mean, median , mode)

#_____________________________________________________________________


                      #3
# list=[3,6,7,5,10]
# n=len(list)
# list1=[0]*n-1
# r=int(input("enter the distance :"))
# for i in range(len(list)):
#     list2=[0]*n
#     list3=[0]*n
    
#     for j in range (len(list)):
#         if r-1==j:
#             list1.append(list[j])
            
#     for k in range (r,len(list)):
#         list2.append(list[k])
        
#     for g in range (len(list)):
#         if list[g]==list1[-1]:
#             break
#         else:
#             list3.append(list[g])
   
#     list2.extend(list3)
#     list=list2
# print(list1+list)

#__________________________________________________________________________



# n= int(input (" enter the total number: "))
# i=1
# list=[0]*n
# for i in range (len(list)):
#     x=int(input (" enter the total number: "))
    
#     list[i]=x
#     i+=1
# print(list)          #4 ( duplicate )

# list=[1,2,3,4,5,2,3,4]
# for i in range(n):
#     for j in range(n-1):
#         if list[j+1]<list[j]:
#             list[j+1],list[j]=list[j],list[j+1]

# count=0
# for i in range (n):
    
#     for j in range (n):
#         if j!=i:
#             if list[i]==list[j]:
#                 count+=1
# if count>=1:
#     print(list[i],"yes list have dublicates" )       
                
            

    




#____________________________________________________________________________



n=int(input("list: "))          #5
list=[0]*n
i=0
while i<n:
    x=int(input(" enter the elements of list:"))
    list[i]=x
    i+=1
m=int(input("list1 :"))
list1=[0]*m
i=0
while i<m:
    x=int(input(" enter the elements of list:"))
    list1[i]=x
    i+=1

    
j=0
z=0
l=[0]*8
while i<(n+m):
    if n>m:
        l[z]=list[j]
        j+=1
    elif m>n:
        l[z]=list1[i]
  ist[i]<list1[j]:
        l[z]=list[i]
        i+=1
    elif list[i]>list1[j]:
        l[z]=list[j]
        j+=1
    z+=1
    

print(l)        
        

print(list)
print(list1)
print("merging of two list:", list+list1)
            
# list =[3,6,7,5,10,2,9,6]          #6
# list1=[]
# sum=12
# for i in range (len(list)):
#     for j in range (len(list),0):
#         if list[i]+list[j]==sum :
#             b=list[i],list[j]
#             if b not in list1:
#                 list1.append(b)
# print(list1)
            

        
# print(list1+list)
# list1.extend(list)
# print(list1)



# list0 =[3,6,7,5,10,2,9,6]  
# list1=[4,5,6,7]
# t=[]
# for i in range (len(list1)):             #7
#     if list1[i] in list0:                 #intersection
#         t.append(list0[i])
# print(t)

# list3=set(list0+list1)                    # union
# print(list(list3))



# list =[3,6,7,5,10,2,9,6]             # 8
# list1= [4,6,3,2,8,9]
# for i in range (len(list)):
#     for j in range (len(list)):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
# for k in range (len(list1)):
#     for l in range (len(list1)):
#         if list1[k]<list1[l]:
#             list1[k],list1[l]=list1[l],list1[k]
# s,t=len(list),len(list1)

# for i in range (len(list)):
#     for j in range (len(list)):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
# for k in range (len(list1)):

#     for a in range(s):
#         if s%2==0:
#             index=((s//2)+((s//2)+1))//2 
#             median= list[index]
#         else:
#             index=(s+1)//2
#             median=list[index]
#     for a in range(t):
#         if t%2==0:
#             index=((t//2)+((t//2)+1))//2 
#             median1= list1[index]
#         else:
#             index=(t+1)//2
#             median1=list1[index]

# print(median, median1)



# n=int(input("enter the size :"))            #list1

# list=[0]*n
# i=0
# while i<n:
#     x=int(input(" enter the elements of list:"))
#     list[i]=x
#     i+=1

#                                        #list2
# a=int(input("enter the size :"))

# list1=[0]*a
# i=0
# while i<a:
#     y=int(input(" enter the elements of list:"))
#     list1[i]=y
#     i+=1
# list=list+list1                 #sorting
# l=(n+a)
# for i in range (l):
#     for j in range (l):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]



# print(list)

# if l%2!=0:                         # median
#     index=(l+1)//2
#     median= index
# else:
#     index =(l//2)
#     index2=(l//2+1)//2
#     median= (index+index2)//2
# print(median)




# list =[3,6,7,5,10,2,9,6]   
 
# for i in range(len(list)-1):
#     min=list[i]
#     j=0
#     while j<=i+1:
#         if min>list[j]:
#             min=list[j]
#         if min >list[i]:
#             min,list[i]=list[i],min
        
#         j+=1
    
    
#     #for k in range (0,)       
# print(min)          
        
        




# l=[9,4,15,1,8,6,5,3,15,2,4,6,1,4,2,6,3]      #4
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if l[j+1]<l[j]:
#             l[j+1],l[j]=l[j],l[j+1]
# print(l)
# list=[]
# for h in range (len(l)-1):
    
#     if l[h]==l[h+1]:
#             list.append(l[h])
#             dublicates=[]
#             for g in range (len(list)-1):
#                 if list[g]!=list[g+1]:
#                     dublicates.append(list[g])
                    
# dublicates.append(list[-1])        

# print(list)
# print(dublicates)


#binary -search

0
# i=0
# randomn=int(input("enter the size :"))

# list=[0]*n
# i=0
# while i<n:
#     x=int(input(" enter the elements of list:"))
#     list[i]=x
#     i+=1

# user=int(input("enter a no.: "))
# j= ="no"
# #n=len(list)
# k=n-1
# while j<k and random !="yes":
#     mid=j+k//2
#     if user > list[mid]:
#         j=mid+1
#     if user<list[mid]:
#         k=mid-1
#     if list[mid]==user:
#         random="yes"
#     i+=1
# print(random,"indexing of user no.: {0}".format(user))


# l=[0]*5                         # insertion sort
# for i in range (len(l)):
#     a=int(input())
#     l[i]=a
# for j in range (1,len(l)):
#     t=l[j]
#     k=j-1
#     while k>=0 and t<l[k]:
#         l[k+1]=l[k]
#         k-=1
#     l[k+1]=t


#_____________________________________________________________________


"ASSIGNMENT-3RD CODING ASSIGNMENT" "6 SEP "



###############  QUESTION - 1  ##########



# i=1
# sum=0
# while i<1000:
#     if i%3==0 or i%5==0:
#         sum+=i
#         #print(i,end=" ")
#     i+=1
#     print()
# print(sum)
    



###############  QUESTION - 2    ##########


# x,y,z=0,1,1
# n=int(input())
# i=0
# sum=0
# while i<=n:

#     if z%2==0 and sum<=4000000:
#         sum+=z
#     x=y
#     y=z
#     z=x+y
#     i+=1

#print(sum)

##############  QUESTION - 3   ###########


# num=600851475143
# i=2
# list=[]
# while i<=num**0.5:
#     if num%i==0:
#         j=1
#         count=0
#         while j<=i:
#             if i%j==0:
#                 count+=1
#             j+=1
#         if count==2:
#             list.append(i)
#     i+=1
# print(list)
# print(list[-1])


###########   QUESTION -4  ##############


# i=999
# max=0
# while i>=100:
#     j=999
#     while j>=100:
#         mul =j*i
#         n=mul
#         rev=0
#         while mul>0:
#             rem=mul%10
#             rev=(rev*10)+rem
#             mul//=10
#         if n==rev:
#             if max< rev:
#                max=rev
#             break
#         else:
#             j-=1
    
#     i-=1
# print(max)



   
   
#################   question - 5      ############
        
# j=2
# n=1
# l= int(input("enter the last limit: "))
# hcf=1
# while j<=l:
#     i=1
    # while i<=min(n,j):
    #     if n% i == 0 and j % i == 0:
    #         hcf = i
    #     i+=1
    # lcm = (j*n)//hcf
#     n=lcm
#     j+=1
    
# print(hcf)
# print("the smallest no divisible by 1 to",l,"is", lcm)
# # # LCM formula


############### QUESTION  - 6    ##########

# i=1
# sum=0
# sum_sq=0
# l= int(input("enter the last limit: "))
# while i<=l:
#     square =i**2
#     sum_sq+=square
#     sum+=i
#     i+=1
# difference=sum_sq - (sum)**2
# print("the difference between sum_sq and sum", difference)



#############   queation -7    #############
# p=1
# i=2
# b=int(input())
# while True:
#     if p==b+1:
#         break
#     elif i==2:
#         print(p,i)
#         p+=1
#     elif i%2!=0:
#         j=3
#         count=0
#         while j**2<=i:
#             if i%j==0:
#                 count+=1
#             j+=1
#         if count==0:
#             if p==b:
#                 print(p,i)
#             p+=1
#     i+=1

# 


# list=[5,3,4,6,7]
# for i in range (len(list)):
#     for j in range (1,len(list)):
#         hcf=1
#         for k in range (1,min(1,list[i],list[j])):
#             if i%k==0 and j%k==0:
#                 hcf=k
        
#         lcm=list[j]*list[i]//hcf
#         print(hcf,lcm)


# t= int(input())
# for i in range (t):
#     N=int(input())
#     A=list(map(int,input().split()))
#     count=0
#     for i in range(len(A)):
#         for j in range(i+1,len(A)):
#             hcf=math.gcd(A[i],A[j])
#             #for k in range (1,min(A[i],A[j])+1)):
                
#             lcm=A[i]*A[j]//hcf
#             print(hcf,lcm)
    
#             if hcf==lcm:
#                 count+=1        
        
#  print(count)




























#from multiprocessing.pool import ApplyResult


# a="ApplyResult"
# for i in range (len(a)):
#     print(ord(i))


# # cook your dish here
# for _ in range(int(input())):
#     n=int(input())
#     s=input()
#     l=list(s)
#     l1=[]
#     for i in range(0,n-1,2):
#         temp=l[i]
#         l[i]=l[i+1]
#         l[i+1]=temp
#     for e in l:
#         initial=ord(e)-97
#         print(ord(e),chr(97))
#         final=122-initial 
#         l1.append(chr(final))
#     print("".join(l1))

# def isprime(num):
#     for n in range(2,int(num**0.5)+1):
#         if num%n==0:
#             return False
#     return True
# print(isprime(7))
# print(isprime(8))























