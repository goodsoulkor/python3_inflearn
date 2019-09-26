# chapter 04-03
# 파이썬 반복문
# while 실습

# while <expr>:
#   <statement(s)>

# ex1
n = 5
while n > 0:
    print(n)
    n -= 1

# ex2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

# ex3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop end')
print()

# ex4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop end')

print()

# ex5
# if 중첩

i = 1

while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1
print()

# ex6
# while - else
n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')
print()

# ex7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'Not found in list.')
print()

# 무한반복
# while True:
#   print('Foo')

# ex8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
