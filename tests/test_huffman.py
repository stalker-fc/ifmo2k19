from labs import huffman_compress


def test_compress_01():
    message = 'aaaaa'
    data, tree = huffman_compress(message)

    assert data == '00000'
    assert tree == {'a': '0'}


def test_compress_02():
    message = 'abab'
    data, tree = huffman_compress(message)

    assert data == '0101'
    assert tree == {'a': '0', 'b': '1'}


def test_compress_03():
    message = 'aabc'
    data, tree = huffman_compress(message)

    assert data == '001011'
    assert tree == {'a': '0', 'b': '10', 'c': '11'}
