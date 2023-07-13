from abc import ABC, abstractmethod
from testla_screenplay.interfaces import IActor

from src.testla_screenplay.using_alias import UsingAlias


class Task(ABC, UsingAlias):
    """An object representing a task that an IActor can perform."""

    @abstractmethod
    def perform_as(self, actor: IActor) -> object:
        """Makes the provided IActor perform this Action."""
        pass