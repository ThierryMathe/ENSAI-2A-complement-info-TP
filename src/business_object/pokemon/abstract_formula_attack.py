from src.business_object.pokemon.abstract_attack import AbstractAttack, AbstractPokemon
from abc import abstractmethod
from random import random


class AbstractFomulaAttack(AbstractAttack):
    @abstractmethod
    def __get_attack_stat(self, APkm: AbstractPokemon) -> float:
        pass

    @abstractmethod
    def __get_defence_stat(self, APkm: AbstractPokemon) -> float:
        pass
      
    def compute_damage(self, attacker: AbstractPokemon, defender: AbstractPokemon) -> int:
        level = 2 / 5 * attacker.level + 2
        atta = self.power * self.__get_attack_stat(attacker)
        defe = self.__get_defence_stat(defender)*50
        rand = random() * 0.15 + 0.85
        return (level * atta / defe +2) * rand
