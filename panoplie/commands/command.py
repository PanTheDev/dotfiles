from typing import Sequence

class Command:
    def __init__(self, command_name: str):
        self.command_name: str = command_name
        self.command: callable = self.find_command(self.command_name)

    def execute(self, args: Sequence[str] = None):
        self.command(args)

    def find_command(self, command: str) -> callable:
        return lambda _: print(f"Executing command: '{command}'.")