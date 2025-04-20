# A set is an unordered, mutable, and unique collection of unique elements in Python.
# Key Properties:
# No duplicates: {1, 2, 2, 3} → {1, 2, 3}
# Unordered: Items have no fixed position.
# Mutable: You can add/remove items, but elements must be immutable (like numbers, strings, tuples).
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric Difference: {1, 2, 4, 5}

a = {10, 20, 30, 40, 50}
b = {50, 60, 70, 80, 90, 100}
c = a | b
print(c)
# {100, 70, 40, 10, 80, 50, 20, 90, 60, 30}
print(sorted(c))
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Sets do not guarantee order — it's by design (for performance).
# Use sorted(set) if you want ordered output.

c = a & b
print(c)
# {50}

c = a - b
print(c)
# {40, 10, 20, 30}

c = a ^ b
print(c)
print(sorted(c))
# [10, 20, 30, 40, 60, 70, 80, 90, 100]

# st = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, {'mahade', 'hasan', 'jony'}}
# print(st)

# Here, you're trying to add a set inside another set.
# But sets are unhashable, and only hashable (immutable) objects can go inside a set.

# ✅ How to Fix It:
# You can convert the inner set to a tuple, which is hashable:

st = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, ('mahade', 'hasan', 'jony'), True, False}
print(st)
# {False, True, 100, 70, 40, 10, ('mahade', 'hasan', 'jony'), 80, 50, 20, 90, 60, 30}
# Now it works because a tuple is immutable and hashable.

st.add(500)
print(st)
# {False, True, 100, 90, 70, 40, 10, 80, 50, 20, 500, ('mahade', 'hasan', 'jony'), 60, 30}
st.remove(20)
print(st)
print(20 in st)
# {False, True, 100, 70, 40, 10, 80, 50, 500, ('mahade', 'hasan', 'jony'), 90, 60, 30}
# False
st.clear()
print(st)
# set()

# frozenset
# What is a frozenset?
# A frozenset is just like a regular set, but it is immutable — meaning:
# ❌ You cannot add, remove, or update its elements.
# ✅ You can still perform set operations like union, intersection, etc.

norm_set = {10, 20, 30, 40, 50, 'mahade', 'hasan'}
frozen = frozenset(norm_set)
print(frozen)
print(type(frozen))
# frozenset({'mahade', 50, 20, 'hasan', 40, 10, 30})
# <class 'frozenset'>

# dictionary
dct = {'1': 'mahade', '2': 'hasan', '3': 'Jony'}
print(dct)
# {'1': 'mahade', '2': 'hasan', '3': 'Jony'}

print(dct.keys())
# dict_keys(['1', '2', '3'])
print(dct.values())
# dict_values(['mahade', 'hasan', 'Jony'])

dct2 = dct.copy()
print(dct2)
# {'1': 'mahade', '2': 'hasan', '3': 'Jony'}
# value change
dct2['3'] = 'afra'
print(dct2)
# {'1': 'mahade', '2': 'hasan', '3': 'afra'}

dct2['4'] = 'badhan'
print(dct2)
# {'1': 'mahade', '2': 'hasan', '3': 'afra', '4': 'badhan'}
del dct2['1']
print(dct2)
# {'2': 'hasan', '3': 'afra', '4': 'badhan'}

dct2.popitem()
print(dct2)
# {'2': 'hasan', '3': 'afra'}
