t1 = (1, 2, 3)
t2 = ('a', 'b', ('ab', 'cd'))
t3 = ('tuple', (1, 2), [3,4])
t4 = ()
t5 = (1,)
t6 = 1, 2, 3
t7 = 1,

print(t6)
x, y, z = t6
print(x, y, z)

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 5)
print(result)

print('성남캠퍼스\t인공지능소프트웨어과')
print('성남캠퍼스\n인공지능소프트웨어과')
print('성남캠퍼스\\인공지능소프트웨어과')

l = 'python'
print(f"Hello, {l.upper()}!")