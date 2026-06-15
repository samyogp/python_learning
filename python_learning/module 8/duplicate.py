# dedupe.py
list_with_dupes = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_with_dupes))
print(unique_list)   # [1,2,3,4,5] (order may differ)