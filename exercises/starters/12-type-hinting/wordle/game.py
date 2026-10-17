"""Run one Wordle game."""

from contextlib import closing

from wordle.display import render
from wordle.scoring import InvalidGuess, check_guess, score_guess
from wordle.solver import best_guess, candidates
from wordle.stats import connect, summary
from wordle.words import load_allowed


class Game:
    """Keep one game's state and report values derived from its history."""

    def __init__(self, secret: str, words: list[str], max_guesses: int = 6) -> None:
        """Create an empty game with a validated guess limit."""
        self.secret = secret
        self.words = words
        self.history: list[tuple[str, list[str]]] = []
        self.max_guesses = max_guesses

    @property
    def max_guesses(self) -> int:
        """Return the configured guess limit."""
        return self._max_guesses

    @max_guesses.setter
    def max_guesses(self, value: int) -> None:
        """Keep the guess limit between one and ten."""
        if not 1 <= value <= 10:
            raise ValueError("max_guesses must be between 1 and 10")
        self._max_guesses = value

    @property
    def is_won(self) -> bool:
        """Return whether the latest guess found the secret."""
        return bool(self.history and self.history[-1][0] == self.secret)

    @property
    def is_over(self) -> bool:
        """Return whether the game was won or has no guesses left."""
        return self.is_won or self.guesses_left <= 0

    @property
    def guesses_left(self) -> int:
        """Return how many guesses remain."""
        return self.max_guesses - len(self.history)

    def guess(self, word: str) -> list[str]:
        """Validate, score and record one guess, then return its marks."""
        if self.is_over:
            raise ValueError("The game is over.")
        check_guess(word, self.words)
        marks = score_guess(self.secret, word)
        self.history.append((word, marks))
        return marks

    def __str__(self) -> str:
        """Draw every scored guess on its own row."""
        return "\n".join(render(word, marks) for word, marks in self.history)


def play(secret: str, words: list[str], max_guesses: int = 6) -> tuple[int, bool]:
    """Play one game and return the guesses used and whether the secret was found."""
    allowed_words = load_allowed()
    game = Game(secret, allowed_words, max_guesses)
    used_letters = set()
    while not game.is_over:
        guess = input(f"Guess {len(game.history) + 1}/{game.max_guesses} : ").strip().lower()
        match guess:
            case "quit":
                break
            case "letters":
                print("Tried :", " ".join(sorted(used_letters)))
                continue
            case "hint":
                possible = candidates(words, game.history)
                print(f"{len(possible)} words left, try {best_guess(possible).upper()}")
                continue
            case "stats":
                print_stats()
                continue
        try:
            check_guess(guess, allowed_words)
            marks = game.guess(guess)
        except InvalidGuess as error:
            print(error)
            continue
        used_letters.update(guess)
        print(render(guess, marks))
    if game.is_won:
        print(f"Got it in {len(game.history)}!")
    else:
        print(f"The word was {secret.upper()}.")
    return len(game.history), game.is_won


def print_stats() -> None:
    """Print database totals, a guess chart and the current winning streak."""
    with closing(connect()) as connection:
        totals = summary(connection)
    print(
        f"Games played: {totals['played']}; won: {totals['won']}; "
        f"win rate: {totals['win_percentage']:.1f}%."
    )
    chart = " ".join(
        f"{guesses}: {'#' * count}"
        for guesses, count in totals["distribution"].items()
    )
    print(f"Wins by guesses: {chart or 'none'}")
    print(f"Current streak: {totals['streak']}")
