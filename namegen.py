# name generator
import random

c = ['b','c','d','f','g','h','j','k','l','m','n',
'p','q','r','s','t','v','w','x','y','z']
v = ['a', 'e', 'i', 'o', 'u']
a = c + v
opt = ''
x = 0
name = ''

# name length
# e = int(input("lenth: "))
e = 10
name = 'Rony ' + a[random.randint(0,22)].upper()
x = len(name)
opt += name

# rule: after c must be a
for i in range(e):
    fst = a[random.randint(0,25)]
    opt += fst

    if opt[0 + x] in c:
        fst = v[random.randint(0, 4)]
        opt += fst
        x += 2
    else:
        x += 1

print(opt[:e])
