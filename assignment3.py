#################  QUESTION - 1    ################
# n= int(input())
# list=[0]*n
# a=0
# for i in range (n):
#     name=input(" name: ")
#     list[a]=name
#     a+=1
# print(list)


################     QUESTION -2     ##############
# n= int(input())
# planet=[0]*n
# a=0
# for i in range (n):
#     name=input(" name: ")
#     planet[a]=name
#     a+=1


#planet=["mercury","venus","earth","mars","jupitar","saturn"]
#n=int(input())
#print(planet[n-1])


# planet=list(map(str,input().split()))
# print(planet)
# user= int(input("enter a number between 0-7: "))
# print(planet[user-1])


###################   QUESTION -3   ######################
#list=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# n= len(list)
# for i in range (n):
#     if i%2!=0:
#         print(list[i])

#print(list[1::2])


###################   QUESTION - 4  ######################



# i=0
# elements=0
# a=0
# n=int(input("total number in an array:" ))
# list=[0]*n
# while True:
#     if elements ==n:
#         break
#     else:
#         if i%2==0:
#             list[a]=i
#             a+=1
#             elements+=1
#     i+=1
# print(list)


#list=[i for i in range(21) if i%2==0]
#print(list)

###################   QUESTION - 5  ######################

# n=int(input())
# list=[0]*n
# a=0
# for i in range (n):
#     user=int(input("number: "))
#     list[a]=user
#     a+=1
# print(list)

# l=list(map(int,input().split()))
# print(l)

###################   QUESTION - 6  ######################

#array=list(map(int,input().split()))
# list=[2,3,54,6,78,65,43,5]
# user=int(input())

# if user in list:
#     print("yes")
# else:
#     print("no")


##################  QUESTION -7   ####################

# n= int(input())
# list=[0]*n 
# a=0
# min=0
# for i in range (n):
#     x=int(input("element: " ))
#     list [a]=x  
#     if min>list[a]:
#         min=list[a]
#     a+=1
# print(list)
# print(min)

###################   QUESTION -8   ######################


# list= [1,1,1,2,3,4,65,65,65,5,1,2]
# user=int(input())
# count=0
# for i in range (len(list)):
#     if user==list[i]:
#         count+=1
    
# print(count)


###################   QUESTION -9  ######################



# list=['T', 'H', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'T',
# 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'T', 'H', 'H', 'T', 'H', 'H',
# 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T',
# 'T', 'T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'T', 'H', 'H', 'T', 'H', 'H', 'H', 'T',
# 'H', 'T', 'H']
# count_T=0
# count_H=0
# c=0
# i=0
# while i<len(list):
#     if list[i]=="H":
#       count_H+=1
#     elif list[i]=="T":
#         if count_T>=3:
#             c+=1
#             count_H=0
#     if list[i]=="T":
#         count_T+=1
#     elif list[i]=="H":
#         if count_H>=3:
#             c+=1
#             count_T=0
#     i+=1
# print(c,count_T,count_H)
    










# if list[i]==list[i+1]==list[i+2]=="T":
#         count_T+=1
#         i+=3
#     elif list[i]==list[i+1]==list[i+2]=="H":
#         count_H+=1
#         i+=3
#     else:
#         i+=1
# print(count_T,count_H,count_T+count_H)


###################   QUESTION -10   ######################


#n=int(input())
#list=[[1]*n]*n

# n=int(input())
# i=1
# list1=[]
# c=1
# while i<=4 :
#     l=[0]*n
#     a=0
#     for j in range (n):
#         l[a]=c
#         a+=1
#     i+=1
#     list1.append(l)
# print(list1)

###################   QUESTION -11   ######################


# n=int(input())
# i=1
# list1=[]
# while i<=16 :
#     l=[0]*n
#     a=0
#     for j in range (n):
#         l[a]=i
#         a+=1
#         i+=1
#     list1.append(l)
# print(list1)


###################   QUESTION -12  ######################


# n=int(input())
# i=1
# list1=[]

# while i<=4 :
#     l=[0]*n
#     a=0
#     for j in range (n):
#         c=int(input())
#         l[a]=c
#         a+=1
#     i+=1
#     list1.append(l)
# print(list1)

###################   QUESTION -13   ######################


