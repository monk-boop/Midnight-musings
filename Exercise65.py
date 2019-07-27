from math import sqrt
x1  =float(input("Enter the x value:"))
y1 = float(input("Enter the y value:"))

prev_x = x1
prev_y = y1

line = float(input("Enter the x value:"))

while line != '':
  x = float(line)
  y = float(input("Enter the value of the y coordinate:"))

  area = sqrt((prev_x-x)**2 + (prev_y-y)**2)
  prev_x = prev_x-x
  prev_y = prev_y-y
  line = input("Enter the x value :")

print("Area is ", area)




