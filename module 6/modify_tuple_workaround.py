# modify tuple example in python 

original = (1, 2, 3)
temp_list = list(original)
temp_list.append(4)
new_tuple = tuple(temp_list)
print(new_tuple)   # (1, 2, 3, 4)