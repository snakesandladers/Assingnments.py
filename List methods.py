#Assingnment 2.2
#Append 
fruits=['apple','banana','mango']
fruits.append("orange")
print(fruits)
#Clear
fruits.clear()
print(fruits)
#Copy 
fruits=['apple','banana','mango']
x=fruits.copy()
print(x)
#Count
fruits=['apple','banana','mango']
x=fruits.count("mango")
print(x)
#Extend
fruits=['apple','banana','mango']
cars=['BMW','BENZ','AUDI']
fruits.extend(cars)
print(fruits)
#index
fruits=['apple','banana','mango']
x=fruits.index("mango")
print(x)
#Insert
fruits=['apple','banana','mango']
fruits.insert(1,'orange')
print(fruits)
#pop
fruits=['apple','banana','mango']
fruits.pop(1)
print(fruits)
#Remove 
fruits=['apple','banana','mango']
fruits.remove("apple")
print(fruits)
#Reverse
fruits=['apple','banana','mango']
fruits.reverse()
print(fruits)
#Sort
cars=['BMW','BENZ','AUDI']
cars.sort()
print(cars)

OUTPUT:
  ['apple', 'banana', 'mango', 'orange']
[]
['apple', 'banana', 'mango']
1
['apple', 'banana', 'mango', 'BMW', 'BENZ', 'AUDI']
2
['apple', 'orange', 'banana', 'mango']
['apple', 'mango']
['banana', 'mango']
['mango', 'banana', 'apple']
['AUDI', 'BENZ', 'BMW']

