from simple_parsing import field
from dataclasses import dataclass

@dataclass
class Install:
    package: str = field(positional=True)