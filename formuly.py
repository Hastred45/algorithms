# id 69627880

import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Player:
    """Класс для представления участника соревнования."""
    name: str
    solved: int
    penalty: int

    def __lt__(self, other):
        if not isinstance(other, Player):
            raise TypeError(
                f"Невозможно выполнить операцию сравнения между "
                f"{self.__class__.__name__} и {other.__class__.__name__}")
        return (-self.solved, self.penalty, self.name) < \
               (-other.solved, other.penalty, other.name)

    def __str__(self):
        return self.name


players = [
    Player('alla', 4, 100),
    Player('aleb', 4, 100),
    Player('gosha', 2, 90),
    Player('rita', 2, 90),
    Player('timofey', 4, 80),
]

print(players[0] < players[1])
