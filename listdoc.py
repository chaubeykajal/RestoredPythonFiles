#question -1

# grocery =["orange" , "mango", "peach"]
# for i in range (len(grocery)):
#     print(i," : ",grocery[i])

#question -2
    
# from typing import List


# list =[["g","f","g"],["i","s"],["b","e","s","t"]]
# for i in range (len(list)):
#     for j in range (len(list[i])):
#         print(list[i][j],end="")
# print()

#question -4 
        
# list2= [1,2,3,30,3,4,4,4,5,6,6]
# uni=[]
# mul=1
# for i  in range (len(list2)):
#     if list2[i]not in uni:
#         uni.append(list2[i])
# for j in range (len(uni)):
#     mul*=uni[j]
        
# print(uni)
# print(" multiply of list's unique num:",mul)

#  question -4


#num=[12,34,5,6,67,55,77,554,75]
# for i in range (len(num)):
#     for j in range (len(num)):
#         if num[i]>num[j]:
#             num[i],num[j]=num[j],num[i]
# print(num) 


# i=0
# while i<len(num):
#     j=0
#     while j<(len(num)-1) :
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]   
#         j+=1
#     i+=1
# print(num)
# print("max number in list(num):", num[-1])
# print("second maximum number in list(num): " ,num[-2])
# print("third maximum number in list(num): " ,num[-3])


# question - 9

# num= [12,33,74,45,108,63,48,84]
# max=0
# min=56
# for i in range (len(num)):
#     if num[i]>max:
#         max=num[i]
#     if num[i]<min:
#         min=num[i]    
# print(max,min)

# min=67

# question -11

#num= 9119

# for i in range (len(str)):
#     d=(int(str[i])*int(str[i]))
#     print(d,end="")

# a=list(str(num))
# print(a)

# s= str(num)
# l=list(s)
# print(l)

#question  -13

# num= [1,1,2,3,4,4,5,6,7,7,8,9,9]
# list2=[]
# for i in range (len(num)-1):
#     #for j in range (len(num)):
#         count=1
#         if num[i]==num[i+1]:
#             count+=1
#             d=count,num[i]
#         if num [i]not in list2:
#             list2.append(d)
#             list2.append(num[i])
# print(list2)
        

# question -13
# num= [1,1,2,3,4,4,5,6,7,7,8,9,9]        #not solve
# list2=[]
# f=[]
# for i in range (len(num)-1):

#     count=1
#     if num[i]==num[i+1]:
#         count+=1
#         #f.append(num[i])
#         d=count,num[i]
#     else:
#        if count<2:
#            list2.append(num[i])
        
#     if  d not in list2:
#         list2.append(d)
    
# #print(f)                  
# print(list2)

#quesrtion  -16

# num=[[0],[12,13,45],[67,67,344,34,34]]
# n=[]
# for i in range (len(num)):
#     count=0
#     for j in num[i]:
#         count+=1
#     d= count,num[i]
#     n.append(d)
# print(max(n))
 
# question - 15  
    
# 


# question - 25      

# num= [4,3,4,3,3,4,5,4,3,4,3,8]
# k=3
# n=[]
# fre=[]
# count_3,count_4,count_5,count_6=0,0,0,0
# for i in range (len(num)):
#     if num[i] not in n:
#         n.append(num[i])        #[4,3,6,5,]
    
#     if num[i]==3:                # counting a specifin number frequency
#         count_3+=1
#     elif  num[i]==4:
#         count_4+=1
#     elif num[i]==5:
#         count_5+=1
#     else:
#         count_6+=1
        
        
# if count_3>=k:
#     fre.append(3)
# if count_4>=k:
#     fre.append(4)
# if count_5>=k:
#     fre.append(5)
# if count_6>=k:
#     fre.append(6)
# print(fre)


# question -26:


# num=[1,1,1,64,65,64,78,98,98,98,98]        #
# fre=[]

# for i in range (len(num)-2):
    
#     if num[i]==num[i+1]==num[i+2]:
#         fre.append(num[i])

# print(fre)


#queation - 27

# input= ["m","?","u"]
# for i in range (len(input)):
#     for j in range (len(input)):
#         for k in range (len(input)):
    
#                 if input[i]==input[j]==input[k]:
#                     print(input[i],input[j],input[k])

