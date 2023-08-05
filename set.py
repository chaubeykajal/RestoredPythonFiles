#1. Write a Python program to create a set. 

# a=set(map(int,input().split( )))
# print(a)


#2. Write a Python program to iteration over sets.

# b={"abscond","barrage","canebis","dungeon","erie"}
# for i in b:
#     print(i,end=" ")

#3. Write a Python program to add member(s) in a set. 

# b={"abscond","barrage","canebis","dungeon","erie"}
# b.add("ferocious")

# b.update({"gaga","hover"})
# b.add("Budapeste")   # but add method add a whole word in given string  
# b.update("iceberge") # update methon  add method add a whole word  
# print(b) 


#5. Write a Python program to remove an item from a set if it is present in the set.

# b={"abscond","barrage","canebis","dungeon","erie"}
# b.pop()
# b.discard("abscond")
# b.discard("barrage")
# b.discard("canebis")
# b.discard("ferocious") # its doesn't give any error
# print(b)


#6. Write a Python program to create an intersection of sets.

# a={"a","b","c","d","e"}
# b={"x","c","q","d"}
# v=a.intersection(b)
# print(v)
# print(a&b)


# ADDITIONAL QUESTION
# t=("a","b","c",)
# print(((t*3)))  


#6. Write a Python program to create an union of sets.

a={"a","b","c","d","e"}
b={"x","c","q","d"}
u=a.union(b)
print(u)
print(a|b)

a={"a","b","c","d","e"}
b={"x","c","q","d"}
m=a.symmetric_difference(b)
print(m)


















