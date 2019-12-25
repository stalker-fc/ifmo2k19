import numpy as np
from .base import bin2array, array2bin

# https://shodhganga.inflibnet.ac.in/bitstream/10603/18696/10/10_chapter%203.pdf

H = np.array(
    [
        [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 1]
    ]
)

G = np.array(
    [
        [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1]
    ]
)

k = 4
n = 10
r = n - k  # 6


def encode(bits: str) -> str:
    bits = bin2array(bits)
    assert bits.shape == (k,)
    assert min(bits) >= 0 and max(bits) <= 1
    codeword = np.dot(G.T, bits) % 2
    return array2bin(codeword)


def decode(bits: str) -> str:
    bits = bin2array(bits)
    assert bits.shape == (n,)
    assert min(bits) >= 0 and max(bits) <= 1

    syndrome = np.dot(H, bits)
    if np.any(syndrome):
        bits = fix(bits)

    return array2bin(bits[-k:])


def fix(bits: np.ndarray) -> np.ndarray:
    for i in range(100):
        syndrome = np.dot(H, bits)
        if not np.any(syndrome):
            return bits
        error_idx = get_error_idx(bits)
        bits[error_idx] = (bits[error_idx] + 1) % 2
    return bits


def get_error_idx(bits: np.ndarray):
    failed_checks = np.zeros(bits.shape[0])
    for idx in range(r):
        mask = H[idx]
        parity = np.sum(bits) % 2
        if parity != 0:
            failed_checks[mask == 1] += 1
    return np.argmax(failed_checks)
