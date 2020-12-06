import re


def is_valid(isbn: str) -> bool:
    """Checks if the input isbn is valid."""
    if not re.search("^[0-9][-]*[0-9]{3}[-]*[0-9]{5}[-]*[0-9X]$", isbn):
        # input isbn is not syntactically valid
        return False

    index = 0
    total = 0
    for i in isbn.replace("-", ""):
        if (index < 9):
            total += int(i) * (10 - index)
        else:
            total += int(i) if i != "X" else 10  # check digit
        index += 1
    return not total % 11
