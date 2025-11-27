import random

data = [
    ("Enterprise", "Picard"),
    ("Voyager", "Janeway"),
    ("Defiant", "Sisko"),
]

# Create a dictionary named captains by using this list of tuples:
captains = dict(data)

# Then, add another spaceship named "Old Bessie" with captain "Leela" to captains.
captains["Old Bessie"] = "Leela"

# Next, store a list of the spaceship names in a variable named spaceships.
spaceships = list(captains.keys())

# Randomly pick three spaceships from spaceships and store them in a list named positions.
positions = random.sample(spaceships, 3)

# Create create dictionary named winners with the keys 1, 2, and 3. The default values should be "unknown" for each key.
winners = {position: "unknown" for position in range(1, 4)}

# Finally, loop over captains and congratulate the captain of the ship with the first ship and motivate the captain who didn’t make it to the top three.
for ship, captain in captains.items():
    if ship in positions:
        winners[positions.index(ship) + 1] = captain
    else:
        print(f"Better luck next time, {captain}.")

print(f"Congratulations, {winners[1]}!")
