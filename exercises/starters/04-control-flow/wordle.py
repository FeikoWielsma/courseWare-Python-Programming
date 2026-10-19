"""Explore the Wordle word list and the data structures around a guess."""

import string

words = ["hello", "crane", "react", "paper"]
guess = input("Your guess: ").strip().lower()
secret = "crane"

print(f"There are {len(words)} words. The first two are {words[:2]}.")
print(f"Crane is in the word list: {'crane' in words}.")
print(f"Example secret: {secret.upper()}.")
common = sorted(set(guess) & set(secret))
ruled_out_letters = sorted(set(guess) - set(secret))
not_tried = sorted(set(string.ascii_lowercase) - set(guess))
print(f"Letters in common: {common}")
print(f"Letters ruled out: {ruled_out_letters}")
print(f"Letters not tried: {not_tried}")

history = []
history.append("slate")
history.append(guess)
ruled_out = (guess, ruled_out_letters)
# Uncomment this line to see why tuple items cannot be reassigned.
# ruled_out[0] = "wrong"
print(f"History: {history}")
print(f"Guess and ruled-out letters: {ruled_out}")

stats = {"played": 0, "won": 0}
stats["played"] += 1
stats["won"] += int(guess == secret)
print(f"Stats: {stats}; streak: {stats.get('streak', 0)}")
