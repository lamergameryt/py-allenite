import requests


class AlleniteResponseUnavailable(Exception):
    """
    Exception representing a failed request to a resource.
    """

    def __init__(self, url: str, response: requests.Response):
        super.__init__(self)
        self._url = url
        self._status = response.status_code

    def __str__(self):
        return f'{self._url} (HTTP Status: {self._status})'


class AlleniteRateLimited(AlleniteResponseUnavailable):
    """
    Exception representing a rate limited endpoint.
    """
    pass


class AlleniteResourceNotFound(Exception):
    """
    Exception representing a value not found in the response.
    """

    def __init__(self, parameter: str):
        super.__init__(self)
        self._parameter = parameter

    def __str__(self):
        return f'Parameter Not Found: {self._parameter}'
