"""Compare one guess with a known word using strings and f-strings."""

secret = "crane"
guess = input("Your guess: ").strip().lower()

print(f"{' WORDLE ':*^28}")
print(f"Secret: {secret.upper()}    Guess: {guess.upper()}")
print(f"{'Position':^10}{'Same place':^14}{'In secret':^12}")
print(f"{0:^10}{guess[0] == secret[0]!s:^14}{guess[0] in secret!s:^12}")
print(f"{1:^10}{guess[1] == secret[1]!s:^14}{guess[1] in secret!s:^12}")
print(f"{2:^10}{guess[2] == secret[2]!s:^14}{guess[2] in secret!s:^12}")
print(f"{3:^10}{guess[3] == secret[3]!s:^14}{guess[3] in secret!s:^12}")
print(f"{4:^10}{guess[4] == secret[4]!s:^14}{guess[4] in secret!s:^12}")
print(f"Five letters: {len(guess) == 5}")
print(f"First two: {guess[:2]}, last two: {guess[-2:]}")
print(f"The secret contains {secret.count('e')} letter e characters.")
print("Position\tSame place\tIn secret")
print(r"The escape sequence \t inserts a tab.")
