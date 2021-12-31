#workaround
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 
Output:
  ('apple', 'kiwi', 'cherry')


#Dictionary
l1=['a','b','c','d','e']
l2=[1,2,3,4,5]
d=dict(zip(l1,l2))
print(d)
Output:
  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
