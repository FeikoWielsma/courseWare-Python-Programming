"""Restricting values to a closed set with typing.Literal.

The file runs without complaint under Python :

    uv run python demos/12-appendix-type-hinting/06_literal.py

A value outside the set is flagged when checked with mypy :

    uv run mypy demos/12-appendix-type-hinting/06_literal.py
"""

from typing import Literal

type TrafficLight = Literal["red", "amber", "green"]


def change_light(color: TrafficLight) -> None:
    """Change the traffic light to a new color."""
    print(f"Traffic light is now {color}")


change_light("green")
change_light("blue")
