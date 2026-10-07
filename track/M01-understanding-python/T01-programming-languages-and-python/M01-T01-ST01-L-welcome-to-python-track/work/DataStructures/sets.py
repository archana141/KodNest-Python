# Sets are unordered, unindexed and mutable, unchangeable
# Don't support duplicate values

s = {1, 2, 3, 4, 5}
# print(s, s[1])
# s[2] = 300 # sets are immutable
s.add(7)
s.update({8, 9})
# s.remove(10)
s.discard(10)
s.pop()
s.pop()
s.clear()
del s
# print(type(s), s)

s1 = {1,2,3,"Hello", 1.2, True, 0, 1.2324, 1, 2, False}
print(s1)

# Constructor of set
s2 = set()
print(s2, type(s2)) # empty set
s3 = set([1, 2, 3, 4])
print(s3, type(s3))
#loop
for n in s3:
    print(n)

# Immutable - frozenset
fs = frozenset([1, 2, 3])
print(fs, type(fs))
fs.add(6) # not possible