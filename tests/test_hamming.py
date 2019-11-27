from labs import hamming_decode, hamming_encode, hamming_set_error


def test_set_error():
    init = '11100111'
    error = hamming_set_error(init)

    assert init != error
    assert len(init) == len(error)
    assert all((c in ('0', '1') for c in error))

    diff = sum([i != e for i, e in zip(init, error)])
    assert diff == 1


def test_encode():
    ...


def test_decode():
    ...


