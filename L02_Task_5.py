# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for i in range(32, 128, 10):
    for j in range(i, i + 10):
        print("{0:3} {1:3}".format(j, chr(j)), end=' ')
        if j >= 127:
            break
    print()
