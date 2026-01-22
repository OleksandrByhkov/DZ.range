import string

def range(s: str) -> str:
    low, high = s.split("-")
    letters = string.ascii_letters
    i1, i2 = letters.index(low), letters.index(high)
    return letters[i1:i2+1]

