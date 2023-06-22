from typing import Type
from testla_screenplay.interfaces import IActor
from testla_screenplay.ability import Ability
from testla_screenplay.action import Action
from testla_screenplay.task import Task
from testla_screenplay.question import Question


class Actor(IActor):
    """Actors use abilities in order to execute tasks/actions and answer questions."""

    def __init__(self, name: str) -> None:
        super().__init__()
        self.attributes = {} # collection of attributes assigned to the actor
        self.__ability_map = {} # map of abilities of this Actor; maps types 
        self.name = name # name of this actor

    def With(self, key: str, value: object) -> IActor:
        """Store an attribute in the actors attribute collection.

        :param key: attribute name
        :param value: attribute value
        :returns: this Actor
        """
        self.attributes[key] = value
        return self

    def states(self, key: str) -> object:
        """Get an attribute from the actors attribute collection.

        :param key: the key for the attribute
        :returns: the value for the requested attribute if the key exists, otherwise None
        """
        return self.attributes.get(key)

    @staticmethod
    def named(name: str) -> "Actor":
        """Create a new Actor with a given name."""
        return Actor(name)

    def with_credentials(self, username: str, password: str) -> "Actor":
        """Sets a username and a password for the actor.
        
        :param username: the username
        :param password: the password
        :returns: the actor
        """
        self.attributes["username"] = username
        self.attributes["password"] = password
        return self

    def can(self, *abilities: Ability) -> "Actor":
        """Assign one or more abilities to the actor
        
        :param abilites: the abilities the actor will be able to use.
        """
        for ability in abilities:
            self.__ability_map[ability.name()] = ability
        return self

    def attempts_to(self, *activities: Action | Task) -> object:
        """Executes the given Tasks/Actions."""
        for activity in activities:
            result = activity.perform_as(self)
        return result

    def with_ability_to(self, ability: Type[Ability]) -> Type[Ability]:
        """Verify if the actor has the given ability."""
        if ability.name() not in self.__ability_map:
            raise RuntimeError("Error: This Actor does not have this ability: " + ability.name())
        else:
            return self.__ability_map[ability.name()]

    def asks(self, question: Question) -> object:
        """Ask a question.
        
        :param question: the question to ask."""
        return question.answered_by(self)
