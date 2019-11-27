import random
import string
import numpy as np
from .constants import BYTE_LEN


def generate_message(message_len: int = 10) -> str:
    """Generates random ascii-string with given length."""
    return ''.join((random.choice(string.ascii_letters) for _ in range(message_len)))


def message2bin(message: str) -> str:
    """
    Converts ascii-letter message to bytes representation.

    :param message:
    :return:
    """
    codes = [ord(c) for c in message]
    if max(codes) > 255:
        raise ValueError('message must contains only letters between [0..255] ASCII-codes.')
    return ''.join([np.binary_repr(code, width=BYTE_LEN) for code in codes])


def bin2message(bin_message: str) -> str:
    if len(bin_message) % 8 != 0:
        raise ValueError('Can`t decode such message.')

    letters_amount = len(bin_message) // 8
    codes = []
    for i in range(letters_amount):
        start_idx = i * BYTE_LEN
        end_idx = start_idx + BYTE_LEN
        codes.append(bin_message[start_idx:end_idx])

    return ''.join([chr(int(c, 2)) for c in codes])
