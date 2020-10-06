#Program to find area of circle using Pyhton 

from math import pi
r=float(input("Enter the radius:"))
print("The area of the circle with radius" + str(r) + "is :" + str(pi * r **2)
fn=input("Enter Filename:")
f=fn.split(".")
print("Extension of the fils is : " + f[-1])
