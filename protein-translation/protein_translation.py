from typing import List


def get_protein_name(codon: str) -> str:
    """Translates the DNA codon sequence to its respective Amino Acid name."""
    if codon == "AUG":
        return "Methionine"
    elif codon == "UUU" or codon == "UUC":
        return "Phenylalanine"
    elif codon == "UUA" or codon == "UUG":
        return "Leucine"
    elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
        return "Serine"
    elif codon == "UAU" or codon == "UAC":
        return "Tyrosine"
    elif codon == "UGU" or codon == "UGC":
        return "Cysteine"
    elif codon == "UGG":
        return "Tryptophan"
    else:
        raise ValueError(f"The sequence value is not recognized: {codon}.")


def proteins(strand: str) -> List[str]:
    """Translates the input DNA strand to its respective Amino Acids.
    
    Args:
        strand: the DNA strand to translate
    
    Returns:  
        A list containing the respective Amino Acids.

    Raises:
        ValueError: when a strand not divisible by 3 (codon length) is passed as input
    """
    if len(strand) % 3:
        raise ValueError("The input strand argument has an invalid length.")

    result: List[str] = []
    for i in range(0, len(strand) - 2, 3):
        current_sequence = strand[i:i+3]
        if current_sequence == "UAA" or current_sequence == "UAG" or current_sequence == "UGA":
            break
        result.append(get_protein_name(current_sequence))
    return result
