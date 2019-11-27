"""Hamming code"""

from .base import message2bin
import itertools


def encode(message: str) -> str:
    data = message2bin(message)




def kek(data):
    data = insert_empty_parity_bits(data)

    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]
    parity_bits_values = [calc_parity_bit_value(data, count) for count in parity_bits_indices]

    data = list(itertools.chain.from_iterable(data))

    for idx, value in zip(parity_bits_indices, parity_bits_values):
        data[idx] = value

    print(''.join(data))


def insert_empty_parity_bits(data: str) -> str:
    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]

    new_data = []
    data_idx = 0
    for idx in range(len(data) + parity_bits_amount):
        if idx in parity_bits_indices:
            new_data.append('0')
        else:
            new_data.append(data[data_idx])
            data_idx += 1

    return ''.join(new_data)


def calc_parity_bit_value(data, parity_idx):
    start = parity_idx
    deg = parity_idx.bit_length()
    block = 2 ** deg
    step = 2 ** (deg + 1)

    value = 0
    for offset in range(block):
        value += sum([int(data[i]) for i in range(start + offset, len(data), step)])

    return str(value % 2)





