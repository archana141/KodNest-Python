# normal assignment 
original =[[10,20],[30,40]]
copy = original
copy[0][0] = 100
print(copy) # 100,20/30,40
print(original) # 100,20/30,40

# shallow copy 
original =[[10,20],[30,40]]
shallowcopy = original.copy()
shallowcopy[0][0] = 100
print(shallowcopy) # 100,20/30,40
print(original) # 100,20/30,40

# deep copy 
original =[[10,20],[30,40]]
deepcopy = original.copy()
deepcopy[0][0] = 100
print(deepcopy) # 100,20/30,40
print(original) # 100,20/30,40