#question =28


# num= [1,1,1,2,3,4,5,1,2]
# new=[]
# for i in range (len(num)):
#     if num[i]==1:
#         pass
#     else:
#         new.append(num[i])
# print(new)


#question = 29

# num= [1,4,5,[],6,45,[],89,[]]
# new=[]
# for i in range (len(num)):
#     if num[i]==[]:
#         pass
#     else:
#         new.append(num[i])
# print(new)
    
    
# question - 30

# num=[23,-34,-67,88,98,-65,-8]
# count_pos=0
# count_neg=0
# pos=[]
# neg=[]
# for i in range (len(num)):
#     if num[i]>0:
#         count_pos+=1
#         pos.append(num[i])
        
#     else:
#         count_neg+=1
#         neg.append(num[i])
# print(count_pos,pos)
# print(count_neg,neg)
        
        
# question - 33

         
# num=[33,45,65,76,89,98] 
# new=[]

# for i in range (len(num)):
#     s=0 
#     j=num[i]
#     while j>0:
#         re=j%10
#         s+=re
#         j//=10
#     new.append(s)
# print(new)

# additional 


##  bubble short   - Ascending order 
# num=[6,4,5,3,2,8]
# num2=[]
# max=0
# for i in range (len(num)):
#     for j in range (len(num)):
#         if num[i]<num[j]:
#             num[i],num[j]=num[j],num[i]
            
# print(num)
              #    Descending order

# num=[6,4,5,3,2,8]
# num2=[]
# num3=[]
# max=0
# for i in range (len(num)):
#     for j in range (len(num)):
#         if num[i]>num[j]:
#             num[i],num[j]=num[j],num[i]
#             num2.append(num[j])
#             num3.append(num[i])
# print(num)
# print(num2, num3)

#     for j in range (i):
#         if num[j]>num[j+1]:
#             num2.append(num[j])
# print(num2)

##  question - 34

# list= [34.34,12,-12,"python",0, "c#"] 
# new=[]
# for i in range (len(list)):
#     if type(list[i])== int:
#         new.append(list[i])
# print(new)

# for i in range (len(list)):
#     if type(list[i])==str:
#         list.remove(list[i])
        
#         #new.append(list[i])
# print(list)


#  question - 35
# num=[1234,132,634,167]
# a=[]

# for i in num:
#     a.append(str(i))
# print(a)   
# for j in range (len(a)):
#     if a[j][0]=="1":
#         g=True
#     else:
#         g=False
#         break
# print(g)


# for i in num:
#     if str(i).startswith("1"):
#         s=True
#     else:
#         s=False
#         break
# print(s)

# question - 36

# num=["1","2","3","4","5","6","7","8"]
# add=[]
# for i in range (0,len(num)-1,2):

#         sum = num[i]+num[i+1]
#         add.append(sum)
# print(add)

# i=0
# while i<len(num)-1:
#     sum =num[i]+num[i+1]
#     add.append(sum)
#     i+=2
# print(add)
    
        
        
#question -37

# num= ["1","2","3","4","5","6"]
# a=[]
# for i in range (len(num)-1):
#     s=[num[i],num[i+1]]
#     a.append(s)
# print(a)

# i=0
# while i<len(num)-1:
#     s=[num[i],num[i+1]]
#     a.append(s)
#     i+=1
# print(a)

#  qusestion - 38
#list=[]
#link="https:/www.w3school.org/python-excercise/.comlist/"

# i=0
# while i <len(domain):
#     j=0
#     while j<(len(list)):
#         if domain[i] in list[j]:
#             print(True)
#         else:
#             print(False)
#         j+=1
#     i+=1


#question -39      

# list=[[0,1,2],   #1
#       [3,4,5,6],  #2      
#       [7,8,9,10,11],#3
#       [12,13,14]]   #4

# question -

# num=[[2,4,5],[5,6,7],[3,4,2],[5,3,2]]       
# s=[]
# for i in range (len(num)):
#     sum=0
#     for j in range (len(num[i])):
#         sum=sum+num[j][i]
#     s.append(sum)
# print(s)
        
            






# question - 41

# list=[[1,2,43],[2,3,4,5]]
# d=[]
# count_i=0
# for i in list:
#     count_i+=1
#     count_j=0
#     for j in i:
#        count_j+=1
# print((count_i, count_j))
#d.append(mat_i_j)
#print(d)

