# condition elif while
age = int(input('x='))
if age < 30:
    print('less than 30')
elif age <= 40:
    print('less than or equal 40')
else:
    print('greater than 40')

# x=40
# less than or equal 40

x = int(input('x='))
if x == 1:
    print('one')
elif x == 2:
    print('two')
elif x == 3:
    print('Three')
elif x == 4:
    print('Four')
else:
    print('Other Value')

i = 1
while i <= 10:
    print(i)
    i += 1

password = input('password: ')
while password != 'secret':
    print('password not matched')
    password = input('password: ')
    if password == 'secret':
        print('login successful')

x = int(input('x='))
y = 'mahade'
z = 0

while z < x:
    print(y)
    z = z + 1

# x=5
# mahade
# mahade
# mahade
# mahade
# mahade

# break
while z < x:
    print(y)
    z = z + 1
    if z == 3:
        break
# x=10
# mahade
# mahade
# mahade

# continue
x = int(input('x='))
z = 0
while z < x:
    z = z + 1
    if z == 3:
        continue
    print(z)
