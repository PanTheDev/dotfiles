import os

from typing import NoReturn


class EnvVarsManager:
    pass

    @classmethod
    def set_env_var(name: str, value: str) -> None | NoReturn:
        os.environ[name] = value

    @classmethod
    def unset_env_var(name: str) -> None | NoReturn:
        del os.environ[name]
