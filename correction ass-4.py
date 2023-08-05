###########  QUESTION - 1   ###########

# list=[2,3,4,5,6,6,7,7,87,6,454,433] 
# n=len(list)
# list2=[0] *n
# a=0
# for i in range (n-1,0,-1):
#     list2[a]=list[i]
#     a+=1
# print(list2)    


########### QUESTION - 2   ##############


# sum=0
# n= int(input (" enter the total number: "))
# i=1
# list=[0]*n
# for i in range (len(list)):                  #  CREATE LIST
#     x=int(input (" enter the total number: "))
#     list[i]=x
#     i+=1
# print(list)



# for i in range (len(list)):                   # sorting
#     for j in range (len(list)-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)

# n=len(list)
# sum=0
  
# for j in range (n):        #mean 10.5  15
#     sum +=list[j]
#     mean=sum/n
# print(mean)

# if n % 2 == 0:                   # median  10.5   14
#  median1 = list[n//2]
#  median2 = list[n//2-1]
#  median = (median1 + median2)/2
# else:
#  median = list[n//2]
# print(median)


# mode= (3 * median) -(2 * mean)     # mode    10.11   13
# print(mean, median , mode)


from binascii import b2a_base64


def sun(a,b):
    return a+b

# def mul(p,q,r,s):
#     return sum(p,q)+r+s
    
# print(mul(2,3,4,5))
# print(

def mul(r):
    return sun(int(input()),int(input()))*r

print(mul(7))





















