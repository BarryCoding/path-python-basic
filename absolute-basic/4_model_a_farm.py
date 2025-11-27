class FarmLocation:
    location_type: str = ""

    def __init__(self, space_available: int):
        self.space_available = space_available
        self.animals: list[Animal] = []

    def __str__(self) -> str:
        return f"The {self.__class__.location_type} has {self.space_available} space filled with {len(self.animals)} animals."

    @property
    def is_full(self) -> bool:
        return len(self.animals) >= self.space_available


class Field(FarmLocation):
    location_type = "field"

    def __init__(self, space_available: int):
        super().__init__(space_available)


class Barn(FarmLocation):
    location_type = "barn"

    def __init__(self, space_available: int):
        super().__init__(space_available)


class Animal:
    animal_type: str = ""

    def __init__(self, name: str, color: str, trait: str):
        self.name = name
        self.color = color
        self.trait = trait
        self._stuff_in_stomach = 0  # private attribute
        self._location = None

    def __str__(self) -> str:
        return f"The {self.trait} {self.color} {self.__class__.animal_type} is '{self.name}'."

    def eat(self) -> str:
        if self.is_hungry:
            self._stuff_in_stomach = 1
            return f"The {self.name} is eating."
        else:
            return self.poop()

    def poop(self) -> str:
        self._stuff_in_stomach -= 1
        return f"The {self.name} poops, then looks relieved."

    @property  # getter
    def is_hungry(self) -> bool:
        return self._stuff_in_stomach < 2

    def move(self, location: FarmLocation):
        if self._location and self._location is location:
            return f"The {self.name} is already in the {location.location_type}"

        if location.is_full:
            return f"The {self.name} cannot move to the {location.location_type} because it is full"

        if self._location is not None:
            self._location.animals.remove(self)

        location.animals.append(self)
        self._location = location
        return f"The {self.name} has moved to the {location.location_type}"

    def talk(self, sound: str = "Zzz"):
        return f"The {self.name} says '{sound}'."


class Dog(Animal):

    animal_type = "dog"

    def talk(self, sound: str = "Bark"):
        return super().talk(sound)


class Pig(Animal):

    animal_type = "pig"

    def talk(self, sound: str = "Oink"):
        return super().talk(sound)


class Sheep(Animal):

    animal_type = "sheep"

    def talk(self, sound: str = "Baa"):
        return super().talk(sound)


field = Field(1)
print(field)
dog = Dog("Rex", "brown", "dog")
pig = Pig("Piggy", "pink", "pig")
print(dog.move(field))
print(field)
print(dog.move(field))
print(pig.move(field))
print(field)
