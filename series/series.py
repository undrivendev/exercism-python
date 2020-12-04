def slices(series, length):
    """Slices an input string in multiple sequences of n length.

    Raises:
        ValueError: if the 'series' argument is an empty list or 'length' argument is invalid.
    """
    if not len(series):
        raise ValueError("series argument cannot be null")
    if length <= 0 or length > len(series):
        raise ValueError("length value is invalid")
    return [series[i:i+length] for i in range(0, len(series) - length + 1)]
