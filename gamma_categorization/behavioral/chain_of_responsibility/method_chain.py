"""
Method chain script
"""


class Creature:
    """
    Creature class
    """

    def __init__(self, name: str, attack: int, defense: int):
        self.name: str = name
        self.attack: int = attack
        self.defense: int = defense

    def __str__(self):
        return f"{self.name}: ({self.attack}/{self.defense})"


class CreatureModifier:
    """
    Creature modifier class.
    """

    def __init__(self, creature: Creature):
        self.creature: Creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier) -> None:
        """
        Add a modifier
        :param modifier: The modifier to add
        :type modifier: CreatureModifier
        :return: None
        :rtype: NoneType
        """
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        """
        Handle the creature modifier
        :return: None
        :rtype: NoneType
        """
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    """
    Double Attack Modifier class that inherits from Creature Modifier.
    """

    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    """
    Increase Defense Modifier class that inherits from Creature Modifier.
    """

    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.attack += 1
        super().handle()


if __name__ == '__main__':
    goblin: Creature = Creature("Goblin", 1, 1)
    print(goblin)
    root: CreatureModifier = CreatureModifier(goblin)
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.handle()
    print(goblin)
