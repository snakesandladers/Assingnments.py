#Add method
fruits={"apple","mango","lemon"}
fruits.add("orange")
print(fruits)
#Set
fruits={"apple","mango","lemon"}
fruits.clear()
print(fruits)
#copy
fruits={"apple","mango","lemon"}
x=fruits.copy()
print(x)
#Difference
x={"apple","mango","lemon"}
y={"google","microsoft","apple"}
z=x.difference(y)
print(z)
#difference_update
x={"apple","mango","lemon"}
y={"google","microsoft","apple"}
x.difference_update(y)
print(x)
#Discard
fruits={"apple","mango","lemon"}
fruits.discard("apple")
print(fruits)
#Intersection
x={"apple","mango","lemon"}
y={"google","microsoft","apple"}
z=x.intersection(y)
print(z)
#intersection_update
x={"apple","mango","lemon"}
y={"google","microsoft","apple"}
x.intersection_update(y)
print(x)
#Isdisjoint
x={"apple","mango","lemon"}
y={"google","microsoft","apple"}
z=x.isdisjoint(y)
print(z)
#Issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z=x.issubset(y)
print(z)
#Issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z) 
#Pop
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits) 
#remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) 
#Symmetric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) 
#Symmeteric difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 
#Union 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) 
#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) 
Output:
  {'lemon', 'orange', 'apple', 'mango'}
set()
{'lemon', 'apple', 'mango'}
{'lemon', 'mango'}
{'lemon', 'mango'}
{'lemon', 'mango'}
{'apple'}
{'apple'}
False
True
True
{'banana', 'apple'}
{'cherry', 'apple'}
{'microsoft', 'cherry', 'banana', 'google'}
{'microsoft', 'cherry', 'banana', 'google'}
{'banana', 'apple', 'google', 'microsoft', 'cherry'}
{'banana', 'apple', 'google', 'microsoft', 'cherry'}
  


