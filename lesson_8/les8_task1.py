# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
#

from hashlib import sha1


def func_1(string):
    result = {}

    for i in range(0, len(string) - 1):
        result.update({string[0:i]: sha1(string[0:i].encode('utf-8')).hexdigest()})

        for j in range(len(string), 0, - 1):
            result.update({string[i:j]: sha1(string[i:j].encode('utf-8')).hexdigest()})

    final = [i for i in result.keys() if i not in ('', string)]

    return f'Количество подстрок: {len(final)}', final


print(func_1('papa'))
print(func_1('beepbeep'))
print(func_1('sova'))
