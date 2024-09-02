import re

from typing import Annotated

from annotated_types import LowerCase, MaxLen, MinLen, Predicate
from variables import TASK_NAME_MAX_CHARS


# Regexes
regex_is_valid_prompt_name = re.compile("^[a-z0-9-]+$")


# Predicates
def prompt_name_is_valid(prompt: str) -> bool:
    return bool(re.match(regex_is_valid_prompt_name, prompt))


predicate_prompt_name = Predicate(prompt_name_is_valid)

# Types
CommandType = list[str] | str
PromptName = Annotated[
    str, MinLen(3), MaxLen(TASK_NAME_MAX_CHARS), LowerCase, predicate_prompt_name
]
