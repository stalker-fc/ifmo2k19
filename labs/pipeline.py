"""Base pipeline for all coding algorithms"""
import random
import string




def pipeline(encode_function, decode_function, messages_amount: int):
    for _ in range(messages_amount):
        message = generate_message(10)
        print(message)
        encoded = encode_function(message)
        print(encoded)
        noised = ...
        print(noised)
        decoded = decode_function(encoded)
        print(decoded)
        assert message == decoded


def generate_message(message_len: int) -> str:
    return ''.join((random.choice(string.ascii_letters) for _ in range(message_len)))

def add_noise(message: bytes) -> bytes:
    pass


def sample_encode(message: str) -> bytes:
    return message.encode()


def sample_decode(message: bytes) -> str:
    return message.decode()


if __name__ == '__main__':
    pipeline(sample_encode, sample_decode, 1)
