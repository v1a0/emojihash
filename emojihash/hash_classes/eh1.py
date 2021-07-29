from hashlib import sha512
from emojihash.db import ONE_LEN_EMOJIS
from emojihash.typing import ContentType


class EmojiHash1:
    """
    Emoji Hash 1
    release 07/29/2021

    Hash function based on sha512. Calculating "base_hash" of input content and depends on it selects emojis.
    Tuple of emojis db.basic_emojis.ONE_LEN_EMOJIS
    ID of each emoji calculating like (value**self.length) % len(ONE_LEN_EMOJIS)

    Collection of emojis for this hash-function contains only one length* emojis, like: 🔥, 👱, 😈.
    """

    def __init__(self, content: ContentType, length: int = 1, encode: str = 'utf-8'):
        self.base_hash = self.hash(content=content, encode=encode)
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        tuple_hash = (self.emoji_by_id(self.base_hash),)

        new_hash = self.base_hash

        for _ in range(self.length - 1):
            new_hash = self.hash(new_hash)
            tuple_hash = tuple_hash + (self.emoji_by_id(new_hash),)

        return ''.join(emoji for emoji in tuple_hash)

    def emoji_by_id(self, value: int) -> str:
        return ONE_LEN_EMOJIS[pow(value, self.length, mod=len(ONE_LEN_EMOJIS))]

    @staticmethod
    def hash(content: ContentType, encode: str = 'utf-8') -> int:
        if isinstance(content, bytes):
            _hash = sha512(content)
        elif isinstance(content, str):
            _hash = sha512(content.encode(encode))
        elif isinstance(content, (int, float)):
            try:
                _hash = sha512(bytes(content))
            except OverflowError:
                _hash = sha512(str(content).encode(encode, errors='replace'))
        elif isinstance(content, bool):
            _hash = sha512(bytes(int(content)))
        else:
            raise TypeError("Unexpected type")

        return int(_hash.hexdigest(), 16)