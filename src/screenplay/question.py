from abc import ABC, abstractmethod
from typing import Any
from interfaces import IActor


class Question(ABC):
    """Questions can be triggered by calling them from an actor object."""

    @abstractmethod
    def answered_by(self, actor: IActor) -> Any:
        """Implementation of the query answer."""
        pass