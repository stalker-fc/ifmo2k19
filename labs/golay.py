import numpy as np
from typing import Dict, Tuple
from .base import bin2array, array2bin

n = 24
k = 12
d = 8
# (24, 12, 8)
# common length 24 bits
# amount of data bits: 12
# amount of check bits: 11

P = np.array([
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, ],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, ],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, ],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, ],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, ],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, ],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, ],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, ],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, ],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, ],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, ],
], dtype='int')

# generator mtx G, where transmitted codewords (24bits) are
# G.T dot msg or (msg dot G) (msg is 12 bit message)
# 2**12 = 4096 total codewords, one for each msg
G = np.concatenate((P, np.eye(12, dtype="int")), axis=1)

# pairity check matrix H satisfies G dot H.T = zeros (mod 2 arithmetic)
# also satisfies syn = H dot rec = H dot err (rec is recieved 24 bits,
# err is 24 bit error string added to transmitted 24 bit vec)
# (all mod 2 arithmetic)
H = np.concatenate((np.eye(12, dtype="int"), P.T), axis=1)


def encode(bits: str) -> str:
    """ takes any 12 bits, returns the golay 24bit codeword in nucleotide format
    bits is a list/array, 12 long, e.g.: [0,0,0,0,0,0,0,0,0,1,0,0]
    nt_to_bits is e.g.: {"A":"11", "C":"00", "T":"10", "G":"01"},None => default
    """
    bits = bin2array(bits)
    assert bits.shape == (12,)
    assert min(bits) == 0 and max(bits) == 1
    # cheap way to do binary xor in matrix dot
    codeword = np.dot(G.T, bits) % 2
    return array2bin(codeword)


def decode(data: str) -> Tuple[str, int]:
    """decodes a nucleotide string of 12 bases, using bitwise error checking
    inputs:
    - seq, a string of nucleotides
    - nt_to_bits, e.g.: { "A":"11",  "C":"00", "T":"10", "G":"01"}
    output:
    corrected_seq (str), num_bit_errors
    corrected_seq is None if 4 bit error detected"""
    bits = bin2array(data)
    corrected_bits, num_errors = decode_bits(bits)  # errors in # bits
    return array2bin(corrected_bits[-12:]), num_errors


def generate_syndromes() -> Dict[Tuple[int], np.ndarray]:
    errors = _make_3bit_errors()
    # len = 2325.  (1 (all zeros) + 24 (one 1) + 276 (two 1s) + 2024)

    # syndrome lookup table is the key to (fast, syndrome) decoding
    # decode() uses syndrome lookup table

    syndromes = {}
    # key: syndrome (12 bits).  Val: 24 bit err for that syn
    # we include the all zeros error (key = all zeros syndrome)
    # build syndrome lookup table
    for errvec in errors:
        syn = tuple(np.dot(H, errvec) % 2)
        syndromes[syn] = np.array(errvec)

    return syndromes


def decode_bits(bits: np.ndarray) -> Tuple[np.ndarray, int]:
    """ decode a recieved 24 bit vector to a corrected 24 bit vector
    uses golay defaults
    input: received bitvec is 24 bits long, listlike
    output: corrected_vec, num_bit_errors
    corrected_vec is None iff num_errors = 4"""

    syndromes = generate_syndromes()
    syn = np.dot(H, bits) % 2
    try:
        err = syndromes[tuple(syn)]
    except KeyError:
        raise ValueError('Can`t decode. There are more than 3 errors in message.')
    corrected = (bits + err) % 2  # best guess for transmitted bitvector

    return corrected, int(np.sum(err))


def _make_3bit_errors(veclen=24):
    """ return list of all bitvectors with <= 3 bits as 1's, rest 0's
    returns list of lists, each 24 bits long by default.
    not included:
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
    included:
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    """
    errorvecs = []
    # all zeros
    errorvecs.append([0] * veclen)
    # one 1
    for i in range(veclen):
        vec = [0] * veclen
        vec[i] = 1
        errorvecs.append(vec)

    # two 1s
    for i in range(veclen):
        for j in range(i + 1, veclen):
            vec = [0] * veclen
            vec[i] = 1
            vec[j] = 1
            errorvecs.append(vec)

    # three 1s
    for i in range(veclen):
        for j in range(i + 1, veclen):
            for k in range(j + 1, veclen):
                vec = [0] * veclen
                vec[i] = 1
                vec[j] = 1
                vec[k] = 1
                errorvecs.append(vec)
    return errorvecs
