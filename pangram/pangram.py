def is_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram.

    Args:
        sentence: the sentence to check
    
    Returns: 
        True if the sentence passed as input is a pangram,
        otherwise False.

    """
    valid_characters = "abcdefghijklmnopqrstuvwxyz"
    unique_list = set()
    for char in sentence.lower():
        if char in valid_characters:
            unique_list.add(char)
            if len(unique_list) == len(valid_characters):
                return True
    return False
