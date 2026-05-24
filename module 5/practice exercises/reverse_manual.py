# reverse a list without using reverse()
original = [1, 2, 3, 4, 5]
reverse_list = []
for i in range(len(original)-1, -1, -1):
    reverse_list.append(original[i])
    print(reverse_list)
    