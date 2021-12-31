#clear
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
car.clear()
print(car)
#Copy
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.copy()
print(x)
#fromkeys
x=('key 1','key 2','key 3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
#get
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.get("model")
print(x)
#Items
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.items()
print(x)
#keys
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.keys()
print(x)
#Pop
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
car.pop("model")
print(car)
#Pop item
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
car.popitem()
print(car)
#default
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.setdefault("model","Bronco")
print(x)
#update
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
car.update({"color":"white"})
print(car)
#values
car={
    "car":"ford",
    "model":"Mustang",
    "year":1964
    }
x=car.values()
print(x)
   
Output:
{}
{'car': 'ford', 'model': 'Mustang', 'year': 1964}
{'key 1': 0, 'key 2': 0, 'key 3': 0}
Mustang
dict_items([('car', 'ford'), ('model', 'Mustang'), ('year', 1964)])
dict_keys(['car', 'model', 'year'])
{'car': 'ford', 'year': 1964}
{'car': 'ford', 'model': 'Mustang'}
Mustang
{'car': 'ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
dict_values(['ford', 'Mustang', 1964])        



