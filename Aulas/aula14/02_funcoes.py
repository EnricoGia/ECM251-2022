from math import sqrt

def bhaskara(a,b,c):
    x1 = (-b + sqrt((pow(b,2))-4*a*c))/(2*a)
    x2 = (-b - sqrt((pow(b,2))-4*a*c))/(2*a)
    return(x1,x2)

# main

a = 3
b = 10
c = 6

print("Raízes para (%ix² + %ix + %i) : %f %f" % ((a, b, c) + bhaskara(a,b,c))) # String formatting duas tuplas