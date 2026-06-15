# this is the example of the set operations on python.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)


print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
