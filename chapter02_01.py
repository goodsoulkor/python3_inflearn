# Chapter02-01
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
import sys
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()


# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션

print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.14)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s .format()을 사용할 때 s를 생략해도 된다.
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%5s' % ('pythonstudy'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%1.18f' % (3.12324252453234))
print('{:f}'.format(3.142312314123))
print('%06.2f' % (3.141235123234123))
print('{:06.2f}'.format(3.12312343423123))
