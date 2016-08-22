class Car():
 counter = 0
 def __init__(self):
  self.__class__.counter += 1
  print "Created car number: " + str(self.__class__.counter)
Car()
Car()
Car()
Car()
Car()