from emojihash import eh1

print(
    eh1("Hello world!")
) # π₯³

print(
    eh1(42)
) # π³

print(
    eh1("I need more emojis!!", length=12)
) # π§ππͺ π π₯ π©ππ¦πΌππ πΆ

print(
    eh1("I need more emojis!!", length=2) # "π§ππͺ π π₯ π©ππ¦πΌππ πΆ"
)

print(
    eh1(b'000', length=2) # "π¦πΌ"
)

print(
    eh1(u'5p34k 1337', length=4, encode='ascii') # "π©Ήπ "
)
