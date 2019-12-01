import random
from labs import generate_message
from labs.base import message2bin
from labs import hamming_decode, hamming_encode, hamming_set_error


def test_set_error():
    init = ''.join((random.choice('01') for _ in range(10)))
    error = hamming_set_error(init)

    assert init != error
    assert len(init) == len(error)
    assert all((c in ('0', '1') for c in error))

    diff = sum([i != e for i, e in zip(init, error)])
    assert diff == 1


def test_hamming():
    init_message = generate_message()
    data = message2bin(init_message)
    correct_bytes_len = len(data) + len(data).bit_length()

    encoded = hamming_encode(init_message)
    assert len(encoded) == correct_bytes_len

    decoded = hamming_decode(encoded)
    assert init_message == decoded



def test_hamming_with_error():
    init_message = generate_message()
    data = message2bin(init_message)
    correct_bytes_len = len(data) + len(data).bit_length()

    encoded = hamming_encode(init_message)
    assert len(encoded) == correct_bytes_len

    encoded_with_error = hamming_set_error(encoded)

    decoded = hamming_decode(encoded_with_error)
    assert decoded == init_message
