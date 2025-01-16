#练习4-3
#numbers = range(1, 21)
#for number in numbers:
#    print(number)

numbers = [number for number in range(1, 21)]
print(numbers)

#练习4-4、4-5
numbers_million = [number_m for number_m in range(1, 1000001)]
#print(numbers_million)
print(f"1-1000000中最小的数字是：{min(numbers_million)}")
print(f"1-1000000中最大的数字是：{max(numbers_million)}")
print(f"1-1000000的和是：{sum(numbers_million)}")

#练习4-6
numbers_ji = [ji for ji in range(1, 20, 2)]
print(numbers_ji)

numbers_ji_2 = list(range(1, 20, 2))
print(numbers_ji_2)

#练习4-7
numbers_3 = [multi_3 for multi_3 in range(3, 30, 3)]
print(numbers_3)

numbers_3_2 = []
for number in range(3, 30, 3):
    numbers_3_2.append(number)

print(numbers_3_2)

#练习4-8
number_lifang = []
for num in range(1, 11):
    number_lifang.append(num **3)

print(number_lifang)

#练习4-9
numbers_lifang2 = [num **3 for num in range(1, 11)]
print(numbers_lifang2)