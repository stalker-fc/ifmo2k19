import random
import string
import numpy as np
from .constants import BYTE_LEN



def bin2array(data: str) -> np.ndarray:
    data = np.array([int(v) for v in data])
    assert min(data) >= 0 and max(data) <= 1
    return data

def array2bin(data: np.ndarray) -> str:
    return ''.join([str(v) for v in data])



def generate_message(message_len: int = 10) -> str:
    """Generates random ascii-string with given length."""
    return ''.join((random.choice(string.ascii_letters) for _ in range(message_len)))


def generate_binary_data(data_len: int = 8) -> str:
    return ''.join((random.choice(('0', '1')) for _ in range(data_len)))


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
