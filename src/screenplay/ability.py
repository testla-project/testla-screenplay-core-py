from abc import ABC
from interfaces import IActor
# import traceback; name: str = traceback.extract_stack()[-2][2]

class Ability(ABC):
    """Abilities enable tasks/actions to perform specific requirements."""
    
    def __init__(self) -> None:
        self.name = type(self).__name__

    @staticmethod
    def As(actor: IActor) -> "Ability":
        return actor.with_ability_to(Ability)
