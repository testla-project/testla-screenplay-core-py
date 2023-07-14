
from typing import Literal
from src.testla_screenplay.interfaces import IActor
from src.testla_screenplay.action import Action
from .use_ability import UseAbility


class UtilizeAction(Action):

    def __init__(self, mode: Literal['get', 'set'] = 'get', payload: object | None = None) -> None:
        self.mode = mode
        self.payload = payload

    def perform_as(self, actor: IActor) -> object:
        ability = UseAbility.As(actor, self.ability_alias)
        if self.mode == 'set':
            return ability.set_payload(self.payload)
        else:
            return ability.get_payload()
        
    @staticmethod
    def get_ability_payload():
        return UtilizeAction()
    
    @staticmethod
    def set_ability_payload(payload: object):
        return UtilizeAction('set', payload)