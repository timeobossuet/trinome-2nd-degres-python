from math import*

a = int(float(input("a =")))
b = int(float(input("b =")))
c = int(float(input("c =")))

discriminant = ((b)**2)-4*(a)*(c)
print (discriminant)

if discriminant < 0:
    print("Il n'y a pas de solution")

if discriminant == 0:
    x = float(-(b)/(2*(a)))
    print("La solution est " + str(x))

if discriminant > 0:
    u = float((-(b) - sqrt(discriminant) ) / (2*(a)))
    v = float((-(b) + sqrt(discriminant) ) / (2*(a)))
    print("u = ", str(u) + " et v = ", str(v))
