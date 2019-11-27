"""Hamming code"""

from .base import message2bin
import itertools


def encode(message: str) -> str:
    data = message2bin(message)


def insert_empty_parity_bits(data: str) -> str:
    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]

    new_data = []
    for idx in range(len(data) + parity_bits_amount):
        if idx in parity_bits_indices:
            new_data.append('0')
        else:
            new_data.append(data[idx - parity_bits_amount])

    return ''.join(new_data)


def calc_parity_bit_value(data, parity_idx):
    start = parity_idx
    block_len = 2 ** (parity_idx + 1)

    value = 0
    for offset in range(block_len):
        value += sum([int(data[i]) for i in range(start + offset, len(data), block_len)])

    return str(value % 2)

def kek(data):
    data = insert_empty_parity_bits(data)

    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]
    parity_bits_values = [calc_parity_bit_value(data, idx) for idx in parity_bits_indices]


    data = list(itertools.chain.from_iterable(data))

    for idx, value in zip(parity_bits_indices, parity_bits_values):
        data[idx] = value

    print(''.join(data))
