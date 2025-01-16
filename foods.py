# 复制数组
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 验证复制
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# 练习4-10
# foods_love = ['apple', 'banana', 'carrot', 'pizza', 'noodles']
# print(f"The first three items in the list are: {foods_love[0:3]}")
# print(f"Three items from the middle of the list are: {foods_love[1:4]}")
# print(f"The last three items in the list are: {foods_love[-3:]}")

#练习4-11
my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = my_foods[:]

my_foods.append('noodles')
friend_foods.append('juice')

print(f"My favorite foods areL {my_foods}.")
print(f"\n\tAnd my friend's favorite foods are: {friend_foods}.")

my_foods_output = [foods for foods in my_foods]
print(f"My favorite foods are {my_foods_output}.")

for foods in my_foods_output:
    print(foods)