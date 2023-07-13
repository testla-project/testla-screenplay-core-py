from abc import ABC, abstractmethod
from .interfaces import IActor
from .using_alias import UsingAlias


class Question(ABC, UsingAlias):
    """Questions can be triggered by calling them from an actor object."""

    @abstractmethod
    def answered_by(self, actor: IActor) -> object:
        """Implementation of the query answer."""
        pass