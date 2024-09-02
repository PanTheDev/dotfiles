from __future__ import annotations

import sys

from dataclasses import dataclass
from typing import Sequence

from commands.command import Command
from commands.init.init import Init
from commands.install.install import Install
from simple_parsing import ArgumentParser, field


def main(argv: list[str]):
    args = parse_args(argv)
    command = Command(args.command.command)
    command.execute()


@dataclass
class PanoplieOptions:
    verbose: bool = field(False, alias="-v", action="store_true")


@dataclass
class CommandArguments:
    command: Init | Install


def parse_args(argv: list[str]):
    parser = ArgumentParser()
    parser.add_arguments(PanoplieOptions, dest="options")
    parser.add_arguments(CommandArguments, dest="command")

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
