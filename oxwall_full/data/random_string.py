import random
import string


def random_string(minlen=1, maxlen=255, spaces=True, enter=False, cyrillic=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += " " * 8
    if enter:
        symbols += "\n" * 2
    if cyrillic:
        symbols += ''.join([chr(s) for s in range(0x0410, 0x044F) if chr(s).isprintable()])
    text = "".join(random.choices(symbols, k=length))
    return text


if __name__ == '__main__':
    print(random_string(maxlen=30, cyrillic=True))



