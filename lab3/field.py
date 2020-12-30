def field(items, *args):
    try:
        assert len(args) > 0
    except AssertionError:
        print("Нет второго рагумента")

    if len(args) == 1:
        for item in items:
            if args[0] in item and item.get(args[0]):
                yield item.get(args[0])
    else:
        for item in items:
            s = {}
            for key in args:
                if key in item and item.get(key):
                    s.update({key: item.get(key)})
            yield s


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'blue'},
    {'title': 'Пуфик', 'price': 5000, 'color': 'red'}
]

f = field(goods, 'title', 'price')
for k in f:
    print(k, end=', ')
print()
print()

f = field(goods, 'price', 'color')
for i in f:
    print(i, end=', ')
print()
print()

f = field(goods, 'title')
for i in f:
    print(i, end=', ')
