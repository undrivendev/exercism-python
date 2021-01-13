def distance(strand_a, strand_b) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Cannot process two strands of different lengths.")

    return len([i for i in range(0, len(strand_a)) if strand_a[i] != strand_b[i]])
