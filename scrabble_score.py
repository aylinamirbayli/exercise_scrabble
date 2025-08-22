def get_letter_value(letter: str) -> int:
    """Get the point value for a letter"""
    values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    return values.get(letter.upper(), 0)

def calculate_score(word: str, word_multiplier: int = 1) -> int:
    """Calculate score with double/triple word bonuses"""
    total = 0
    for letter in word:
        total += get_letter_value(letter)
    
    # Apply word multiplier to final total
    return total * word_multiplier

def main() -> None:
    word = "PYTHON"
    
    basic_score = calculate_score(word)
    double_word_score = calculate_score(word, 2)
    triple_word_score = calculate_score(word, 3)
    
    print(f"The word '{word}' scores {basic_score} points normally")
    print(f"On double word score: {double_word_score} points")
    print(f"On triple word score: {triple_word_score} points")

if __name__ == "__main__":
    main()
