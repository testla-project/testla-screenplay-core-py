from src.testla_screenplay.actor import Actor
from .implementation.wrapper_task import WrapperTask
from .implementation.use_ability import UseAbility
from .implementation.utilize_action import UtilizeAction
from .implementation.sample_question import SampleQuestion


# 'Defining an actor who states its name and attributes'
def test_actor():
    test_actor = Actor.named("Test Actor").With("an attribute", 1)

    assert test_actor.states("name") == "Test Actor"
    assert test_actor.states("an attribute") == 1

# Register an ability with an actor and use it via action
def test_ability():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test"))
    retrieved_value = test_actor.attempts_to(
        UtilizeAction.get_ability_payload()
    )
    assert retrieved_value == "test"

# Trigger multiple actions at one shot
def test_multiple_actions():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test"))
    retrieved_value = test_actor.attempts_to(
        UtilizeAction.set_ability_payload("another test"),
        UtilizeAction.get_ability_payload()
    )
    assert retrieved_value == "another test"

# Try using an action without actor having the corresponding ability assigned
def test_ability_not_assigned():
    has_error = False
    test_actor = Actor.named("Test Actor")
    try:
        test_actor.attempts_to(
            UtilizeAction.get_ability_payload()
        )
    except:
        has_error = True
    assert has_error

# Register an ability with an actor and use it via task that wrappes action
def test_task():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test"))
    retrieved_value = test_actor.attempts_to(
        WrapperTask.execute()
    )
    assert retrieved_value == "test"

# Register an ability with an actor and ask a question
def test_question():    
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test"))
    assert test_actor.asks(
        SampleQuestion.to_have_payload("test")
    )
    assert test_actor.asks(
        SampleQuestion.not_to_have_payload("test1")
    )

# Register an ability with an actor and ask 2 questions at the same time
def test_questions_at_same_time():    
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test"))
    assert test_actor.asks(
        SampleQuestion.to_have_payload("test"),
        SampleQuestion.not_to_have_payload("test1")
    )

# Try using a question without actor having the corresponding ability assigned
def test_question_no_ability():
    has_error = False
    test_actor = Actor.named("Test Actor")
    try:
        test_actor.asks(
            SampleQuestion.to_have_payload("test")
        )
    except:
        has_error = True
    assert has_error

# Register an ability (with alias) with an actor and use it via action
def test_ability_alias():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test").with_alias("test alias"))
    retrieved_value = test_actor.attempts_to(
        UtilizeAction.get_ability_payload().with_ability_alias("test alias"),
    )
    assert retrieved_value == "test"

# Register 2 abilities (1 with alias) with an actor and use them via action
def test_multiple_abilties_alias():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test")).can(UseAbility.using("test with alias").with_alias("test alias"))
    retrieved_value = test_actor.attempts_to(
        UtilizeAction.get_ability_payload()
    )
    assert retrieved_value == "test"

    retrieved_value_with_alias = test_actor.attempts_to(
        UtilizeAction.get_ability_payload().with_ability_alias("test alias")
    )
    assert retrieved_value_with_alias == "test with alias"

# Register an ability (with alias) with an actor and use it via task
def test_task_alias():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test").with_alias("test alias"))
    retrieved_value = test_actor.attempts_to(
        WrapperTask.execute().with_ability_alias("test alias"),
    )
    assert retrieved_value == "test"

# Register an ability (with alias) with an actor and use it with a question
def test_question_alias():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test").with_alias("test alias"))
    assert test_actor.asks(
        SampleQuestion.to_have_payload("test").with_ability_alias("test alias")
    )

# Register 2 abilities (1 with alias) with an actor and use them with questions
def test_multiple_questions_alias():
    test_actor = Actor.named("Test Actor").can(UseAbility.using("test")).can(UseAbility.using("test with alias").with_alias("test alias"))
    assert test_actor.asks(
        SampleQuestion.to_have_payload("test")
    )
    assert test_actor.asks(
        SampleQuestion.to_have_payload("test with alias").with_ability_alias("test alias")
    )
