# words ="12,13"              #1    split()
# words =words.split()
# print(words)
 
# fruits = ["grape", "apple", "mango"]            #2 ENUMERATE()
# for i ,j in enumerate(fruits,start=2):

#     print(i,j)

                            
# list=[12,13,12,12]                  # replace
# list2=[]
# for i in range(len(list)):
#     list[i]=str(list[i]).replace(str(12),str(11))
#     list2.append(int(list[i]))
# print(list2)


# l=["python","tutorial","on","Mue"]
# l=("_").join(l)
# l=l.split(" ")
# print(l)

# neg=3-7               #abs 
# print(abs(neg))



# list="pppython#probl emspainfullpupp  "       #strip
# list=list.strip("p ")
# print(list)



# list=[1,23,4,5,6]
# print(list[0:3])


# import  statistics
# a=[1,-2,4,-8,16]
# print("The original list : " + str(a))
# test_list.sort()
# mid = len(test_list) // 2
# res = (test_list[mid] + test_list[~mid]) / 2
# print("Median of list is : " + str(res))
# # test_list.sort()
# mid = len(test_list) // 2
# res = (test_list[mid] + test_list[~mid]) / 2
# print("Median of list is : " + str(res))
# # res = statistics.median(a)
# # print("Median of list is : " + str(res))

# test_list = [1,-2,-4,8,-16]
# # test_list.sort()
# mid = len(test_list) // 2
# res = (test_list[mid] + test_list[~mid]) / 2
# print("Median of list is : " + str(res)

     
# l=[1,2,3,4,3,2,1,3,3]
# d=[]
# for i in range (len(l)//2):
#     count=1
#     for j in range (len(l)-1,-1,-1):
#         if i==j :
#             pass
#         elif l[i]==l[j]:
#             count+=1
#     if count>=2:
#         d.append(l[i])
# print(d)           


# cook your dish here
t=int(input())
for i in range (t):
    x=int(input())
    c=0
    if x<10:
        print(-1)
    else:
        if x>=10:
            c=c+x//10
            x=x-10*c
        if x==5:
            c=c+x//5
        print(c)
            

















































