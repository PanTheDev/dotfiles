from __future__ import annotations

import pprint
import re
import tomllib

from asyncio import Condition
from pathlib import Path
from typing import Any, Literal, NoReturn

from pydantic import BaseModel, ConfigDict, Field, model_validator

from panoplie.exceptions.exceptions import ManifestNotFoundError
from panoplie.manifest.manifest_types import CommandType, PromptName


# from pydantic_extra_types.semantic_version import SemanticVersion


class PanoplieManifest(BaseModel):
    prompts: None | dict[str, ChoicePrompt | TextPrompt | SecretPrompt] = Field(
        None, description=""
    )
    tasks: None | dict[str, Task] = Field(None, description="")
    installs: None | dict[str, Install] = Field(None, description="")
    dotfiles: None | dict[str, Dotfile] = Field(None, description="")

    model_config = ConfigDict(extra="forbid")

    @classmethod
    def from_toml(cls, manifest_path: Path | str) -> PanoplieManifest:
        return PanoplieManifest.model_validate(cls._parse_toml(Path(manifest_path)))

    @classmethod
    def _parse_toml(cls, manifest_path: Path) -> dict | NoReturn:
        cls._check_manifest_exists(manifest_path)
        with open(manifest_path, "rb") as manifest_file:
            manifest_toml = tomllib.load(manifest_file)
        return manifest_toml

    @classmethod
    def _check_manifest_exists(cls, manifest_path: Path) -> None | NoReturn:
        if not manifest_path.is_file():
            raise ManifestNotFoundError(
                f"Manifest file '{manifest_path.absolute()}' does not exist."
            )

        if not re.match(r"^(.+\.)?panoplie\.toml$", manifest_path.name):
            raise ManifestNotFoundError()


class Command(BaseModel):
    cmd: CommandType


class Prompt(BaseModel):
    prompt: None | str = Field(None, description="")
    input_type: Literal["choice", "text", "secret"]
    when: Literal["pre-install", "post-install"] = Field(
        "pre-install", description="When to ask "
    )


class ChoicePrompt(Prompt):
    input_type: Literal["choice"]
    choices: list[str] = Field(..., description="")


class TextPrompt(Prompt):
    input_type: Literal["text"]
    validation: str  # TODO


class SecretPrompt(Prompt):
    input_type: Literal["secret"]
    validation: str  # TODO


class Install(BaseModel):
    handler: str
    options: dict[str, Any]  # Todo restrict to toml approved types
    env: dict[str, str]
    condition: None | str = Field(None, description="")

    @model_validator
    def validate_condition():
        pass


class Task(BaseModel):
    pass


class Dotfile(BaseModel):
    pass


if __name__ == "__main__":
    pprint.PrettyPrinter().pprint(PanoplieManifest.model_json_schema())
    pprint.PrettyPrinter().pprint(
        PanoplieManifest.from_toml("manifest/example.panoplie.toml")
    )
