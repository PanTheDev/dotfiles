from simple_parsing import field
from dataclasses import dataclass

@dataclass
class Init:
    shell: str = field("bash", positional=True)