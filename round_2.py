from typing import Counter


tests = [
    ('civic', True),
    ('ivicc', True),
    ('hello', False),
    ('aabbccdd', True),
    ('iiiillll', True),
    ('iixiillll', True),
    ('iiillll', True),  # wrong case in non-improved version
]


def main(word: str) -> bool:
    even = len(word) % 2 == 0
    unique_count = 0
    for letter in word:
        letter_count = len(list(filter(lambda l2: l2 == letter, word)))
        if letter_count % 2 != 0:
            if even or not even and unique_count > 0:
                return False
            unique_count += 1
    return True


def improved(word: str) -> bool:
    """
    Improvement because:

    Avoid full scanning the string for each letter.
    Logical improvement: We can simplify the problem by just saying "unique letters shouldn't be more than 1",
    regardless if letter count is even or odd, since if you have an even word, it's impossible to have just one unique
    letter, they'll be 0 or >= 2.
    """
    counts = Counter(word)
    odd_counts = sum(1 for c in counts.values() if c % 2 != 0)
    return odd_counts <= 1


if __name__ == '__main__':
    for input, output in tests:
        result = main(input)
        assert result == output
        improved_result = improved(input)
        print(input, output, improved_result)
        assert improved_result == output
