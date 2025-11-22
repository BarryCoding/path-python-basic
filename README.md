# Python Basic Path

## RPG 

Write a text-based role-playing game (RPG) with the following characteristics:
- There’s one player and one monster
- The player starts with 100 health, the monster with 150 health (it’s big!)
- The player can choose to attack, heal, or run away.
- If the player attack, the player deal between 10- 15 damage to the monster.
- If the player heal, the player regain 30 health, up to a maximum of 100.
- If the player run away, the game ends.
- After the player’s turn, if the monster is still alive, it deals 15- 20 damage to the player.

The game continues until either the player or the monster’s health reaches 0, or
the player runs away.

Stretch Goals:
- Prevent the player from exiting the game by pressing Ctrl + C.
- Introduce double-damage critical hits that happen when an attack value is a factor of 3.
- Use emojis or string formatting syntax to make the game output more fun.

## Poetry Generator

In this challenge, you’ll write a program that generates poetry.  
Create five lists for different word types:  
Randomly select the following number of elements from each list:
- Three nouns
- Three verbs
- Three adjectives
- Two prepositions
- One adverb
Using the randomly selected words, generate and display a poem with the
following structure inspired by Clifford Pickover:

```py
{article} {adj1} {noun1}
{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} the {adj3} {noun3}

# example
A melancholic aardvark
A melancholic aardvark shimmers like the furry horse
extravagantly, the aardvark gallops
the horse meows over the incredulous gorilla
```

```py
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
```

## Space Race

Create a dictionary named captains by using this list of tuples:
```py
[
    ("Enterprise", "Picard"),
    ("Voyager", "Janeway"),
    ("Defiant", "Sisko"),
]
```

Then, add another spaceship named "Old Bessie" with captain "Leela" to captains.

Next, store a list of the spaceship names in a variable named spaceships.

Randomly pick three spaceships from spaceships and store them in a list named positions.

Create create dictionary named winners with the keys 1, 2, and 3. The default values should be "unknown" for each key.

Finally, loop over captains and congratulate the captain of the ship with the first ship and motivate the captain who didn’t make it to the top three.

```
Better luck next time, Picard.
Congratulations, Sisko!
```