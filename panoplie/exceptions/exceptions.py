class PanoplieException(Exception):
    pass


class ManifestError(PanoplieException):
    pass


class InvalidManifestError(ManifestError):
    pass


class ManifestNotFoundError(ManifestError):
    pass
