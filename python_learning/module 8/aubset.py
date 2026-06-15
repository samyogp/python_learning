# subset.py
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))   # True
print(B.issuperset(A)) # True

C = {5, 6}
print(A.isdisjoint(C)) # True (no common)