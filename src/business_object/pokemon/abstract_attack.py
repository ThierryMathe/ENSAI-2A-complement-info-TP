from abc import ABC, abstractmethod
from src.business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(attacker: AbstractPokemon, defender: AbstractPokemon) -> int:
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
