d= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique = set() #set to  add only unique value

for items in d:
    for value in items.values():
        unique.add(value)

print(unique)