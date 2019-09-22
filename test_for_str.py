words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 2:
        words.insert(0, 'w')


print(words)

a = {0:1,
     "b":2,
     (1,2):12,
     "0":2}
print(a[0])
print(a["0"])
print(a[(1,2)])


ab = lambda a, b: a+b
ac = lambda a, b: a+b
print(ab(1,2))

def func(axa: int):
    return axa(3)

print(func(lambda a:a**a))

def func_2(a):
    return a**a

print(func(func_2))
