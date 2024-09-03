import sys

from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

from exceptions.exceptions import ManifestNotFoundError
from simple_parsing import ArgumentParser, field

from panoplie.common.utils import find_manifest
from panoplie.manifest.manifest import PanoplieManifest


@dataclass
class Init:
    shell: str = field("bash", positional=True)


def find_manifest_path_if_none(manifest_path: None | Path) -> Path | NoReturn:
    if manifest_path is not None:
        return manifest_path
    try:
        return find_manifest()
    except FileNotFoundError as e:
        raise ManifestNotFoundError()


def main(argv: list[str]):
    args = parse_args(argv)
    manifest_path = find_manifest_path_if_none(args.manifest_path)
    manifest = PanoplieManifest.from_toml(manifest_path)


def parse_args(argv: list[str]):
    parser = ArgumentParser()

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
