class UsingAlias():
    """An object representing a task that an IActor can perform."""
    ability_alias: str | None = None
    
    def with_ability_alias(self, alias: str | None = None):
        self.ability_alias = alias
        return self