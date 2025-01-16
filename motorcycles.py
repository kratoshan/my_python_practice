motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #使用此方法会修改数组内指定的元素
print(motorcycles)

#append()_1
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') #最简单的添加元素的方法，默认添加到数组末尾
print(motorcycles)

#append()_2
motorcycles = [] #穿件一个空数组，用append()方法添加元素，动态创建数组

motorcycles.append('honda')
motorcycles.append('yahama')
motorcycles.append('suzuki')
print(motorcycles)

#insert()
motorcycles = ['honda', 'yahama', 'suzuki']

motorcycles.insert(2, 'ducati') #使用insert()可以将新元素插入数组中任何位置
print(motorcycles)

#del
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)

del motorcycles[0] #利用del方法和索引可以删除数组中的任何一个元素
print(motorcycles)

#pop()_1
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
#方法pop()可以直接删除数组末尾的元素，并可以直接使用它，简单理解为弹出数组最后一个值并弹射给新的变量
print(motorcycles)
print(popped_motorcycle)

#pop()_2
motorcycles = ['honda', 'yahama', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#pop()_3
motorcycles = ['honda', 'yahama', 'suzuki']

first_owned = motorcycles.pop(1) #在括号中加入索引位置，可以弹出任何一个值
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#remove()_1
motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') #不知道变量位置的时候可以使用remove方法删除值
print(motorcycles)

#remove()_2
motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")