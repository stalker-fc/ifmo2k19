from collections import Counter
from typing import Tuple, Dict


def compress(data: str) -> Tuple[str, Dict[str, str]]:
    counter = Counter(data)
    n = sum(counter.values())
    frequencies = {symbol: freq / n for symbol, freq in counter.items()}
    encoding_tree = make_encoding_tree(frequencies)
    compressed = ''.join([encoding_tree[c] for c in data])
    return compressed, encoding_tree


def make_encoding_tree(frequencies: Dict[str, float]) -> Dict[str, str]:
    if len(frequencies) == 2:
        return dict(zip(frequencies.keys(), ['0', '1']))

    sym1, sym2 = lowest_frequency_symbols(frequencies)

    tree = frequencies.copy()
    f1, f2 = tree.pop(sym1), tree.pop(sym2)
    node = ''.join((sym1, sym2))
    tree[node] = f1 + f2

    # Recurse and construct code on new distribution
    tree = make_encoding_tree(tree)

    node_encoding = tree.pop(node)
    tree[sym1], tree[sym2] = f'{node_encoding}0', f'{node_encoding}1'

    return tree


def lowest_frequency_symbols(frequencies: Dict[str, float]) -> Tuple[str, str]:
    (k1, v1), (k2, v2) = sorted(frequencies.items(), key=lambda x: x[1])[:2]
    return k1, k2
