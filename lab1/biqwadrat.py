import math

def bi(a, b, c):
    if a == b == 0:
        if c == 0:
            return ['Корней бесконечно много']
        else:
            return ['Некорректный ввод']

    x = []
    def push_x(t):
        if t == 0:
            x.append(0)
        elif t > 0:
            x.append(math.sqrt(t))
            x.append(-math.sqrt(t))

    d1 = b * b - 4 * a * c

    if a == 0:
        if b * c > 0:
            return ['Корней нет!']
        else:
            push_x(-c / b)
            return x
    
    if d1 > 0:
        t = (-b + math.sqrt(d1)) / (2 * a)
        push_x(t)
            
        t = (-b - math.sqrt(d1)) / (2 * a)
        push_x(t)
        return x

    if d1 == 0:
        t = -b / (2 * a)
        push_x(t)
        
    if len(x) == 0:
        x.append('Корней нет!')
    return x

def read():
    while 1:
        try:
            z = float(input())
            break
        except:
            print('Некорректный ввод, попробуйте еще раз:')
    return z


print('Лункин Владимир ИУ5-55Б')
print('Введите A: ')
a = read()
print('Введите B: ')
b = read()
print('Введите C: ')
c = read()

print(*bi(a, b, c))
