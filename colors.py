import random

color_names = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "lime",
    "olive",
    "teal",
    "navy",
    "gold",
    "violet",
    "maroon",
    "coral",
    "indigo",
    "silver",
    "orchid",
    "turquoise"
]


def rand_color():
    return random.choice(color_names)