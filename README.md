# EmojiHash ๐

Library with hashing tools where hash is emoji(s). Zero dependencies.

## Installation
```shell
pip install emojihash
```

## Simple example

```python
from emojihash import eh1

my_string = "Hello world!"

emoji_hash = eh1(my_string) # eh == Emoji Hash

print(emoji_hash) # ๐ฅณ
```

## More examples
```python
from emojihash import eh1

print(
    eh1("Hello world!") # "๐ฅณ"
)

print(
    eh1(42) # "๐ณ"
)

print(
    eh1("I need more emojis!!!", length=12) # "๐ค๐ง๐ฎ๐๐๐นโฉ๐๐๐๐๐"
)

print(
    eh1("I need more emojis!!!", length=2) # "๐ฆ๐ผ"
)

print(
    eh1(b'000', length=2) # "๐ฉน๐ "
)

print(
    eh1(u'5p34k 1337', length=4, encode='ascii') # "๐๐ฃ๐ฉ๐ฏ"
)
```