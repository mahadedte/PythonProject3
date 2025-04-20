# list
lst = [x for x in range(10)]
print(lst)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst = [3 * x + 2 for x in range(10)]
print(lst)
# [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

lst = [x for x in range(10)]
print(lst[0:5])
# [0, 1, 2, 3, 4]
print(lst[10:0:-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst[8:4:-1])
# [8, 7, 6, 5]

# Second Slice: lst[10:0:-1]
# Syntax: lst[start:stop:step] (step = -1, meaning reverse traversal)
# Behavior:
# Start (10): Out of bounds (max valid index is 9).
# Python adjusts it to the last index (9).
# Stop (0): The slice stops before reaching index 0 (exclusive).
# Step (-1): Moves backward (right to left).
# Indices included: 9, 8, 7, 6, 5, 4, 3, 2, 1 → Values: [9, 8, 7, 6, 5, 4, 3, 2, 1]

lst = []
for x in range(50):
    lst.append(x)
    print(lst)
    if x % 2 == 0:
        break

lst = []
for x in range(50):
    if x % 2 == 0:
        continue
    lst.append(x)
    print(lst)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# Important Note: break like with cute girl relationship, after relation breakup occurs:
#   (after print then break) , continue is when girl not cute then skip and print another.

lst = []
x = 20
i = 10
while i <= x:
    lst.append(i)
    i += 1
    print(lst)
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lst1 = [x for x in range(10) if x % 2 == 0]
lst2 = ['mahade', 'hasan', 'jony']
lst1.append(lst2)
print(lst1)
# [0, 2, 4, 6, 8, ['mahade', 'hasan', 'jony']]

# membership testing
lst = [x for x in range(1000)]
print(10001 in lst)
# False

# list insert()
lst = [10, 20, 30, 40, 50, 'mahade', 'hasan', 'Jony']
lst.insert(1, 500)
print(lst)
# [10, 500, 20, 30, 40, 50, 'mahade', 'hasan', 'Jony']

# list append()
lst = [10, 20, 30, 40, 50, 'mahade']
lst.append('hasan')
print(lst)
# [10, 20, 30, 40, 50, 'mahade', 'hasan']
lst2 = ['bonna', 'badhan']
lst.append(lst2)
print(lst)
# [10, 20, 30, 40, 50, 'mahade', 'hasan', ['bonna', 'badhan']]
print(len(lst))
# 8
# Your code uses append(), which adds the entire lst2 as a single nested list, making the length 8.
# If you wanted to merge the lists, you should use extend(), which would make the length 9.
lst.extend(lst2)
print(lst)
# [10, 20, 30, 40, 50, 'mahade', 'hasan', ['bonna', 'badhan'], 'bonna', 'badhan']
print(len(lst))
# 10

# list remove
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lst.remove(20)
print(lst)
# [10, 30, 40, 50, 60, 70, 80, 90, 100]
# list pop
lst.pop()
print(lst)
# [10, 30, 40, 50, 60, 70, 80, 90]
# list del
del lst[2]
print(lst)
# [10, 30, 50, 60, 70, 80, 90]

lst = [x for x in range(10)]
print(lst)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list reverse
lst.reverse()
print(lst)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# list count
print(lst.count(1))
# 1

lstX = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'Copy']
lstY = lstX.copy()
print(lstY)
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 'Copy']
lstY.reverse()
print(lstY)
# ['Copy', 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

lst = [10, 30, 20, 80, 70, 90, 100, 110, 50, 40, 60, 30]
lst.sort()
print(lst)
# [10, 20, 30, 30, 40, 50, 60, 70, 80, 90, 100, 110]

lst.sort(reverse=True)
print(lst)
# [110, 100, 90, 80, 70, 60, 50, 40, 30, 30, 20, 10]

# immutable - mutable process
tpl = (10, 20, 30, 'mahade', 'hasan', 100)
lstTemp = list(tpl)
lstTemp.append(10)
print(lstTemp)
# [10, 20, 30, 'mahade', 'hasan', 100, 10]
lstTemp.extend([20])
print(lstTemp)
# [10, 20, 30, 'mahade', 'hasan', 100, 10, 20]
# The extend() method expects an iterable (like a list, tuple, string), but you're passing an integer (20), which is not iterable. Hence, Python throws a TypeError.
tpl = tuple(lstTemp)
print(tpl)
# (10, 20, 30, 'mahade', 'hasan', 100, 10, 20)
print(type(tpl))
# <class 'tuple'>
print(type(lstTemp))
# <class 'list'>
print(tpl[2])
# 30
tpl = (10, 20, 30, [100, 110], 'mahade', 'hasan')
print(len(tpl))
# 6
print(tpl[0:3])
# (10, 20, 30)
print(tpl[0:4])
print(tpl[6:0:-1])
# ('hasan', 'mahade', [100, 110], 30, 20)

# mutable-immutable
lstnew = [10, 20, 30, 'mahade', 'hasan']
print(lstnew)
print(type(lstnew))
lstnew.append('afra')
tplnew = tuple(lstnew)
print(tplnew)
print(type(tplnew))

# [10, 20, 30, 'mahade', 'hasan']
# <class 'list'>
# (10, 20, 30, 'mahade', 'hasan', 'afra')
# <class 'tuple'>

tpl1 = (10, 20, 30, 40, 50)
tpl2 = (60, 70, 80, 90, 100)

tpl3 = tpl1 + tpl2
print(tpl3)
# (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# membership check
print(60 in tpl3)
# True
del tpl2
print(tpl3)

tpl1 = (10, 20, 30, 40, 50)
tpl2 = (60, 70, 80, 90, 100)

# tpl3 = tpl1 + tpl2  # This creates a new tuple and assigns it to tpl3
# del tpl2  # This deletes the variable tpl2, not its contents from tpl3
# print(tpl3)  # This is perfectly valid and will print the combined tuple
