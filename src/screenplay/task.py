from abc import ABC, abstractmethod
from typing import Any
from interfaces import IActor


class Task(ABC):
    """An object representing a task that an IActor can perform."""

    @abstractmethod
    def perform_as(self, actor: IActor) -> Any:
        """Makes the provided IActor perform this Action."""
        pass