#workaround
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 



#Dictionary
l1=['a','b','c','d','e']
l2=[1,2,3,4,5]
d=dict(zip(l1,l2))
print(d)