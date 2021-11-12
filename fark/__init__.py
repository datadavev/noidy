
import typing


class Minter:

    def __init__(self):
        self.name = "Abstract minter"
        pass

    def mint(self, count:int = 1) -> typing.Generator[str, None, None]:
        raise(NotImplementedError("Base Minter must be overridden"))

