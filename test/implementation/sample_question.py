
from typing import Literal
from src.testla_screenplay.interfaces import IActor
from src.testla_screenplay.question import Question
from .use_ability import UseAbility


class SampleQuestion(Question):

    def __init__(self, check_mode: Literal['to_have','not_to_have'], val: object):
        self.check_mode = check_mode
        self.val = val

    def answered_by(self, actor: IActor) -> object:
        ability = UseAbility.As(actor, self.ability_alias)
        payload = ability.get_payload()
        assert (self.val == payload) == (self.check_mode == 'to_have')

        return True
    
    @staticmethod
    def to_have_payload(val: object):
        return SampleQuestion('to_have', val)
    
    @staticmethod
    def not_to_have_payload(val: object):
        return SampleQuestion('not_to_have', val)
