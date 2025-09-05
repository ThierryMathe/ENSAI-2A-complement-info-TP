from src.business_object.pokemon.abstract_attack import AbstractAttack, AbstractPokemon


class FixedDamageAttack(AbstractAttack):
    def compute_damage(attacker: AbstractPokemon, defender: AbstractPokemon) -> int:
        return super().power
