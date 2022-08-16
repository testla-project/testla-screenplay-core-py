from abc import ABC, abstractmethod
from testla_screenplay.interfaces import IActor


class Question(ABC):
    """Questions can be triggered by calling them from an actor object."""

    @abstractmethod
    def answered_by(self, actor: IActor) -> object:
        """Implementation of the query answer."""
        pass