from labs import golay_encode, golay_decode
from labs.base import generate_binary_data, set_error


def test_golay():
    data = generate_binary_data(12)

    encoded = golay_encode(data)
    assert len(encoded) == 24

    decoded, _ = golay_decode(encoded)
    assert data == decoded


def test_set_error():
    init = generate_binary_data(12)

    for diff in range(1, 4):
        error = set_error(init, diff)
        assert init != error
        assert len(init) == len(error)
        assert all((c in ('0', '1') for c in error))

        counter = sum([i != e for i, e in zip(init, error)])
        assert diff == counter


def test_golay_with_error():
    data = generate_binary_data(12)

    for diff in range(1, 4):
        encoded = golay_encode(data)
        assert len(encoded) == 24
        error = set_error(encoded, diff)
        decoded, counter = golay_decode(error)
        assert diff == counter
        assert data == decoded
