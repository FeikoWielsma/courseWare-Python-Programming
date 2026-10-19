"""Wordle, as it stands at the end of Exercise 4."""


words = [
    "hello", "crane", "react", "paper", "slate", "error", "house", "ghost",
    "world", "money", "speed", "geese", "trace", "grace", "raise", "trick",
]
secret = "crane"
max_guesses = 6
used_letters: set[str] = set()

print("Guess the five-letter word. Type 'quit' to give up, 'letters' for the letters tried.")

guess_count = 0
while guess_count < max_guesses:
    guess = input(f"Guess {guess_count + 1}/{max_guesses} : ").strip().lower()

    match guess:
        case "quit":
            print(f"The word was {secret.upper()}.")
            break
        case "letters":
            print("Tried :", " ".join(sorted(used_letters)))
            continue

    if len(guess) != 5 or guess not in words:
        print("That is not a five-letter word I know.")
        continue

    guess_count += 1
    used_letters.update(guess)

    # [A] is in the right place, (A) is in the word elsewhere, A is not in it.
    row = ""
    for position, letter in enumerate(guess):
        if letter == secret[position]:
            row += f"[{letter.upper()}]"
        elif letter in secret:
            row += f"({letter.upper()})"
        else:
            row += f" {letter.upper()} "
    print(row)

    if guess == secret:
        print(f"Got it in {guess_count}!")
        break
else:
    print(f"Out of guesses. The word was {secret.upper()}.")
