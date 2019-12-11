import numpy as np
# Чтобы данный код мог исправить m-ошибок, нужно добавить 2 * m символов
# Пусть слово, которое мы собираемся кодировать имеет длину k
# Тогда длина кодированного слова n = k + 2 * m
# Перейдем к конкретным числам:
# Пусть длина кодированного слова n = 7, мы хотим исправить m = 2 ошибки
# Тогда длина полезной информации будет k = 4
# (7, 4) код
# https://habr.com/en/post/212095/
# http://vbond.kiev.ua/ru/post/Kodirovanie_informacii_s_primeneniem_kodov_Rida-Solomona/
# http://www.machinelearning.ru/wiki/images/0/00/pa_coding_algorithms.pdf


n = 7  # общая длина закодированного сообщения, бит
k = 3  # количество полезных бит
m = 4  # количество избыточных бит
g = [1, 0, 1, 1]  # g(x) = x^3 + x + 1, порождающий полином


def encode(data: str) -> str:
    data = np.array([int(v) for v in data])
    encoded = ...   # g(x) * u(x)

    return ''.join([str(v) for v in encoded])


def decode(data: str) -> str:
    ...
