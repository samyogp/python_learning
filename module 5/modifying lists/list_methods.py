# list methods example in python 

scores = [85, 92, 78, 90, 85]
print(len(scores))
print(scores.index(90))
print(scores.count(85))


scores.sort()
print(scores)

scores.reverse()
print(scores)
# copying a list 
new_scores = scores.copy()
new_scores.append(100)
print(scores)
print(new_scores)

