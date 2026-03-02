def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


def first_word(text):
    parts = text.split()
    return parts[0] if parts else ""