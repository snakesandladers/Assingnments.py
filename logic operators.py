x=5
y=4
#and operator 
N=x=y and y<x
print(N)
#or operator 
N=x>y or y>x
print(N)
#not operator 
N=not(x<y and y>x)
print(N)

output:
True
True
False
