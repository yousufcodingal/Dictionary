my_dictionary = {'codingal':2, 'is':2, 'best':2, 'for':1, 'coding':1}
print(my_dictionary)
k = 2
count = 0 
for key in my_dictionary:
    if my_dictionary[key]==k:
        count = count + 1
print(count)
