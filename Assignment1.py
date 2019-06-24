#!/usr/bin/env python
# coding: utf-8

# In[55]:


a=4
b=6
a=a+b
b=a-b
a=a-b


# In[56]:


a,b


# In[4]:


print("enter the no to find the volume of sphere:")
r=int(input())
pi=3.14
vol=4/3*pi*r*r*r
print("volume:",vol)


# In[18]:


a=0
b=0
x=[]
y=[]
for i in range(1,100):
    if i%2==0:
        x.append(i)
    else:
        y.append(i)
    i+=1   
print("EVEN",x)
print("ODD",y)


# In[7]:


print("enter coefficient of quadratic equation:")
a=int(input())
b=int(input())
c=int(input())
print("equation:" , a,b,c)
d=b*b-4*a*c
import math

if d>=0:
    root1=(-b+math.sqrt(d))/2*a
    root2=(-b-math.sqrt(d))/2*a
    print("roots are equal and real",root1,root2)
else:
    print("roots are imaginary")
    


# In[8]:


print("enter the number:")
a=int(input())
count=0
while a>0:
    a= a//10
    count=count+1
print("number of digits:",count)


# In[3]:


print("enter the number:")
a=int(input())
if a>1:
    for i in range(1,a):
        if a%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("not prime")


# In[10]:


print("enter the number:")
a=int(input())
sum=0
for i in range(1,a):
    if i%5==0 or i%3==0:
        sum=sum+i
        print("numbers considered in the sum:",i)
print("sum:",sum)


# In[51]:


a=int(input("enter the number:"))
sum=0
for i in range(1,a):
    if i%3==0 or i%5==0 and a<1000:
        sum=sum+i
        print(i,"is a multiple , sum: ", sum)
    else:
        print(i,"is not a multiple of 3 or 5")


# In[70]:


def add(a):
    sum=0
    for i in range(1,a):
        sum=sum+i
    print("sum ",sum)
def product(a):
        product=1
        for i in range(1,a):
                product=product*i
        print("product ",product)        
  


# In[71]:


print("enter a number: ")
a=int(input("a="))
print("choose one of the following actions:")
print("1.add\n2.multiply")
c=int(input())
if c==1:
    add(a)
else:
    product(b)


# In[32]:


a=int(input("enter the no in range 2000 to 3500:"))
if a>3500:
    print("out of range!!")
else:
    if a%7==0:
        if a%5==0:
            print("divisible by 7 and also 5!! so not valid")
        else:
            print("divisible only by 7!! so valid")
        
    else:
        print("not divisible by 7")
            
        


# In[2]:


print("enter the string:")
str1="stop"
while True:
    n=str(input())
    if n==str1:
        print("you entered stop!!")
        break 
        


# In[76]:


print("enter the number:")
n=int(input())
if n>1:
    if n==2 or n==3:
        print(n,"is prime")
    for i in range(2,n):
        if i==2 or i==3:
            print(i,"is prime")
        if   n%i==0 or i%2==0 or i%3==0:
            continue
        else:
            print(i,"is prime")
            
            


# In[17]:



def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


# In[20]:


print("enter the number to find the factorial:")
n=int(input())
fact(n)


# In[46]:


print("enter the number to find fabonicci series")
n=int(input())
p=0
n=1
for i in range(n):
    print(n)
    p,n=n,n+p


# In[1]:


print("enter the number:")
a=int(input("a="))
p=0
n=1
for i in range(a):
    print(n)
    p,n=n,p+n
    


# In[10]:



def gcd(a,b):
    if a==0:
        return b
    else:
        if a>b:
            return b
        else:
            return a
def lcm(a,b):
    return (a*b)/gcd(a,b)


# In[11]:


print("enter two numbers to find LCM:")
a=int(input("a="))
b=int(input("b="))
lcm(a,b)


# In[35]:


def factors(n):
    for i in range(1,n):
        if n%i==0:
            print(i) 
            


# In[38]:


factors(10)


# In[57]:


n=5
for i in range(n):
    print("*"*(i+1)," "*(n+1))


# In[66]:


n=7
for i in range(n):
    print("*"*(n-i)," "*(i))


# In[47]:


n=5
for i in range(n):
    for j in range(i):
        print(i,end=" ")
        j+=1
    print("")


# In[22]:


c=1
n=5
for i in range(n):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    print("")


# In[81]:


n=65
for i in range(5):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n+=1
    print("")


# In[87]:


n=5
for i in range(n):
    print("  "*(n-i-1),"* "*(2*i+1))


# In[3]:


print("enter rhe number:")
a=int(input("a="))
for i in range(4):
    print("a"*(i+1),end="+")
a=a+a*a+a*a*a+a*a*a*a
print(" =",a)    
   


# In[ ]:





# In[ ]:





# In[ ]:




