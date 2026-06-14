# adding and removing items example 
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)
s.add(2)
print(s)

s.update([5, 6, 7])
print(s)
s.remove(5)
s.discard(10)
print(s)
pooped = s.pop()
print(pooped)

s.clear()
print(s)
