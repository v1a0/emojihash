# EmojiHash 😄

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

print(emoji_hash) # 🥳
```

## More examples
```python
from emojihash import eh1

print(
    eh1("Hello world!") # "🥳"
)

print(
    eh1(42) # "🚳"
)

print(
    eh1("I need more emojis!!!", length=12) # "🍤🍧🚮🛄👑🛹⛩💙🙇🎊🍍👚"
)

print(
    eh1("I need more emojis!!!", length=2) # "🦈🏼"
)

print(
    eh1(b'000', length=2) # "🩹🟠"
)

print(
    eh1(u'5p34k 1337', length=4, encode='ascii') # "🍓👣🔩💯"
)
```