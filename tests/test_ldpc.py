import numpy as np
from typing import List
from labs import ldpc_encode, ldpc_decode
from labs.base import generate_binary_data, set_error, array2bin


def get_all_codewords() -> List[str]:
    codes = np.arange(0, 16)
    return [np.binary_repr(code, width=4) for code in codes]


def test_ldpc():
    for data in get_all_codewords():
        encoded = ldpc_encode(data)
        assert len(encoded) == 10

        decoded = ldpc_decode(encoded)
        assert data == decoded


def test_ldpc_with_error():
    for data in get_all_codewords():
        encoded = ldpc_encode(data)
        assert len(encoded) == 10

        error = set_error(encoded)
        decoded = ldpc_decode(error)
        assert data == decoded
