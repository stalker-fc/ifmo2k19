from .base import generate_message, generate_binary_data

from .hamming import encode as hamming_encode
from .hamming import decode as hamming_decode
from .hamming import set_error as hamming_set_error


from .huffman import compress as huffman_compress
from .huffman import compress as huffman_decompress


from .golay import encode as golay_encode
from .golay import decode as golay_decode

from .ldpc import encode as ldpc_encode
from .ldpc import decode as ldpc_decode
