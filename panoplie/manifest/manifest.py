from __future__ import annotations

import tomllib

from pathlib import Path
from typing import Literal, NoReturn

from pydantic import BaseModel

from panoplie.exceptions.exceptions import ManifestNotFoundError
from panoplie.manifest.manifest_types import CommandType, PromptName


# from pydantic_extra_types.semantic_version import SemanticVersion


class PanoplieManifest(BaseModel):
    prompts: dict[str, Prompt]

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

        if manifest_path.name != "panoplie.toml":
            raise ManifestNotFoundError()


class Command(BaseModel):
    cmd: CommandType


class Prompt(BaseModel):
    prompt: str
    input_type: Literal["text", "choice", "secret"]
    choices: None | list[str] = None
    validation: None | str = None  # TODO regex type
    when: None | Literal["pre-install", "post-install"] = "pre-install"


if __name__ == "__main__":
    print(PanoplieManifest.from_toml("manifest/panoplie.toml"))
