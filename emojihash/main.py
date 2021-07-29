from emojihash.typing import ContentType
from emojihash.hash_classes import EmojiHash1


def eh1(content: ContentType, length: int = 1, encode: str = 'utf-8') -> str:
    """
    Emoji Hash function (string)
    Function to get string emoji hash of content

    :param content: Hashtable data, might be bytes, string, integer, float.
    :param length: Length of result hash string
    :param encode: Optional parameter, specifying encoding of input string (if content is string)
    :return: Emoji hash as string
    """

    return EmojiHash1(content=content, length=length, encode=encode).__str__()

