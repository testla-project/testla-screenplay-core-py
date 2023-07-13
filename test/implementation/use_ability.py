from src.testla_screenplay.ability import Ability
from src.testla_screenplay.actor import Actor

class UseAbility(Ability):

    def __init__(self, payload: object):
        self.payload = payload

    @staticmethod
    def using(payload: object):
        return UseAbility(payload)
    
    @staticmethod
    def As(actor: Actor, alias: str | None = None) -> "UseAbility":
        return actor.with_ability_to(UseAbility, alias)
    
    def get_payload(self):
        return self.payload
    
    def set_payload(self, payload: object):
        self.payload = payload