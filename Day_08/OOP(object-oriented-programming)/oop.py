
# # class Person:
# #   def __init__(self, name:str, age:int):
# #     self.name = name
# #     self.age = age

# #   def myfunc(self):
# #     print(f"Hello my name is  {self.name} and i am {self.age} old")

# # p1 = Person("John", 36)
# # p1.myfunc()

# # # p1.age=21 #modify the age attribute
# # # p1.myfunc()

# # # you can also delete and object properties using del keyword
# # del p1.age
# # print(p1.myfunc())


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         # Check if age attribute exists
#         if hasattr (self, 'age'):
#             print(f"Hello my name is {self.name} and I am {self.age} years old")
#         else:
#             print(f"Hello my name is {self.name} and my age is unknown")

# p1 = Person("John", 36)
# p1.myfunc()

# # Delete the age attribute
# del p1.age
# p1.myfunc()
