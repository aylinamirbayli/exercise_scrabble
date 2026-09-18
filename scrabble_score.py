LETTER_SCORES = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
    "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
    "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

def calculate_score(word, letter_multipliers=None, word_multiplier=1):
    word = word.upper()
    if letter_multipliers is None:
        letter_multipliers = [1] * len(word)
    
    total = sum(
        LETTER_SCORES.get(letter, 0) * mult
        for letter, mult in zip(word, letter_multipliers)
    )
    return total * word_multiplier

def main():
    word = "PYTHON"
    print(f"The word '{word}' scores {calculate_score(word)} points normally")
    print(f"With letter bonuses: {calculate_score(word, [2, 1, 3, 1, 1, 1])} points")
    print(f"On double word score: {calculate_score(word, word_multiplier=2)} points")
    print(f"Letter bonuses on a triple word: {calculate_score(word, [2, 1, 3, 1, 1, 1], word_multiplier=3)} points")

if __name__ == "__main__":
    main()
