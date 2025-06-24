#Write a list comprehension to print only the word 'python' from the list.
                   #  S=[ ‘python’ ,’java’ , ‘c++’ , ‘developer’ ] s=['python', 'java', 'c++', 'developer']
# res=[x for x in s if x=='python']
# print(res)
# #output:- ['python']



#Flatten the nested list [[1, 2], [3, 4], [5, 6]] into a single list.
n=[[1,2],[3,4],[5,6]]
res=[x for i in n for x in i]
print(res)
#output:- [1,2,3,4,5,6]


#From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.
n=[[2,5], [7,9], [12,15]]
res=[x for i in n for x in i if x%2==0]
print(res)
#output:- [2,12]


#Create a list of squares for numbers from 1 to 20.
res=[i**2 for i in range(1,21)]
print(res)
#output:-[[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]]


#Print prime numbers between 10 to 20 using list comprehension?
res= [ i for i in range(10,21) if all(i%j!=0 for j in range(2,i))]
print(res)
#output:- [11,13,14,17]


#Convert a=10 int data type to 10 string data type  with out using str()?
a=10
s="0123456789"
res=""
while a>0:
    digit=a%10
    a//=10
    for x in range(len(s)):
        if digit==x:
            res=s[x]+res
print(type(res),res)
#output:-# <class 'str'> 10

#Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
a="Hello World"
res=""
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
        res+=chr(ord(i)-32)
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        res+=chr(ord(i)+32)
    else:
        res+=i
print(res)

# Output:-
# hELLO wORLD