# list=[[1,2,3,4],
#       [5,6,7,8],
#       [9,0,1,2],
#       [2,3,6,9]]
# row=[]
# column=[]
# for i in range (len(list)):
#     if i==2-1:
#         row.append(list[i])
#     for j in range (len(list)):
#         if j==3-1:
#             column.append(list[i][j])

            
# for i in range (len(list)):
#     print(list[1][i])
#for i in range (len(list)):
#     print(list[i][2])
    



# print(row,column) 
         

###################   QUESTION - 14  ######################


# list=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# r=int(input())
# c=int(input())
# row=[]
# column=[]
# for i in range (len(list)):
#     if i==r-1:
#         row.append(list[i])
#     for j in range (len(list)):
#         if j==c-1:
#             column.append(list[i][j])
            
    
# print("value of elements  specific row and column which given by user:", row, column )          



###################   QUESTION -19  ######################




# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.','.', '.', '.']]

# for i in range (6):
#     for j in range(9):
#         print(grid[j][i],end=" ")
#     print()    

#####################  QUESTION -20     ###############



# a=[[1,2,3],
#    [5,6,7],
#    [9,10,11],
#    [13,14,15]]    
# n=len(a)
# top,bottom=0,n-1
# left,right=0,n-1
# dir=0
# while top<=bottom and right>=left:
#     if dir==0:
#         for i in range (left,right+1):
#             print(a[top][i])
#         top+=1
#     elif dir ==1:
#         for i in range(top ,bottom+1):
#             print(a[i][right])
#         right-=1
#     elif dir==2:
#         for i in range(right,left-1,-1):
#             print(a[bottom][i])  
#         bottom-=1
#     elif  dir==3:
#         for i in range (bottom ,top-1,-1):
#             print(a[i][left])  
#         left+=1   
#     dir=(dir+1)%4


################### #######      ASSIENGMENT  -  4 (NESTED LIST)   #############################################




# a= [[2,4,1],
#     [18,10,-1],
#     [1,-4,50]]
# b= [[8, 0, 3,1],
#     [2,-5,7,1],
#     [3, -1,5,2]]

#####################   QUESTION = 14   ##################

# b= [[2,3,6],
#     [3,4,5],
#     [6,5,9]]
#list=[]
# for i in range (len(b)):
#       l=[]
#       for j in range (len(b[i])):
#             l.append(b[j][i])
#       list.append(l)
# print(list)
# if list==b:
#       print("it is a symmetric matrix")
# else:
#       print("not a symmetric matrix")



############## QUESTION =  13  ##################


b= [[0,2,4],
    [-2,0,3],
    [-4,-3,0]]
list=[]
for i in range (len(b)):
      l=[]
      for j in range (len(b[i])):
            d=-1*b[j][i]
            l.append(d)
      list.append(l)
print(list)

if list==b:
      print("it is a skewed matrix")
else:
      print("not a skewed matrix")
          
  













################ QUESTION -12    ##############

# user =int(input(" enter any no: "))
# for i in range (len(b)):
#     for j in range(len(b)):
#         if user==b[i][j]:
#             print("indexing of user no {0} is :-".format(user),i,j,b[i][j])
        

################  QUESTION -11  ###############

# for i in range (len(a)):
#     for  j in range (len(a)):
#         if max<a[i][j]:
#             max=a[i][j]
# print("the maximum(largest) element in list (a) is : ", max)   
        

############   QUESTION -10  #################

# min =a[0][0]
# for i in range (len(a)):
#     for  j in range (len(a)):
#         if min>a[i][j]:
#             min=a[i][j]
# print("the maximum(smallest) element in list (a) is : ", min)  


############   QUESTION -  9  #################

     
# sum=0
# for i in range (len(a)):
#     for j in range(len(a)):
#         sum+=a[i][j]
#         i+=1
#     break
# print(sum)


      ####  left to right from down to up diagonal  ##### 

# sum=0
# for i in range (len(a)-1,-1,-1):
#     for j in range (len(a)):
#         sum+=a[i][j]
#         i-=1
#     break
# print(sum)


################   QUESTION - 8    #################

# b=[[1,0,0],
#    [0,1,0],
#    [0,0,1]]
# diagonal=0
# for i in range (len(b)):
#       for j in range (len(b[i])):
#            if b[j][i]==b[i+1][j+1]:
#                  print("yes")
#            else:
#                  print("no")
      
#            i+=1
           
# for i in range (len(b)):
#       r_s=0
#       c_s=0
#       for j in range (len(b[i])):


