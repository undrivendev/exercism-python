def is_armstrong_number(number: int) -> bool:
    """Checks is the input number is an 'Armstrong number'."""
    str_num = str(number)
    return sum(int(i)**len(str_num) for i in str_num) == number
