# list= ["apple","banana","lichi","peach","kiwi"]
# new=[i for i in list if i !="apple"]
# print(new)


# for i in range (len(list)):
#     if list[i]!="apple":
#         new.append(list[i])
# print(new)

# for i in list:
#     if "apple"  not in i:
#         new.append(i)
# print(new)


# # 
# num=[]
# for i in range(10):
#     num.append(i)
# print(num)



# new=[i.upper() for i in range(10)if i<=5]
# print(new)


# list=["papaya","peach"]
# list.append(list[0])
# print(list)
 

# num=[12,23,4,5,32,34,56,776,544] 
# #new=[]
# i=0
# while i<(len(num)):
#     j=0
#     while j<len(num):
#         if num[i]<num[j]:
#             num[i],num[j]=num[j],num[i]
#             print(num)
#         j+=1
#     i+=1
# from ast import List
# from codecs import latin_1_encode
# import copy
# from email.charset import QP
# from msilib.schema import ListBox
# from tkinter.messagebox import QUESTION       
# li1 = [1, 2, [3,5], 4]
  
# using deepcopy to deep copy 
#li2 = copy.deepcopy(li1)
#li3=[] 
# original elements of list
#print ("The original elements before deep copying")
#for i in range(0,len(li1)):
 #   li1.append(20)
    #print (li1[i] ,end=" ")
#print(li3)
#print(li1)
#print(li2)
# print("\r")   
      
    

     
     
     
     
     
     
    

# i=0
# while i<10:
#     if i<=5:
#         new.append(i)
#     i+=1
# print(new)

# for i in range(10):
#     if i <=5:
#         new.append(i)
# print(new)




# i=0
# while i<(len(list)):
#     if list[i]!="apple":
#         new.append(list[i])
#     i+=1
# print(new)
# list=range (100,110)
# print(list.index(109))

# list=[12,13]
# list2=[12,13]
# print((list[0]+list2[0],list[1]+list2[1])*2)

# list=[1,2,3,4,(1,23,43),34,None,[1,2]]
# print(len(list))

#print(list(range(4,20,2)))

# for i in range (4,30):
#     if i%2==0:
#         print(i,end=" ")

# index=int(input("enter the num: "))
# n=0
# for x in range(0,index+1):
#     n+=x
#     print(n,end=" ") 



# list=[]
# n=int(input("enter the number: "))
# i=1
# while i<n:
#     num=int(input("enter the which u want to insert num: "))
#     i+=1
#     list.append(num)
# print(list,"<---given/n")
# list.sort()
# print(list)
# print(max(list))

# list=[]
# def l(a,b):
#     for i in range (a,b):
#         if i%2==0:
#             print(i)
    

# alist=[12,34,2,3,65,4]
# alist.sort(reverse=True)
# print(alist)
# print(alist.pop(2))




# l=[1,2,3,4,5,6,7,8]

# for i in range (len(l)):
#     a= int(input("enter the number : "))
#     if a==2:
#          l[-1],l[-2]=l[-2],l[-1]
#          print(l)   
#     elif a==3:
#          l[-1],l[-3],l[-2]=l[-2],l[-1],l[-3]
#          print(l)
#     elif a==4:
#          l[-1],l[-2],l[-4],l[-3]=l[-2],l[-4],l[-2],l[-1] 
#          print(l)
#     else:
#          l[-1],l[-2],l[-4],l[-3]=l[-2],l[-4],l[-2],l[-1]
#          l[1],l[2],l[3]=l[3],l[1],l[2]
#          print(l)
        
# n="Q"
# m="P"
# a=int(input("enter a number: "))
# print((n+str(a)+m+str(a)+" ")*a)  
 ##------------------------------------------------------------------------------------       
        
#doc QUESTION


# list1=[[10,20],[30,40],[50,60,70,90]]      #50
# list2=[[61],[34,54,67],[23,13,45,34]]
# new=[]
# for i in range (len(list1)):
#     d=(list1[i])+(list2[i])
#     new.append(d)
# print(new)

# list=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

