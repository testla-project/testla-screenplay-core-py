from typing import Any
from interfaces import IActor
from ability import Ability
from action import Action
from task import Task
from question import Question

class Actor(IActor):
    """Actors use abilities in order to execute tasks/actions and answer questions."""

    def __init__(self, name: str) -> None:
        super().__init__()
        self.attributes = {} # collection of attributes assigned to the actor
        self.ability_map = {} # map of abilities of this Actor; maps types 
        self.name = name # name of this actor

    def With(self, key: str, value: Any) -> IActor:
        """Store an attribute in the actors attribute collection.

        :param key: attribute name
        :param value: attribute value
        :returns: this Actor
        """
        self.attributes[key] = value
        return self

    def states(self, key: str) -> Any:
        """Get an attribute from the actors attribute collection.

        :param key: the key for the attribute
        :returns: the value for the requested attribute
        """
        return self.attributes[key]

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
        """Assign one or more abilities to the actor. e.g. Browsing, SFT-Client, HTTP-Client, ...
        
        :param abilites: the abilities the actor will be able to use.
        """
        for ability in abilities:
            self.ability_map[type(ability)] = ability
        return self

    def attempts_to(self, *activities: Action | Task) -> Any:
        """Executes the given Tasks/Actions."""
        for activity in activities:
            result = activity.perform_as(self)
        return result

    def with_ability_to(self, ability: Ability) -> Ability:
        """Verify if the actor has the given ability."""
        if ability not in self.ability_map:
            raise RuntimeError("Error: This Actor does not have this ability: " + str(ability))
        else:
            return self.ability_map[ability]

    def asks(self, question: Question) -> Any:
        """Ask a question.
        
        :param question: the question to ask."""
        return question.answered_by(self)
