
print('---Text---'.lstrip('-')) #обрезка символов слева
print('---Text---'.rstrip('-')) #обрезка символов справа
print('---Text---'.strip('-')) #обрезка символов слева и справа

print('- -Text?--'.strip(' -?')) #обрезка символов слева и справа

#регистры
print('- - some Text?--'.upper())
print('- - some Text?--'.lower())
print('- - some Text?--'.capitalize())
print('some Text'.capitalize()) #первая буква к верхнему регистру
print('some Text'.swapcase())
print('some text'.title())

#замена в строке
print('some Text'.replace('t', 'т'))
print('some Text'.replace('e', '0', 1))

#индексы
print('some Text'[-2])

#срезы. извлечение подстроки из строки
print('0123456789'[1:3])
print('0123456789'[1:])
print('0123456789'[:3])
print('0123456789'[:-2])
print('0123456789'[:7:3]) #step

#print('  43FFffff bgflbfg;l %t;gl;g'.center(30, fillchar))