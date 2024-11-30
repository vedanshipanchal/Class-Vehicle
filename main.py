#create a class
class enemy:
    def __init__(self,name,color,size):
      self.name = name
      self.color = color
      self.size = size


#object creation
ene1 = enemy("crab", "pink",5)
ene2 = enemy("snail", "green",3)

#display
print("i have enemy1. the name is",ene1.name)
print("i have crab and its size is:", ene1.size)
print("snail's color is:", ene2.color)
