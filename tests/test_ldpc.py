from labs import ldpc_encode, ldpc_decode
from labs.base import generate_binary_data, set_error


def test_ldpc():
    data = generate_binary_data(4)

    encoded = ldpc_encode(data)
    assert len(encoded) == 10

    decoded = ldpc_decode(encoded)
    assert data == decoded



def test_ldpc_with_error():
    data = generate_binary_data(4)

    encoded = ldpc_encode(data)
    assert len(encoded) == 10

    error = set_error(encoded)
    decoded = ldpc_decode(error)
    assert data == decoded
