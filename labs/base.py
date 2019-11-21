import math
import random
import string
from typing import List


def generate_message(message_len: int = 10) -> str:
    return ''.join((random.choice(string.ascii_letters) for _ in range(message_len)))


def message2bin(message: str) -> List[str]:
    codes = [ord(c) for c in message]
    letter_len = math.ceil(len(f'{max(codes):b}') / 8)
    if max(codes) > 255:
        raise ValueError('Incorrect symbols for encoding.')
    return [f'{c:b}'.zfill(letter_len) for c in codes]


def bin2message(codes: List[str]) -> str:
    return ''.join([chr(int(c, 2)) for c in codes])
