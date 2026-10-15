"""Lecture 9 notes"""
phrase: str = "Let me do this"

for word in map(str.upper, phrase.split()):
    print(word)

strings = ["October", "November", "December"]

def shorten(s: str) -> str:
    """Shortens strings"""
    return s[0:3]

print(list(map(shorten, strings)))
print(list(map(lambda s: s[0:3], strings)))

def is_long(s: str) -> bool:
    return len(s) >= 4

filtered_list: list[str] = list(filter(is_long, phrase.split()))
