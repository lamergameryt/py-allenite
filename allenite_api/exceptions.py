import requests


class AlleniteResponseUnavailable(Exception):
    """
    Exception representing a failed request to a resource.
    """

    def __init__(self, url: str, response: requests.Response):
        super.__init__(self)
        self._url = url
        self._response = response

    def __str__(self):
        status = self._response.status_code
        try:
            json = self._response.json()
            if 'error' in json:
                error = json['error']
            elif 'message' in json:
                error = json['message']
            else:
                error = None

            return f'{self._url} : {"" if error is None else error} (HTTP Status: {status})'
        except TypeError:
            return f'{self._url} (HTTP Status: {status})'


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
