def convert(number: int) -> str:
    return (f"{'Pling' if (not number % 3) else ''}"
            f"{'Plang' if (not number % 5) else ''}"
            f"{'Plong' if (not number % 7) else ''}"
            ) or str(number)
