class DirectDownloadLinkException(Exception):
    """No method found for extracting direct download link from the http link"""

    pass


class NotSupportedExtractionArchive(Exception):
    """The archive format use is trying to extract is not supported If This is an Error plz Do Report it : @movieskacona"""

    pass
