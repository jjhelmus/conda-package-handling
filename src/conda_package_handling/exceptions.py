from errno import ENOENT


class InvalidArchiveError(Exception):
    """Raised when libarchive can't open a file"""
    def __init__(self, fn, msg, *args, **kw):
        msg = ("Error with archive %s.  You probably need to delete and re-download "
               "or re-create this file.  Message from libarchive was:\n\n%s" % (fn, msg))
        self.errno = ENOENT
        super(InvalidArchiveError, self).__init__(msg)


class CaseInsensitiveFileSystemError(Exception):
    def __init__(self, package_location, extract_location, **kwargs):
        message = ("""
        Cannot extract package to a case-insensitive file system. Your install
        destination does not differentiate between upper and lowercase
        characters, and this breaks things. Try installing to a location that
        is case-sensitive. Windows drives are usually the culprit here - can
        you install to a native Unix drive, or turn on case sensitivity for
        this (Windows) location?

          package location: %(package_location)s
          extract location: %(extract_location)s
        """)
        super(CaseInsensitiveFileSystemError, self).__init__(
            message,
            package_location=package_location,
            extract_location=extract_location,
            **kwargs
        )


class ConversionError(Exception):
    def __init__(self, missing_files, mismatching_sizes, *args, **kw):
        self.missing_files = missing_files
        self.mismatching_sizes = mismatching_sizes
        errors = ""
        if self.missing_files:
            errors = "Missing files in converted package: %s\n" % self.missing_files
        errors = (errors + "Mismatching sizes (corruption) in converted package: %s" %
                  self.mismatching_sizes)

        super(ConversionError, self).__init__(errors, *args, **kw)
