
from src.testla_screenplay.interfaces import IActor
from src.testla_screenplay.task import Task
from .utilize_action import UtilizeAction


class WrapperTask(Task):

    def __init__(self):
        self.activities = [UtilizeAction.get_ability_payload()]

    def perform_as(self, actor: IActor) -> object:
        for activity in self.activities:
            activity.with_ability_alias(self.ability_alias)

        return actor.attempts_to(*self.activities)
    
    @staticmethod
    def execute():
        return WrapperTask()