# alpha=input("enter a alphabet among the list: ")
# for i in range (len(list)-1,0,-1):
    
#     if list[i]==alpha:
#         break
# print("last occerence of {0}".format(alpha),i)  

    
# list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]   
# new=[]
# i=0
# while i<len(list)-4:
#     s=[list[i],list[i+1],list[i+2],list[i+3]]
#     new.append(s)
#     i+=4
# print(new)
    
# list=['Red', 'Maroon', 'Yellow', 'Olive']
# new=[]
# for i in list:
#     list2=[]
#     for j in i:
#         list2.append(j)
#     new.append(list2)
# print(new)

    
# list1=['0', '1', '2', '3', '4']
# list2=['red', 'green', 'black', 'blue', 'white']
# list3=['100', '200', '300', '400', '500']
# new=[]
# for i in range (len(list1)):
#     sum=list1[i]+list2[i]+list3[i]   
#     new.append(sum) 
# print(new)
        
 
# list=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# new=[]
# n=int(input("enter the number:"))
# for i in range (len(list)-n):
#     new.append(list[i])
# print(new)

    
# list=[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]

# new=[]
# for i in range (len(list)):
#     sum= 0.51+list[i]
#     new.append(sum)
# print(new)


# list=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']

# for i in range (3,len(list),4):
#     list.insert(i,"z")
# print(list)

# list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# start_index=3
# for i in range (len(list)):   #8
#     element_index=start_index%len(list)     #3%8   4%8
#     print(list[element_index],end=" ")
#     start_index+=1

# list=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]

# for i in range (len(list)):
#     count=0
#     for j in range (len(list[i])):
#         count+=1
# print(count,i+1)

# list=[[0, 1, 2], [2, 4, 5, 5], [2, 3, 4],[3, 6, 9, 1]]
# add=[]
# for i in range (len(list)):
#     sum=0                                  not solved
#     for j in range (len(list[i])):
#         if list[i][j]==None:
#             list[i][j]==0
            
#         sum+=list[j][i]
#     add.append(sum)
# print(add)
    
# link="https://www.w3resource.com/nethttps://www./w3resource.tv/net"
# list2=['.com', '.edu', '.tv']
# l= []
# l.append(link)
# print(l)

# for i in l:
#     for j in list2:
#         if j in i:
#            print("True")
#         else:
#            print("false")


# list=[1, 2, 3, 4, 5]
# new=[]
# for i in range (len(list)-1):
#     s=list[i],list[i+1]
#     new.append(s)
# print(new)
    
# staute=[6,2,3,8]         #18
# staute.sort()
# print(staute)
# o=[4,5,7]
# a=3

# staute.insert(2,4)
# staute.insert(3,5)
# staute.insert(5,7)
# print(staute)

# Input=[1, 1, 1, 64, 23, 64, 22, 22, 22]
# new=[]
# count=0
# for i in range (len(Input)-2):
#     if Input[i]==Input[i+1]==Input[i+2]:
#         #s=Input[i]
#         print(Input[i],end=" ")
    #new.append(s)
#print(new)      

# Input=[1, 2, 3]
# for i in range(len(Input)):
#     for j in range (len(Input)):
#         for k in range (len(Input)):
#             if Input[i]!=Input[j]!=Input[k]:
#                 print(Input[i],Input[j],Input[k])
        
     
# input= [1, 1, 2, 3, 4, 5, 1, 2] 
# new=[]    
# r=1
# for i in range (len(input)):
#     if input[i]!=r:
#         new.append(input[i])
# print(new)



# input=[5, 6, [], 3, [], [], 9]
# new=[]
# b=[]
# for i in range (len(input)):
#     if input[i]!=b:
#         new.append(input[i])
# print(new)

        

# list1 = [2, -7, 5, -64, -14]
# new_pos=[]
# new_neg=[]
# neg=0
# pos=0
# for i in range(len(list1)):
#     if list1[i]>0:
#         pos+=1
#         new_pos.append(list1[i])
#     else:
#         neg+=1
#         new_neg.append(list1[i])
# print(neg,new_neg)
# print(pos,new_pos)


