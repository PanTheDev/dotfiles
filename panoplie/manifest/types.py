from pathlib import PosixPath
from typing import Annotated, NoReturn

from pydantic import BeforeValidator


def validate_path(v: str) -> str | NoReturn:
    try:
        if str(posix_path := PosixPath(v)) != v:
            raise ValueError()
    except (TypeError, ValueError) as e:
        raise ValueError from e
    return v


StrictPath = Annotated[PosixPath, BeforeValidator(validate_path)]
Condition = str
