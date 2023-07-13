from abc import ABC, abstractmethod
from testla_screenplay.interfaces import IActor

from src.testla_screenplay.using_alias import UsingAlias


class Question(ABC, UsingAlias):
    """Questions can be triggered by calling them from an actor object."""

    @abstractmethod
    def answered_by(self, actor: IActor) -> object:
        """Implementation of the query answer."""
        pass