# a=[10,50,40]       #1
# b=[2,5,3]
# i=0
# sum=0
# c=0
# while i<len(b):
#     sum+=b[i]
#     s=a[i]*b[i]
#     c+=s
#     i+=1
# print(c/sum)

# a=[10,50,40,6,7,3,8]    #2
# b=[2,5,3,5,4,10,50]
# for i in  (a):
#     for j in b:
#         if i==j:
#             print(True,(i,j))


# list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']    #3
# new=[]
# for i in range (len(list)):
#     if i!=4 and i!=0 and i!=5:
#         new.append(list[i])
# print(new)
    
# from random import shuffle                #4
# list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(list)
# print(list)



# list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]  #5
# l= len(list1) 
# for i  in range (0,l):
#     for j in range (0,l-1):
#         if list1[j][1]>list1[j+1][1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)


# list=[1,2,3,4,5,6,7,8,9,10,11,12]               #6
# new=[]
# for i in range (len(list)):
#     new.append(list[i]**2)
# print(new[0:5])
# print(new[-5:])



# a=[1,2,3]                           #7
# new=[]
# for i in range (len(a)):
#     for j in range  (len(a)):
#         for k in range(len(a)):
#             if (a[i]!=a[j] and a[j]!=a[i] ) and (a[k]!=a[j] and a[j]!=[k]) and (a[i]!=a[k]and a[k]!=a[i]):
#                 b=(a[i],a[j],a[k])
#                 new.append(b)
# print(new)  


# list1 = [1, 3, 5, 7, 9]           #8
# list2=[1, 2, 4, 6, 7, 8]
# list3=set(list1)-set(list2)
# list4=set(list2)-set(list1)
# print(list(list3)+list(list4))

# list1 = [1, 3, 5, 7, 9]          #9
# for i in range (len(list1)):
#     print(i,list1[i])

# list=["p","y","t","h","o","n"]    #10
# string=""
# for i in list:
#     print(i,end="")

        
# list = [[2,4,3],[1,5,6], [9], [7,9,0]]     # 11
# new=[]
# for i in list:
#     for j in i:
#         new.append(j)
# print(new)
   
# list=["p","y","t","h","o","n"] 
# list1 = [1, 3, 5, 7, 9]                  #12
# list.extend(list1)
# print(list)
# list=list+list1
# print(list)

  
# list=[1, 3, 5, 7, 9]           #13
# import random
#print(random.choice(list))


# a=[9,44,10,77,88,66,79] 
# max=a[0]
# min =max   
# s_max= max
# i=0
# for i in range(len(a)):
#     if a[i]>max:
#         max=a[i]
#     if min>a[i]:
#         min=a[i]
#     if max>s_max and s_max<a[i]:
#         s_max=a[i]
#     i+=1
# print(max,s_max,min)
    
        
        
        
# list = [10,10,10,10,20,20,20,20,40,40,50,50,30]  #15
# count=1 
# new=[]
# for i in range(len(list)-1):
#     if list[i]==list[i+1]:
#         count+=1
#     else:
#         b=count,list[i]
#         new.append(b)
#         count=1
        
# print(new)


# list=["p","q"]                    #16
# list1=[]
# n=int(input('enter the number:'))
# for i in range(1,n+1):
#     for j in range(len(list)):
#         b=list[j]+str(i)
#         list1.append(b)
# print(list1)    


# num=int(input(" enter a number: "))        #  prime factor of a number
# i= 2
# while i<=num:   #12
#     if num%i==0:     
#         j=2
#         count=0
#         while j<=i:   #1<=2
#             if i%j==0:     #2%2
#                 count+=1
#             j+=1
#         if count==1:
#             print(j-1,num)
#     i+=1
        
# list=[1, 10,2,8,3, 5, 7, 9]       #17
# max=0
# sec=0
# for i in list:
#     if i>max:
#         sec=max
#         max=i
#     else:
#         if max>sec and sec<i:
#             sec=i
# print(max,sec)
        

# for i in range(10):
#     if i==5:
#         pass
# else:
#     print(i)

    
# x=0                                #18
# y=1
# z=0
# num=int(input(" enter the no: "))
# item=1
# while item<=num:
#     print(z)
#     x=y
#     y=z
#     z=x+y
#     item+=1
    

# list=[1, 10,2,8,3, 5, 7, 9]              #19

# n= int(input("enter a number where from you want to start: "))
# count=0
# for  i in range (n,len(list)-2):
#     count+=1
#     print(list[i],count)
# print(count)    
      
# def count_list_item(x,s,e):
#     count=0
#     for i in x:
#         if s<=i<=e:
#             count+=1
#     return count
# list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print(count_list_item(list,20,40))


# test_list = [5, 6, 3,8,2, 1, 7, 1]           #20
# sublist = [3, 8, 2] 
# def is_sublist(x,y):
#     for i in x:
#         if y in x:
#             subset="True" 
#         else:
#             subset="False"
#     return subset
# print(is_sublist(test_list,sublist))
            


# lowest2 = None
# for i in list1[1:]:	
# 	if list1[i] < lowest:
# 		lowest2 = lowest
# 		lowest = list1[i]
#     elif lowest2 is None or lowest2 > i:
# 		lowest2 = list1[i]
			
# print("Smallest element is:", lowest)

# print("Second Smallest element is:", lowest2)

# list = [5, 6, 3,8,2, 1,45,98, 7, 1]              #21
# list1=[1,2,3,4,5,6,7,9,45,98]
# new=[]
# for i in list1:
#     if i in list:
#         new.append(i)
# print(new)


# list=[0,1,2,3,4,5]                               #22
# for i in range (0,len(list)-1,2):
#     list[i],list[i+1]=list[i+1],list[i]
    
