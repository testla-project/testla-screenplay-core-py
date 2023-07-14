# no interfaces in Python! -> no need for IAbility, IAction, IQuestion, ITask?

from abc import ABC, abstractmethod


class IActor(ABC):
    # collection of attributes assigned to the actor
    attributes: dict 

    # set attribute
    @abstractmethod
    def With(self, key: str, value: object) -> "IActor":
        pass

    # get attribute
    @abstractmethod
    def states(self, key: str) -> object:
        pass

    # connection to questions
    @abstractmethod
    def asks(self, *questions) -> object:
        pass

    # connection to abilities
    @abstractmethod
    def with_ability_to(self, ability, alias: str | None = None):
        pass

    @abstractmethod
    def can(self, ability) -> "IActor":
        pass

    # connection to tasks/actions
    @abstractmethod
    def attempts_to(self, *activities) -> object:
        pass
