from discord.ext.commands import CommandError

class PokemonNotFound(CommandError):
    'Exception raised, Pokemon not found'
    pass

class PokemonInvalidContext(CommandError):
    'Exception raised, Pokemon invalid in context'

    def __init__(self, invalid_mons):
        self.invalid_mons = invalid_mons
    
class MoveNotFound(CommandError):
    'Exception raised, move not found'
    pass

class MoveInvalid(CommandError):
    'Exception raised, move not learned by Pokemon'
    pass



