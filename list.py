# List() ----Hetro
# list() constructor---------------
lis1 = list((1, 'hi', 2, 3, 'hello', 4, 'welcome', 5.0))
print(lis1)

# check-------------------
lis = ['hi']
if "hi" in lis:
    print("Yes,'hi' is in the lis")

if lis[0] == "hi" in lis:
    print("Yes,'hi' is in the lis")

lis3 = [1, 2, 3, 1]
if lis3[0] <= lis3[3] in lis3:
    print("YES,it is true")

lis3 = [1, 2, 3, 1]
lis4 = [1, 5, 6, 7]
if lis3[0] <= lis4[0] in lis3 and lis4:
    print("YES,it is true")

# index

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10]
lis.index(4)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis.index('hi')

lis1.index(1), lis1.index(4)
lis1.index(1), lis2.index(7)

lis1.index(1), lis1.index('hi')
# ---Try
lis1.index(4 and 2)

lis1.index(2 and 4)

lis1.index(2 or 4)
# ---opposite
lis1.index(1) and lis1.index('hi')

lis1.index(1) or lis1.index('hi')

# Access------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10]
print(lis1[2])

print(lis1[1:4], lis2[0:2])

print(lis1[2], lis2[1])

lis3 = lis1[2], lis2[1]
print(lis3)

lis3 = lis1[2] + lis2[1]
print(lis3)

# Append-------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.append('wellcome')
print(lis1)

lis1 = [('hi', 'hello')]
lis1.append(('wellcome', 'thans'))
print(lis1)

# Insert------------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.insert(3, 'wellcome')
print(lis1)

lis1 = [('hi', 'hello')]
lis1.insert(3, ('wellcome', 'thanks'))
print(lis1)

# Copy-------------------------------------------
lis1 = [1, 2, 3]
lis2 = [5, 6, 7]
lis1 = lis2
lis1.insert(0, 0)
print(lis1, lis2)

lis1 = [1, 2, 3]
lis3 = lis1.copy()
print(lis3)
lis1.insert(0, 0)
print(lis3)

lis2 = list(lis1)
print(lis2)
lis1.insert(0, 0)
print(lis2)

# Extend--------------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10]
lis1.extend(lis2)
print(lis1)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10]
lis3 = [1, 2, 3, 4, 5]
lis1.extend(lis2), lis1.extend(lis3)
print(lis1)

# Remove-----------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.remove('hi')
print(lis1)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.remove(3), lis1.remove(2)
# --(None, None)
print(lis1)

# POP-------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.pop(0)
print(lis1)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.pop(0), lis1.pop(1)
# ----(1, 3)
print(lis1)

# Delete-------------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
del lis1[0]
print(lis1)

del lis1[0], lis1[0]

del lis1
# -- print(lis1)

# Clear-----------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis1.clear()
print(lis1)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10, 11, 12, 13]
lis1.clear(), lis2.clear()
print(lis1, lis2)

# count-------------------------------------------------------------
lis1 = [1, 2, 3, 4, 5, 'hi', 'hello', 7, 8, 9, 10, 1, 2, 3, 4, 5]
lis1.count(1)

lis1.count(1), lis1.count(2)

lis2 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 1, 2, 3, 4, 5]
lis1.count(1), lis2.count(2)

# Reverse-------------------------------------------
lis1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 1, 2, 3, 4, 5]
lis1.reverse()
print(lis1)

lis1 = [1, 2, 3, 4, 5, 'hi', 'hello']
lis2 = [7, 8, 9, 10, 11, 12, 13]
lis1.reverse(), lis2.reverse()
print(lis, lis2)

# sort--------------------------------------
lis1 = [1, 2, 5, 7, 9, 3, 6, 4, 8]
lis1.sort()
print(lis1)

lis1.sort(reverse=True)
print(lis1)

lis1 = [1, 2, 5, 7, 9, 3, 6, 4, 8]
lis2 = [7, 8, 11, 16, 9, 12, 13]
lis1.sort(), lis2.sort()
print(lis1, lis2)

lis1.sort(), lis2.sort(reverse=True)
print(lis1, lis2)

# ----case
lis1 = ['hi', 'wellcome', 'hello', 'thanks', 'bye']
lis1.sort()
print(lis1)

lis1 = ['hi', 'wellcome', 'hello', 'thanks', 'bye', 'Hi', 'Wellcome', 'Hello', 'Thanks', 'Bye']
lis1.sort()
print(lis1)

lis1.sort(key=str.lower)
print(lis1)
lis1.sort(key=str.upper)
print(lis1)

# Join-------------------------------------
lis1 = [1, 2, 3, 4, 5]
lis2 = [6, 7, 8, 9, 10]
lis3 = lis1 + lis2
print(lis3)

lis1 = [1, 2, 3, 4, 5]
lis2 = ['hi','hello']
lis3 = lis1 + lis2
lis4=lis1,lis2
print(lis3)
print(lis4)

lis3 = lis1[0],lis2[0]
print(lis3)
# ----for more refere access


import numpy
lis=[[1,2,3,4],[5,6,7,8,9],['hi','hello'],['welcome']]
lis2=list(numpy.concatenate(lis).flat)
print(lis2)
