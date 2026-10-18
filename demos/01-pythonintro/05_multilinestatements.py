intro = 30
orbit = 222
echo = 185

total = (
    intro + orbit + echo
)
print(total)  # 437

playlist = [
    "Intro", "Orbit", "Echo",
]
print(playlist)

# A backslash also continues a line; parentheses are easier to maintain.
same_total = intro + \
    orbit + echo
print(same_total)
