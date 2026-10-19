"""Compare one guess with a known word using strings and f-strings."""

secret = "crane"
guess = input("Your guess: ")
guess = guess.strip().lower()

print("WORDLE")
print(f"Secret: {secret.upper()}    Guess: {guess.upper()}")
print("Position / Same place / In secret")
print(f"0 / {guess[0] == secret[0]} / {guess[0] in secret}")
print(f"1 / {guess[1] == secret[1]} / {guess[1] in secret}")
print(f"2 / {guess[2] == secret[2]} / {guess[2] in secret}")
print(f"3 / {guess[3] == secret[3]} / {guess[3] in secret}")
print(f"4 / {guess[4] == secret[4]} / {guess[4] in secret}")
print(f"Five letters: {len(guess) == 5}")
print(f"First two: {guess[:2]}, last two: {guess[-2:]}")
print(f"The secret contains {secret.count('e')} letter e characters.")
print("First line\nSecond line")
print(r"The escape sequence \t inserts a tab.")
