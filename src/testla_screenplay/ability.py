from abc import ABC
from .interfaces import IActor


class Ability(ABC):
    """Abilities enable tasks/actions to perform specific requirements."""

    @classmethod
    def name(cls) -> str:
        """Get the name of the (sub)class, primarily for the ability mapping."""
        return cls.__name__

    alias: str | None = None
    
    @staticmethod
    def As(actor: IActor, alias: str | None = None) -> "Ability":
        return actor.with_ability_to(Ability, alias)
    
    def with_alias(self, name: str) -> "Ability":
        self.alias = name
        return self
