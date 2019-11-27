"""Hamming code"""

import random
import itertools
from typing import Optional
from .base import message2bin, bin2message


def encode(message: str) -> str:
    """
    Encodes ascii-letter`s string to binary representation using hamming code.

    :param message:
    :return:
    """
    data = message2bin(message)
    data = insert_empty_parity_bits(data)
    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]
    parity_bits_values = [calc_parity_bit_value(data, count) for count in parity_bits_indices]

    data = list(itertools.chain.from_iterable(data))

    for idx, value in zip(parity_bits_indices, parity_bits_values):
        data[idx] = value

    return ''.join(data)


def decode(data: str) -> str:
    """
    Decodes binary string of hamming code to ascii-letter`s string.

    :param data:
    :return:
    """
    parity_bits_amount = len(data).bit_length()
    parity_bits_indices = [(1 << i) - 1 for i in range(parity_bits_amount)]
    init_parity_bits = [data[idx] for idx in parity_bits_indices]

    bla = list(itertools.chain.from_iterable(data))
    for idx in parity_bits_indices:
        bla[idx] = '0'

    msg = ''.join(bla)
    parity_bits_values = [calc_parity_bit_value(msg, count) for count in parity_bits_indices]
    if parity_bits_values != init_parity_bits:
        error_idx = 0
        for a, b, c in zip(init_parity_bits, parity_bits_values, parity_bits_indices):
            error_idx += c
        bla[error_idx] = str((int(data[error_idx]) + 1) % 2)

    res = []
    for idx in range(len(bla)):
        if idx not in parity_bits_indices:
            res.append(bla[idx])

    res = ''.join(res)
    return bin2message(res)


def set_error(data: str, error_idx: Optional[int] = None) -> str:
    """
    Randomly changes one byte in data.

    :param data:
    :return:
    """
    if not all((c in ('0', '1') for c in data)):
        raise ValueError('Incorrect input value.')
    if error_idx is None:
        error_idx = random.randint(0, len(data))
    elif error_idx + 1 > len(data) or error_idx < 0:
        raise ValueError('Incorrect index values.')

    error_val = str((int(data[error_idx]) + 1) % 2)

    return ''.join([data[0:error_idx], error_val, data[error_idx + 1:]])


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
