#sort()_1
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sort()方法永久性修改元素排列顺序（首字母）
print(cars)

#sort()_2
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #传入参数reverse=True可以反向排序
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #sorted()方法可以让数组元素临时排序，不会改变原本的顺序

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))