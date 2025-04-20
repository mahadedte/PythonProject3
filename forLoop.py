print('for-list')
lst = ['mahade', 10, True, False, 100]
lst[0] = 'Afia'
print(lst)
print(lst[2])
for value in lst:
    print(value)

print('for-tuple')
tpl = (10, True, False, 'Afia')
print(tpl[0])
for value in tpl:
    print(value)

print("for-set")
st = {10, 20, 'mahade', 'hasan', 10}
# {10, 'mahade', 20, 'hasan'}
print(st)

for value in st:
    print(value)

print('break with for loop')
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for item in lst:
    print(item)
    if item == 40:
        break

for item in lst:
    if item == 40:
        continue
    print(item)

for i in range(10):
    print(i)

for i in range(10, 100, 13):
    print(i)

# for-list
# ['Afia', 10, True, False, 100]
# True
# Afia
# 10
# True
# False
# 100
# for-tuple
# 10
# 10
# True
# False
# Afia
# for-set
# {'hasan', 10, 20, 'mahade'}
# hasan
# 10
# 20
# mahade
# break with for loop
# 10
# 20
# 30
# 40
# 10
# 20
# 30
# 50
# 60
# 70
# 80
# 90
# 100
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 23
# 36
# 49
# 62
# 75
# 88

for num in range(10, 30):
    if num % 2 == 0:
        print(num)
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24
# 26
# 28

for num in range(10, 30):
    if num % 2 != 0:
        print(num)

# 13
# 15
# 17
# 19
# 21
# 23
# 25
# 27
# 29

# tuple
print('tuple')
tpl = (10, 20, 'mahade', 30, True, False, 50, 60, 70, 80, 90, 100)
print(tpl)
print('tuple-break')
for value in tpl:
    print(value)
    if value == 20:
        break
print('tuple-continue')
for value in tpl:
    if value == 'mahade':
        continue
    print(value)

# tuple
# (10, 20, 'mahade', 30, True, False, 50, 60, 70, 80, 90, 100)
# tuple-break
# 10
# 20
# tuple-continue
# 10
# 20
# 30
# True
# False
# 50
# 60
# 70
# 80
# 90
# 100

# list comprehension
print('list-comprehension')
lst = [num for num in range(20)]
print(lst)
# list-comprehension
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# num is the loop variable that takes values from range(20).
# So inside the list comprehension, you should use num, not item.

lst = [num for num in range(16) if num % 2 == 0]
print(lst)
# [0, 2, 4, 6, 8, 10, 12, 14]

lst = [num for num in range(16) if num % 2 != 0]
print(lst)
# [1, 3, 5, 7, 9, 11, 13, 15]

print('list append')
lst = []
for i in range(10):
    lst.append(i)
    print(lst)

# list append
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# tpl = ()
# for i in range(5):
#     tpl.append(i)
#     print(tpl)
# You're trying to append elements to a tuple in Python, but tuples are immutable, which means you cannot change them (e.g., add items) after they are created.

st = set()
for i in range(5):
    st.add(i)
    print(st)
# {0}
# {0, 1}
# {0, 1, 2}
# {0, 1, 2, 3}
# {0, 1, 2, 3, 4}

lst = [x for x in range(10) if x % 2 == 0]
print(lst)
# [0, 2, 4, 6, 8]

lst = []
for x in range(10):
    if x % 2 != 0:
        lst.append(x)
        print(lst)

# [1]
# [1, 3]
# [1, 3, 5]
# [1, 3, 5, 7]
# [1, 3, 5, 7, 9]