# count_i=0
# i=0
# while i<len(list):
#     count_i+=1
#     count_j=0
#     j=0
#     while j<len(list[i]):
#         count_j+=1
#         j+=1
#     i+=1
# print((count_i,count_j))

#question -43

#list=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
# for i in range (len(list)):
#     list.insert(0+i,20)
#     i+=4
# print(list)
# i=4
# while i<len(list):
#     list.insert(i,20)
#     i+=4
# print(list)

# for i in range (4,len(list),4):
#     list.insert(i,20)
# print(list) 

#question - 44

# num=[3,8,9,4,5,6,54,3,3,24,78,65]
# n=[]
# sum=0.51

# for i in num:
#     add=sum+i
#     n.append(add)

# print(n)

# i=0
# while i in range (len(num)):
#     add=sum+num[i]
#     n.append(add)
#     i+=1
# print(n)

#question - 45

# num=[3,8,9,4,5,6,54,3,3,24,78,65,34,6,1,67,54,78,89,43]
# new_list=[]
# n=int(input("enter any number within the len(num) :"))
# for i in range (len(num)-n):
#     new_list.append(num[i])
# print(new_list)

# i=0
# while i<len(num)-n:
#     new_list.append(num[i])
#     i+=1
# print(new_list)

    
# question - 46

# list=["0","1","2","3"]
# list2=["apple","banana","mango","lichi"]
# list3=['100',"200","300","400"]
# new=[]

# for i  in range(len(list)):
#     sum= list[i]+list2[i]+list3[i]
#     new.append(sum)
# print(new)
    
# i=0
# while i<len(list):
#     sum=list[i]+list2[i]+list3[i]
#     new.append(sum)
#     i+=1
# print(new)


#question -47

# name=["Red","Maroon","purple","peach"]
# new=[]
# for i in range (len(name)):
#     n=[]
#     for j in range (len(name[i])):
#         n.append(name[i][j])
#     new.append(n)
# print(new)
    
    # for j in range(len(name[i])):
    #     s=list(name[i][j])
    #     print(s)

# i=0
# while i<len(name):
#     s=[]
#     j=0
#     while j<len(name[i]):
#         s.append(name[i][j])
#         j+=1
#     i+=1
#     new.append(s)
# print(new)

# Question - 48

# num=[12,45,23,67,78,90,32,100,76,38,62,73,29,45]
# new=[]

# for i in range (0,len(num)-2,3):
    
#     s=[num[i],num[i+1],num[i+2]]
#     new.append(s)

# print(new)

# i=0
# while i<len(num)-2:
#     list=[num[i],num[i+1],num[i+2]]
#     new.append(list)
#     i+=3
# print(new)


# question -50

#l=[[10,20],[30,40],[12,45,67,45],[12]]
#l2=[[1],[34,56,67],[12,34,],[89,78],[67]]
#n=[]
# for i in range(len(l)):
#     merge=l[i]+l2[i]
#     n.append(merge)
# print(n)

# i=0
# while i<len(l):
#     merge =l[i]+l2[i]
#     n.append(merge)
#     i+=1
# print(n)

# a=["s","d","f","k","d","f","s","f","k","o","p","i","w","e","k","c"]
# n=input("enter a alphabet with the list: ")

# for i in range(len(a)-1,0,-1):#15,0-1
#     if a[i]==n:
#         break
# print(i)
        
        
# i=len(a)-1
# while i>0:
#     if a[i]==n:
#         break
#     i-=1
# print(i)


# count=0
# i=0
# while i<len(a):
#     if a[i]==n:           #not correct code
#         count+=1
#     else:
#         break
#     i+=1
# print(count)
    
  

###_______________________________________________________________________________________

# num=[12,45,23,67,78,90,32,100,76,38,62,73,29,45]
# max=0
# min=0
# for i in num:
#     if max<i:
#         max=i
#     if min<i:
#         min=i
# print(min ,max)



 
    






        







 
    
        
        
    


    
    
    



                
                
        

        
    










# num=[1,1,2,3,4,4,4,5,6]
# count=0

# for i in range (len(num)):
#     for j in range (len(num)):
#         if  num[i]==num[j]:
        
            







        
    
    






