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
    def asks(self, question, activityResult: object) -> object:
        pass

    # connection to abilities
    @abstractmethod
    def with_ability_to(self, ability):
        pass

    @abstractmethod
    def can(self, ability) -> "IActor":
        pass

    # connection to tasks/actions
    @abstractmethod
    def attempts_to(self, *activities) -> object:
        pass


# class IAbility(ABC):
#     """This is an empty interface, since every ability has its own call patterns and therefore there is no common ground.
#     Only the name attribute needs to be set for internal reference.
#     """
#     name: str


# class IAction(ABC):
#     """An object representing an action that an IActor can perform."""

#     @abstractmethod
#     def perform_as(self, actor: IActor) -> object:
#         """Makes the provided IActor perform this Action."""
#         pass


# class ITask(ABC):
#     """An object representing a task that an IActor can perform."""

#     @abstractmethod
#     def perform_as(self, actor: IActor) -> object:
#         """Makes the provided IActor perform this Action."""
#         pass


# class IQuestion(ABC):

#     @abstractmethod
#     def answered_by(self, actor: IActor) -> object:
#         """Implementation of the query answer."""
#         pass