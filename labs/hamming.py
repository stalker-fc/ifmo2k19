"""Hamming code"""

import math

from typing import List
from itertools import chain

from .base import message2bin



def encode(message: str) -> List['str']:
    bin_view = message2bin(message)
    letter_len = len(bin_view[0])
    bin_msg = ''.join(bin_view)







def set_control_bytes(msg: str) -> str:

    control_bytes_amount = len(msg).bit_length()
    control_indices = [1 << i for i in range(control_bytes_amount)]


    encoded = []
    for idx in range(len(msg) + control_bytes_amount):
        ...

    return ''.join(encoded)
