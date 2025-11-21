import random

nouns = [
    "badger",
    "horse",
    "aardvark",
    "mouse",
    "gorilla",
    "elephant",
    "eagle",
    "sparrow",
]
verbs = [
    "hugs",
    "bounces",
    "meows",
    "hauls",
    "whispers",
    "flutters",
    "gallops",
    "shimmers",
]
adjectives = [
    "furry",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
    "melancholic",
    "serene",
]
prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverbs = [
    "curiously",
    "extravagantly",
    "graciously",
    "reluctantly",
    "meticulously",
    "vigorously",
]


def get_article(word: str):
    """get the article for the word"""
    if word.startswith(("a", "e", "i", "o", "u")):
        return "an"
    return "a"


def generate_poem():
    """generate a poem"""
    # Three nouns
    [noun1, noun2, noun3] = random.sample(nouns, 3)
    # Three verbs
    [verb1, verb2, verb3] = random.sample(verbs, 3)
    # Three adjectives
    [adj1, adj2, adj3] = random.sample(adjectives, 3)
    # Two prepositions
    [prep1, prep2] = random.sample(prepositions, 2)
    # One adverb
    [adverb1] = random.sample(adverbs, 1)

    return f"""
    {get_article(adj1)} {adj1} {noun1}
    {get_article(adj1)} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adverb1}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} the {adj3} {noun3}
    """


for _ in range(10):
    print(generate_poem())
