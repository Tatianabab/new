print('calculator')
a = int(input('Введите число'))
c = input('Введите символ + - / *')
b = int(input('Введите число'))
if c == '+':
    print('a', '+', 'b', '=', a+b)
if c == '-':
    print('a', '+', 'b', '=', a+b)
if c == '/':
    if b == 0:
        print("Делить на 0 нельзя!")
    else:
        print('a', '/', 'b', '=', a/b)
if c == '*':
    print('a', '*', 'b', '=', a*b)
