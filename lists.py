# Creating a List
names = ["Rohit", "Madhu", "Karthik", "Sravani"]

# Accessing elements in lists. Index numbers start from 0 to N
names[0]

# Accessing using For each loop
test = input('Hey user, Enter few names: \n')
for name in test.split():
    print(name)

# Adding items
names.append("Lolo")
print(names)

# Deleting items
try:
    names.remove('rohit')
except:
    print('NO such element found!')

print(names)


