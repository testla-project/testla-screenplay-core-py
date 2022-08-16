# Testla Screenplay

## Introduction

The testla project is a collection of tools of different tools to help in the QA automation process.
Testla screenplay core defines the frame for an implementation of the Screenplay Pattern.

## What is Screenplay Pattern and how does it work?

The Screenplay Pattern is a user-centred approach to writing high-quality automated tests. It steers you towards an effective use of layers of abstraction, helps your tests capture the business vernacular, and encourages good testing and software engineering habits.

Instead of focusing on low-level, interface-centric interactions, you describe your test scenarios in a similar way you'd describe them to a human being - an actor in Screenplay-speak. You write simple, readable and highly-reusable code that instructs the actors what activities to perform and what things to check. The domain-specific test language you create is used to express screenplays - the activities for the actors to perform in a given test scenario.

The Screenplay Pattern is beautiful in its simplicity. It's made up of five elements, five types of building blocks that Testla gives you to design any functional acceptance test you need, no matter how sophisticated or how simple.

The key elements of the pattern are: actors, abilities, tasks, actions and questions.

![Screenplay Pattern](/doc/screenplay.png)

## How to use this package?

### Define an ability

Abilities are essential since they define _what_ an actor _can do_. So the first thing we need to do is to define an ability by extending the testla ability.

```py
from @testla/screenplay import Ability, Actor

class MyBrowseAbility(Ability):
    def __init__(self, page: Page):
        super.__init__()
        self.page = page
    
    # passing in whatever is required for this ability
    # in our example a page object from playwright
    @staticmethod
    def using(page: Page) -> "MyBrowseAbility":
        return MyBrowseAbility(page)

    # this function is essential so that the actor can execute a task/action with this ability
    @staticmethod
    def As(actor: Actor) -> "MyBrowseAbility":
        return actor.with_ability_to(MyBrowseAbility)

    # navigate functionality by using playwright spicific code for our example
    def navigate(self, url: str) -> None:
        return self.page.goto(url)

    # fill functionality by using playwright spicific code for our example
    def fill(self, locator: str, value: str) -> None:
        return self.page.fill(locator, value)

    # click functionality by using playwright spicific code for our example
    def click(self, locator: str) -> None:
        return self.page.click(locator)

    # find functionality by using playwright spicific code for our example
    def find(locator: string) -> object:
        return self.page.wait_for_selector(locator)

    # further implementations
    # ...
```

### Define actions

The next step is to define actions and which can be grouped into tasks later. Actions use abilities to perform actual activities.

```py
from @testla/screenplay import Actor, Action

class Navigate(Action):

    def __init__(self, url: str):
        super.__init__()
        self.url = url

    # the actual implementation of the action
    def perform_as(self, actor: Actor) -> object:
        return MyBrowseAbility.As(actor).navigate(self.url)

    # static member method to invoke the action
    @staticmethod
    def to(url: string) -> "Navigate": 
        return Navigate(url)

class Fill(Action):

    def __init__(self, locator: str, value: str) {
        super.__init__()
        self.locator = locator
        self.value = value
    }

    # the actual implementation of the action
    def perform_as(self, actor: Actor) -> object:
        return MyBrowseAbility.As(actor).fill(self.locator, self.value)

    # static member method to invoke the action
    @staticmethod
    def With(locator: str, value: str) -> "Fill":
        return Fill(locator, value)


class Click(Action):

    def __init__(self, locator: str):
        super.__init__()
        self.locator = locator

    # the actual implementation of the action
    def perform_as(self, actor: Actor) -> object:
        return MyBrowseAbility.As(actor).click(self.locator)

    # static member method to invoke the action
    @staticmethod
    def on(locator: str) -> "Click":
        return Click(locator)
```

### Define a task

Tasks group actions into logical entities.

```py
from @testla/screenplay import Actor, Task

class Login(Task):
    
    # the actual implementation of the task
    def perform_as(actor: Actor) -> object:
        return actor.attempts_to(
            Navigate.to("https://www.my-fancy-url.com"),
            Fill.With("#username", actor.username),
            Fill.With("#password", actor.password),
            Click.on("#login-button"),
        )

    # static member method to invoke the task
    @staticmethod
    def to_app() -> "Login":
        return Login()
```

### Define a question

Questions are used to check the status of the application under test.

```py
from @testla/screenplay import Actor, Question

class LoginStatus(Question):

    # the actual implementation of the task
    def answered_by(actor: Actor) -> object:
        return BrowseTheWeb.as(actor).find("#logged-in-indicator")

    # static member method to invoke the question
    @staticmethod
    def of():
        return LoginStatus()
```

### Define a test case

The final step is to define a test case using the Actions and Abilities defined above.

```py
from @testla/screenplay import Actor

# Example test case with Playwright
def my_first_test(page):
    actor = Actor.named("James")
        .With("username", "John Doe")
        .With("password", "MySecretPassword")
        .can(MyBrowseAbility.using(page))

    actor.attempts_to(Login.to_app())

    expect(actor.asks(LoginStatus.of())).not.to_be_null()
```

### What about the 'Screen' in 'Screenplay'?

With screen is meant that all locators for page elements are held in specific files/collections. In our example from above we put the locators inline. A sample screen file for the Login task could look like this:

```py
# screen.py

LOGIN_URL = "https://www.my-fancy-url.com"
USERNAME_INPUT = "#username"
PASSWORD_INPUT = "#password"
LOGIN_BUTTON = "#login-button"
```

Within the task the screen elements are then used as:

```py
from @testla/screenplay import Actor
from screen import LOGIN_URL, USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON

def perform_as(actor: Actor) -> object:
    return actor.attempts_to(
        Navigate.to(LOGIN_URL),
        Fill.With(USERNAME_INPUT, actor.states('username')),
        Fill.With(PASSWORD_INPUT, actor.states('password')),
        Click.on(LOGIN_BUTTON),
    )
```