################   QUESTION -  7  #################

# b= [[1,0,0],
#     [0,1,0],
#     [0,0,1]]
# count=0
# for i in range (len(b)):
#       for j in range (len(b)):
#             if i==j:
#                 if  b[i][j]!=1:
#                     count+=1
#                     break
#             else:
#                 if b[i][j]!=0:
#                    count+=1
#                    break
#       if count>0:
#           break
# if count>0:
#     print("not identitcal")
# else:
#     print("identitical")


#####################    question = 8    ##############


# b=[[1,0,0],
#    [0,1,0],
#    [0,0,1]]

# count=0
# for i in range (len(b)):
#     for j in range (len(b[i])):
#         if i!=j :
#             if b[i][j]!=0:
#                 count+=1
#                 break
#     if count>0:
#         break 
# if count>0:
#     print("not diagonal")
# else:
#     print("diagonal")



#####################   QUESTION = 6    ###################


# a= [[2,4,1],
#     [18,10,-1],
#     [1,-4,50]]
# list=[]
# for i in range (len(a)):
#       l=[]
#       last=[]
#       for j in range (len(a[i])-1,-1,-1):
            
#             if j==-1:
#                   last.append(a[i][j])
#             else:
#                   l.append(a[i][j])
#       last=last+l
#       list.append(last)
# print(list)
      
            
##################  QUESTION =   5      ###################

# n=10
# phone=" "
# for i in range (n):
#       user=int(input())
      
#       if i==3 or i==6:
#             phone+="-"+user
#       else:
#             phone+=user
# print(phone)     
                
                
                #or
                
# phone="1234567878"
# new=""
# for i in  range (len(phone)):
#       if i==3 or i==6:
#             new+="-"+phone[i]
           
#       else:
#             new+=phone[i]
# print(new)
          

#####################   QUESTION =  4    #######################     
      
# a= [[2,4,1],
#     [18,10,-1],
#     [1,-4,50]]

# list=[]
# for i in range (len(a)):
#       l=[]
#       for j in range (len(b)):
#             l.append(a[j][i])
#       list.append(l)
# print(list)
            
            
############   QUESTION = 1, 2, 3  ###############

# ADD=[]
# SUB=[]
# MUL=[]
# for i in range (len(a)):
#     sum=0
#     s=0
#     m=1
#     add=[]
#     sub=[]
#     mul=[]
#     for j in range (len(a)):
#         sum=a[i][j]+b[i][j]
#         s =a[i][j]-b[i][j]
#         m=a[i][j]*b[i][j]
#         add.append(sum)
#         sub.append(s)
#         mul.append(m)
#     ADD.append(add)
#     SUB.append(sub)
#     MUL.append(mul)
# print( "sum of list(a) &list(b) : ", ADD)
# print("difference of list(a) &list(b) : ", SUB)
# print("multiplation of list(a) &list(b) : ", MUL)
















# b=[[1,0,0],
#    [0,1,0],
#    [0,0,1]]
# diagonal=0
# for i in range (len(b)):
#       for j in range (len(b[i])):
#            if b[j][i]==b[i+1][j+1]:
#                  print("yes")
#            else:
#                  print("no")
      
#            i+=1
           
# for i in range (len(b)):
#       r_s=0
#       c_s=0
#       for j in range (len(b[i])):








































































































































































# b= [[1,1,0],
#     [0,1,0],
#     [0,0,1]]
# count_i=0
# for i in range (len(b)):
#     count_i+=1
#     count_j=0
#     for j in range (len(b[i])):
#         count_j+=1
# if count_i==count_j:
#       print("it is a square matrix") 
#       d_s=0
#       for k in range (len(b)):
#             for l in range (len(b[k])):
        
#                   d_s+=b[k][l]
#                   k+=1
#             if d_s==3:
#                   for n in range (len(b)):
#                         r_s=0
#                         c_s=0
#                         for m in range(len(b[n])):
#                             r_s+=b[n][m]
#                             c_s+=b[m][n]
                            
#                         if r_s==1 and c_s==1:
#                             continue
#                         else:
                            
                            
                        
                        
                    
#             else:
#                   print("its dianols sum is greater than or less than 3")
#                   break
    
                
#             if n==2 and m==2:
#                     print("it is an ideantiy matrix")
#                     break
# else: 
#       print("it is not a square matrix,so  that it's not also a identity matrix ")