# list=[12, 67, 98, 34]    
# add=[]
# for i in range (len(list)):
#     add.append(str(list[i]))
# #print(add)
# sum=[]
# for j in range (len(add)):
#     s=0
#     for k in range(len(add[j])):
#         s+=int(add[j][k])
#     sum.append(s)
# print(sum)

# list=['Python', 'list', 'exercises', 'practice', 'solution']
# a=[]
# for i in list:
#     for j in range(3,len(i)):
#         a.append(list[j])
#         for k in range(0,3):
#             a.append(list[k])
# print(a)

    
    
# for i in range (len(list)):
#     list[i][3]=list[i][1]1
# print(list)
    
        
        




# n=int(input("enter any no: "))
# i=1
# while i<=n:
#     print("  "*(n-i),"* "*(2*i-1))

        
# Input = [12, 35, 9, 56, 24]
# Input[1],Input[-1]=Input[-1],Input[1] 
# print(Input)      

# a=int(input("no:"))       # 1
# b=int(input("no: "))       #2
# c=int(input("no: "))
        
       
    
# series=int(input("enter the no: "))
# i=1
# sum=0
# while i<= series:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1

#     if count<3:
#         print("prime", count, i)
#         sum+=i
#     # else:
#     #     print("prime", count, i)
#     i+=1
# print(sum)
    
    
# amt= int(input(" enter the total amount: "))
# t_notes=0
# if amt>=2000:
#    notes=amt//2000
#    amt= amt-(notes*2000) 
#    t_notes+=notes
# if amt>=500:
#     notes= amt//500
#     amt=amt-(notes*500)
#     t_notes+=notes
# if amt>=200:
#     notes=amt//200
#     amt=amt-(notes*200)
#     t_notes+=notes
# if amt>=100:
#     notes=amt//100
#     amt=amt-(notes*100)
#     t_notes+=notes
# if amt>=50:
#     notes=amt//50
#     amt=amt-(notes*50)
#     t_notes+=notes
# if amt>=20:
#     notes=amt//20
#     amt=amt-(notes*20)
#     t_notes+=notes
# if amt>=10:
#     notes= amt//10
#     amt= amt-(notes*10)
#     t_notes+=notes
# if amt>=5:
#     notes=amt//5
#     amt=amt-(notes*5)
#     t_notes+=notes
# if amt>=2:
#     notes=amt//2
#     amt=amt-(notes*2)
#     t_notes+=notes
# if amt>=1:
#     notes=amt//1
#     amt=amt-(notes*1)
#     t_notes+=notes
# print(t_notes)   

# a=int(input(" enter the num: "))   
# b=int(input(" enter the num: "))  
# c=int(input(" enter the num: ")) 
# d=int(input(" enter the num: "))     
    
# if a>b:
#     max= a
#     sec=b  
#     if c>max:
#         t_max=sec
#         sec=max
#         max=c
#     elif sec<c:
#         t_max=sec
#         sec=c
#     else:
#         t_max=c
#         print(t_max)
# else:
#     max=b
#     sec=a
#     if max<c:
#         t_max=sec
#         sec=max
#         max=c
#     elif sec<c:
#         t_max=sec
#         sec=c
#     else:
#         t_max=c
# if max<d:
#     t_max=sec
#     sec=max
#     max=d
# elif sec<d:
#     t_max=sec
#     sec=d
# elif t_max<d:
#     t_max=d
#     print(t_max)

# print(max,sec,t_max)
    

#________________________________________________________________________________

# a= [10, 50, 40]  
# b=[2,5,3]
# sum=0
# for i in range(len(a)):
#   avg=a[i]*b[i]/a[i]
#   sum+=avg
#   print(sum)a
# print(sum)



list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l=len(list1)
for i in range (0,l):
  for j in range (0,l-1):
    if list1[j][1]>list1[j+1][1]:
      list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
  


b=[2,3,4,]

if len(b)==0:
  print(True)
else:
  print(False)













