scores = {"math": 56, "science": 78, "english": 90}
removed = scores.pop("science")
print(scores)
print(removed)


last = scores.popitem()
print(last)
print(scores)


scores.clear()
print(scores)
