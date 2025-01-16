name_invited = ['zhangsan', 'lisi', 'wangwu']
name_invited_shown = f"{name_invited[0].title()}, {name_invited[1].title()}, {name_invited[-1].title()}"
print("We have 3 people to invite, they are ",name_invited_shown,".")

message_invited = f"I want to invite {name_invited[0].title()} to my birthday party!"
print(message_invited)

print(f"Unfortuntely, {name_invited[0].title()} cannot be here.")
name_invited[0] = 'zhaoliu'
print(f"We have to change Zhangsan to {name_invited[0].title()}.")
name_invited_shown = f"{name_invited[0].title()}, {name_invited[1].title()}, {name_invited[-1].title()}"
print(f"So, the new list of peopoe who will be invited are", name_invited_shown,".")

name_invited.insert(0, 'laoliu')
name_invited.insert(2, 'zhouqi')
name_invited.append('shiba')
name_invited_shown = f"{name_invited[0].title()}, {name_invited[1].title()}, {name_invited[2].title()}, {name_invited[3].title()}, {name_invited[4].title()}, {name_invited[-1].title()}"
print(f"\'Cause we have a big table, we can invite more people to this party, they are", name_invited_shown,".")

print("Oh shit, the table we booked cannot deliver on time, we cannot invite so many people.")
print(name_invited)
poped_laoliu = name_invited.pop(0)
print(f"I\'m so sorry {poped_laoliu.title()} that we cannot invite you.")
poped_zhaoliu = name_invited.pop(0)
print(f"And for {poped_zhaoliu.title()}, we cannnot invite, too.")
poped_zhouqi = name_invited.pop(0)
print(f"We cannot also invite {poped_zhouqi.title()}.")
poped_lisi = name_invited.pop(0)
print(f"And the last one we cannot invite is Mr.{poped_lisi.title()}.")

#Practice 3-9
count_peoppe_invited = len(name_invited)
print(f"So, till now, we only invite {count_peoppe_invited} people to our party.")

name_invited_shown = f"{name_invited[0].title()} and {name_invited[1].title()}"
print(f"And the two people left can still be invited to party, they are {name_invited_shown}.")

del name_invited[0]
del name_invited[0]
print(name_invited)