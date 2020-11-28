def leap_year(year: int) -> bool:
    """Checks if the year passed as input is a leap year.
    
    Args:
        year: the year to check

    Returns:
        bool: return True if the input year is a leap year, otherwise False

    """
    return not year % 4 and (year < 100 or (bool(year % 100) or (not year % 100 and not year % 400)))
