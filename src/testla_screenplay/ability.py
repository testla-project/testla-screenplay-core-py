from abc import ABC
from testla_screenplay.interfaces import IActor


class Ability(ABC):
    """Abilities enable tasks/actions to perform specific requirements."""

    @classmethod
    def name(cls) -> str:
        """Get the name of the (sub)class, primarily for the ability mapping."""
        return cls.__name__

    @staticmethod
    def As(actor: IActor) -> "Ability":
        return actor.with_ability_to(Ability)
