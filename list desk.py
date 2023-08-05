add=[]

# list =[
#     [78,76,94,86,88,],
#     [91,71,98,65],
    
    
#     [87,67,49,68,88]]
# 
# for i in list:
      #sum=0
    
#     for j in i :
#         sum =sum+list[i][j]
        
#         add.append(sum)
# print(add)
# print()


# a=[1,[34,54],[3,5,4],2,[6,7,8]]
# print(a[1][1])
# print(a[2][0])
# print(a[4][2])



# m_s=[[8,3,4],
#      [1,5,9],
#      [6,7,2]]
# for i in range (len(m_s)):
#     sum_c=0
#     sum_r=0
    
#     for j in range (len(m_s[i])):
#         sum_r+=m_s[i][j]
#         sum_c+=m_s[j][i]
        
    

# print(sum_c)
# print(sum_r)

# sum_d=0
# k=0
# p=0
# while k<len(m_s):
#     sum_d+=m_s[k][p]
#     p+=1
#     k+=1
    
# print(sum_d)

# if sum_r==sum_c==sum_d:
#     print("it is a magic square")
# else:
#     print("not a magic square")
    
    

# new=[]
# s=["rishabh ","kiara","minni","jiya"]
# m=[23,44,67,89,76] 
# for i in range (len(s)): 
#     d=s[i],m[i]
#     new.append(d)
# print(new)
      
      
# s_e=[]
# s_o=[]
# l=[23,14,56,12,19,9,15,25,31,42,43]
# sum_1=0
# sum_2=0
# for i in range (len(l)):
#     if l[i]%2==0:
#         sum_2+=l[i]
#     else:
#         sum_1+=l[i]
# print(sum_1,sum_2)

question =["how manycontinents are there?",
           "what is the capital of india?",
           "which couse are avilable in ng?"]
option=[["four","three", "seven","nine"],
        ["chandigarh","bhopal","mumbai","delhi",],
        ["software eng","counselling","tourism","agriculture"]]
ans=["seven","delhi","software"]
sol=[["nine","seven"],
     ["mumbai","delhi"],
     ["softwa eng","counselling"]]
key=["seven","delhi","software eng"]

for i in range(len(question)):
    print("AAPKA  SAWAL HAI ")
    print(question[i])
    print(i+1,".",end="")
    print(*option[i],sep="\n   ")
    
    lifeline=input("do you want 50-50 lifeline: ")
    for j in key:
        if lifeline=="yes":
            print(i+1,".",end="")
            print(*j,sep="\n")
            user=input("enter the answer: ")
            if user==j:
                print("you win")
            else:
                print("oops")
                break
            
    user_ans=input(" enter your ans according to the option :")
    if user_ans==ans[i]:
        print("you win")
    else:
        print("u lose, try again")
        break
    
    


    
    

        
    