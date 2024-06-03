# ## 1
# ## Try this.
# from dataclasses import dataclass

# @dataclass
# class Dog:
#     name: str
#     age: int
#     breed: str
   
# d1 = Dog("Tucker", 4, "Cocker Spaniel")
# d2 = Dog("Henry", 8, "Bassett Hound")
# # You have the option of using named keyword arguments:
# d3 = Dog(name="Henry", age=8, breed="Bassett Hound")

# print(d1.name)

# ## In this example, Dog is a "class", which can be thought of as a 
# ## template that describes what data we want to include every time 
# ## we use the Dog class.
# ## The variables d1 and d2 are called "instances" of the class Dog. 
# ## It's also possible to call them "objects".
# ## So far, this doesn't provide any new features, but it allows you to 
# ## organize data into named attributes. It also ensures that every Dog 
# ## object that you create (or instantiate) has the 
# ## required attributes: name, age, and breed.

# ## 2
# ## Fill in the blanks:
# print(f"The dog named {d1.name} is {___} years old. His/her breed is {___}.")

# ## 3
# ## Try this.
# from dataclasses import dataclass

# @dataclass
# class Dog:
#     name: str
#     age: int
#     breed: str

# dogs = [
#     Dog("Tucker", 4, "Cocker Spaniel"),
#     Dog("Henry", 8, "Bassett Hound")
# ]

# print("The first item of our dogs list:")
# print(dogs[0])
# print("The name of the first dog:")
# print(dogs[0].name)

# ## 4
# ## Make a Car class that has at least three attributes.
# ## Make a list of at least three Car objects (a.k.a. instances).
# ########################
# ##  INSTRUCTOR-CHECK  ##
# ########################