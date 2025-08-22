from typing import List, Optional

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

def calculate_score(word: str, letter_multipliers: Optional[List[int]] = None) -> int:
    """Calculate score with double/triple letter bonuses"""
    if letter_multipliers is None:
        letter_multipliers = []
    
    total = 0
    for i, letter in enumerate(word):
        letter_score = get_letter_value(letter)
        
        # Apply letter multiplier if specified for this position
        if i < len(letter_multipliers):
            letter_score *= letter_multipliers[i]
            
        total += letter_score
    return total

def main() -> None:
    word = "PYTHON"
    # Double letter on P (position 0), triple letter on Y (position 2)
    multipliers = [2, 1, 3, 1, 1, 1]
    
    basic_score = calculate_score(word)
    bonus_score = calculate_score(word, multipliers)
    
    print(f"The word '{word}' scores {basic_score} points normally")
    print(f"With letter bonuses: {bonus_score} points")

if __name__ == "__main__":
    main()
