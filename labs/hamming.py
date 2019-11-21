"""Hamming code"""

import math

from typing import List
from .base import message2bin



def encode(message: str) -> List['str']:
    words_to_encode = 4
    bin_view = message2bin(message)


def set_control_bytes(msg: str) -> str:
    new = msg
    amount = len(msg).bit_length()
    indices = [1 << i for i in range(amount)]
    res = []
    for idx in range(len(msg) + amount):
        ...




def decode(message: List[str], word_len: int) -> str:
    added_bytes = len(message[0]) % 8




