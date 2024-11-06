
# 01) write a function to calculate and return the square of number

# def square(x:int)->int:

#     return x**2

# result1= square(4)
# print(result1)

# ........................................................................................................

#02) create a function that takes two numbers as a parameter and return their sum

# def sum(num1:int,num2:int)->int:
#     return num1 + num2

# result2=sum(2,2)
# print(result2)

# ........................................................................................................

#03) write a function multiply,that multiply two numbers,but can also accept and multiply strings.

# def multiply(val1,val2):
#     return val1*val2

# result3=multiply("hello ", 3)
# print(result3)
# print(type(result3))

# ........................................................................................................

#04) create a function a function that return both the area and circumference of a circle given its radius

# import math
# def circle(radius)->float:
#     circumference=2*math.pi*radius
#     Area=math.pi*radius**2
#     return circumference,Area

# c,a=circle(5)
# print(f"Circumference:{c:.2f} , Area:{a:.2f}")

# ........................................................................................................

# 05) Write a function that greets a user.if no name is provided,it should greet with a default name.

# def greet(name:str="user")->str:
#     return f"Hello, {name}"

# result5=greet("Shiraz")
# print(result5)
# result6=greet()
# print(result6)

# ........................................................................................................

# 06) Create a lambda function to compute the cube of a number.

# cube_num=lambda x:x**3
# print(cube_num(3))

# ........................................................................................................

# 07) write a function that takes variable number of arguments and returns their sum.

# def sum_args(*args:int)->int:
#     return sum(args)

# result7=sum_args(1,2,3)
# print(result7)
# result8=sum_args(1,2,3,4,5,6)
# print(result8)
# result9=sum_args(1,2,3,4,5,6,7,8 )
# print(result9)

#........................................................................................................

# 08) create a function that accept any number 

# def kwargs(**kwargs):
#     for key,value in kwargs.items():
#          user_data= f"{key} : {value}"
#          print(user_data)

# print(kwargs(name="shiraz",age=21,profession="Student"))

# def kwargs(**kwargs):
#     result = ""
#     for key, value in kwargs.items():
#         result += f"{key} : {value}\n"
#     return result

# # Print the returned result
# print(kwargs(name="shiraz", age=21, profession="Student"))

#........................................................................................................

# 09) write a generator function that yields even numbers up to a specific limit.

# def generator_function(n:int):
#     for i in range(2,n+1,2):
#         yield i


# for i in generator_function(10):
#     print(i)

#........................................................................................................

# 10) create a recursive function to calculate the factorial of a number.

# def factorial(n:int)->int:
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(4))
