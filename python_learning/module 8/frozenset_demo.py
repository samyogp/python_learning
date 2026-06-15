# frozenset_demo.py
fs = frozenset([1, 2, 3])
# fs.add(4)   # AttributeError
print(fs)      # frozenset({1,2,3})

# Can be used as key
d = {fs: "immutable set"}
print(d[fs])   # "immutable set"