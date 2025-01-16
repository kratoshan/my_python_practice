bicycles = ['trek', 'connodale', 'redline', 'specialized']
#print(bicycles)
#print(bicycles[0])
#print(bicycles[1].title())
#print(bicycles[-1].upper())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#A practice
names = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(names[0].title())
print(names[1].upper())

message_ZS = f"Good morning {names[2].title()}."
message_LS = f"Nice to meet you {names[3].upper()}."
print(message_ZS)
print(message_LS)

traffic_tools = ['bicycle', 'motorcycle', 'bus', 'metro']
message_bicycle = f"I would like to own a Trek {traffic_tools[0].lower()} to go to work."
message_metro = f"But I have no money, so I go to work by {traffic_tools[-1].upper()}."
print(message_bicycle)
print(message_metro)