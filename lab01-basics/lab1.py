# Практична робота №1: Основи роботи в Python
# Код можна вставити в комірки Google Colab (кожен блок "# %%" — окрема комірка).

# %% a) Сортування словника за значеннями
d = {'a': 30, 'b': 10, 'c': 20}
sorted_d = dict(sorted(d.items(), key=lambda kv: kv[1]))
print("a)", sorted_d)

# %% b) Додавання ключа до словника
d = {0: 10, 1: 20}
d[2] = 30
print("b)", d)  # {0: 10, 1: 20, 2: 30}

# %% c) Об'єднання словників
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {**dic1, **dic2, **dic3}
print("c)", merged)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# %% d) Перевірка наявності ключа
key = 2
print("d)", key in merged)

# %% e) Ітерація по словнику через for
for k in merged:
    print("e) ключ:", k, "значення:", merged[k])

# %% f) Словник (x, x*x) для чисел від 1 до n
n = 5
squares_n = {x: x * x for x in range(1, n + 1)}
print("f)", squares_n)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# %% g) Квадрати чисел від 1 до 15
squares_15 = {x: x * x for x in range(1, 16)}
print("g)", squares_15)

# %% h) Створення set
s = {1, 2, 3, 3}
print("h)", s)

# %% i) Ітерація по set
for el in s:
    print("i)", el)

# %% j) Додавання значення до set
s.add(10)
print("j)", s)

# %% k) Видалення елемента з set (помилка, якщо елемента немає)
s.remove(2)
print("k)", s)

# %% l) Видалення елемента, якщо він є в set
s.discard(99)  # без помилки, навіть якщо 99 немає
if 3 in s:
    s.discard(3)
print("l)", s)

# %% m) Об'єднання та перетин sets
# У завданні написано "об'єднання", а в дужках "intersection" — показано обидві операції
a = {1, 2, 3}
b = {3, 4, 5}
print("m) об'єднання:", a | b, "| перетин:", a & b)

# %% n) Сума всіх елементів списку
lst = [1, 2, 3, 4, 5]
total = 0
for x in lst:
    total += x
print("n) сума:", total)

# %% o) Добуток всіх елементів списку
import math
print("o) добуток:", math.prod(lst))

# %% p) Найбільше та найменше значення у списку
print("p) max:", max(lst), "min:", min(lst))

# %% q) Сортування кортежів за останнім елементом
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = sorted(tuples, key=lambda t: t[-1])
print("q)", sorted_tuples)  # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# %% r) Видалення повторюваних елементів (порядок зберігається)
dups = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(dups))
print("r)", unique)  # [1, 2, 3, 4]

# %% s) Видалення 0-го, 4-го та 5-го елементів
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove_idx = {0, 4, 5}
result_s = [c for i, c in enumerate(colors) if i not in remove_idx]
print("s)", result_s)  # ['Green', 'White', 'Black']

# %% t) Добуток усіх значень у списку
values = (8, 2, 3, -1, 7)
print("t)", math.prod(values))  # -336

# %% u) Факторіал числа
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print("u)", factorial(5))  # 120

# %% v) Підрахунок великих та малих літер
text = 'The quick Brow Fox'
upper = sum(1 for ch in text if ch.isupper())
lower = sum(1 for ch in text if ch.islower())
print("v) No. of Upper case characters :", upper)
print("   No. of Lower case Characters :", lower)  # 3 і 12

# %% w) Патерн з зірочок
pattern_rows = [1, 1, 2, 3, 4, 3, 2, 1, 1]
for count in pattern_rows:
    print("* " * count)
