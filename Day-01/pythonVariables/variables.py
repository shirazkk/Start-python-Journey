
#Variables are containers for storing data values.

# Variables in Python are created by directly assigning a value.

a="shiraz"
print(a) #it will print str value "shiraz"

b=2
print(b) #integar output print 2

#we also declare python variables with specefic type 

d:str="Hello"
print(d)

e:int=4
print(e)

r:bool=True
print(r) #output will be in boolean true /false


# Get the Type
#you can also check type of your variable using type keyword

print(type(r))
print(type(d))

# Case-Sensitive
# Variable names are case-sensitive.

p="hello-world1"
P="hello-world2"

print(p)
print(P)

#python variable names

# These are legal variable names

_a="hello"
box_model="margin"
myvar="var"
_myvariable_="variable"


# these are ilegal variable it through error

# 2myvar = "John"
# my-var = "John"
# my var = "John"
# def="hello"

#Python Variables - Assign Multiple Values

aa, bb, cc = "apple", "Banana", "peach" #Make sure the number of variables matches the number of values, or else you will get an error.
print(aa)
print(bb)
print(cc)

#you also assign one value to multiple variables.

one=two=three="values" #print "values" in all variables.
print(one)
print(two)
print(three)

#if you have collection of values like list object so you unpack them in variables

myList = ["apple" ,"mango","watermelon"]
q,t,c=myList
print(q)
print(t)
print(c)

