from typing import NoReturn

from exceptions.exceptions import PanoplieException
from manifest.manifest import PanoplieManifest


class PanoplieExecutor:
    def __init__(self, manifest: PanoplieManifest) -> None | NoReturn:
        self.preprocess_done = False
        self.manifest = manifest
        self.preprocess()

    def preprocess(self):
        pass

    def apply(self):
        if not self.preprocess_done:
            raise PanoplieException