# print(list)
    

# list=[11,22,33,44,55,5,0]        #23
# for i in list:
#     print(str(i),end="")


#list=["a","b","c"]

# for i in range (len(list)):
#     list1=[]
#     for j in list:
#         list1.append([j])
#     for k in range (len(list)-1):
        
#         b=[list[k],list[k+1]]
        
#         list1.append(b)
#     for m in range (len(list)-2):
#         g=[list[m],list[m+1],list[m+2]]
#         list1.append(g)
# for l in range (len(list)-1):
#     list[l],list[l+1]=list[l+1],list[l]
# print(list)
# c=[list[l],list[l+1]]
# list1.append(c)
#print(list1)


# list=[1,2,3]
# list1=[]
# for i in range (len(list)):
#     list2=[]
#     for j in range (list[i]):
#         if list[i]!=list[j]:
#             b=list[j],list[i]
#             list1.append(b)
        
# print(list1)



# l=[1,2,3]
# lists = [[]]
# for i in range(len(l) + 1):
#     for j in range(i):
#         print(l[j: i])
#         lists.append(l[j: i])
# print(lists)  
  
# list=["p","q"]
# def add_list(x,l):
#     #l=int(input("enter the number: "))

#     i=1
#     list1=[]
#     while i<=l:
#         for j in range (len(list)):
#             b=x[j]+str(i)
#             list1.append(b)
    
#         i+=1
#     return list1
# n=int(input("enter the number: "))

# print(add_list(list,n))
        
# s="mental"
# print(format(id(s)))
  
  
  
# l=[944,5,6,67,34,21,12,13]
# min=l[0]
# s_min=l[-1]
# max= l[0]
# s_max=l[-1]
# for i in range (len(l)):
#     if max<l[i]:
#         s_max=max
#         max=l[i]
#     elif max==s_max:
#         s_max=l[i]
#     else:
#         if s_max<l[i]:
#             s_max=l[i]
#     if min>l[i]:
#         s_min=min
#         min=l[i]
#     elif min==s_min:
#         s_min=l[i]

#     if s_min>l[i]:
#         s_min=l[i]
        
# print(s_min,min)
# print("max:",max,"s_max",s_max)
  
  
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think', 
#     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']  
# j=0
# for i in range(len(word_list)):
#     for j in range (len(word_list)(i)):
#         print(word_list[i][j])
    
  
  
# num= int(input(" enter the number:"))
# i=1
# ele=0
# while True:
#     if ele==num:
#         break 
#     else:
#         count=0
#         j=1
#         while j<=i**0.5:
#             if i%j==0:
#                 count+=1
#                 if count>1:
#                     break
#             j+=1
#             if count==1:
#                 print(i)
#                 ele+=1
#         i+=1
        
# a=int(input("enter the number:"))
# max=int(input("entert the number:"))
# sec=int(input("enter the number:"))

# third=int(input("enter the numner:"))
# if max<sec:
#     max,sec=sec,max
#     if max<third:
#         third,sec,max=sec,max,third
#     else:
#         sec,max,third=max,third,sec
# elif  max<third:
#     sec,third=third,sec
# i=0
# while i<a-3:
#     z=int(input("enter ethe number:"))
#     if max<z:
#         third=sec
#         sec=max
#         max=z
#     elif sec<z:
#         third=sec
#         sec=z
#     elif third<z:
#         third=z
#     i+=1
# print(max,sec,thirword_list = ['be','have','do','say','get','make','go','know','take','see','come','think', 
#     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']  
# j=0
# for i in range(len(word_list)):
#     for j in range (len(word_list)(i)):
#         print(word_list[i][j]d)  



# list=[]                ##  check weather a number  is in a list or not. 

# n=int(input("enter the total number: "))
# i=1
# while i<=n:
#     x= int(input(" enter the items: "))
#     list.append(x)
#     i+=1
# print(list)
# user_number= int(input("enter the number: "))
# for j in range(len(list)):
#     if list[j]==user_number:
#         print("yes {0} in list at index{0}".format(user_number,i))
#         break
#     elif list[j]==list[-1]:
#         if list[-1]!=user_number:
#             print(" not in list")
    
 
# list=[]
# items=int(input("enter the number:"))
# max=int(input("enter the number:"))
# i=1
# while i<=items-1:
#     x=int(input("enter the number:"))
#     if max<x:
#         max,x=x,max
#         list.append(x)
#     else:
#         list.append(x)
        
    
#     i+=1
# list.append(max)
# print(list)

 
# n= int(input(" enter the total items which you want:"))
# i=2         
# while  i<=n:
#     if i==2 or i==3  or i==7 or i==5:
#         print(i)
#     elif i%2==0 or  i%3==0 or i%5 or i%7==0:
#         pass
#     else:
#         print(i)
#     i+=1

  
# n= int(input("enter the items no:"))
# i=1

# list=[]


# while i<=n-1:
#     x= int(input("enter the no: "))
#     list.append(x)
#     i+=1
# list=[34,56,43,76,87,12]
# for j in range (len(list)):
#     for k in range(len(list)):
#         if list[j]>list[k]:
#             c=max
#             max=list[k]
#             list[k]=c
            
# print(list)





# g=89
# print(format(id(g),"g"))
# print(id(g))



#-----------------------------------------------------------------------  


# count = 5
# def some_method():
#     global count
# 	count = count + 1
# 	print(count)
# some_method()


for i in range (int(input())):
	u=input()
	d=input()
	s_u=0
	s_d=0
	for j in range (len(u)):
		s_u += int(u[j])
		s_d+=int(d[j])
print(s_u+s_d)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  