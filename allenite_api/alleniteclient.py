from allenite_api.exceptions import *
from typing import Union


class AlleniteClient:
    """
    Base class for Allenite API access.
    """

    def __init__(self):
        self.api_url = 'allenite-api.herokuapp.com'

    def get_respect(self, discord_id: Union[str, int]) -> int:
        """
        Get respect of a user.

        :param discord_id: The discord id of the user whose respect has to be retrieved.
        :return: The respect of the user.
        """
        json = self.fetch_json('respect', query_params={'id': discord_id})
        if 'respect' not in json:
            raise AlleniteResourceNotFound('respect')

        return json['respect']

    def get_clash_royale_tag(self, discord_id: Union[str, int]) -> str:
        """
        Get the clash royale tag of a user.

        :param discord_id: The discord id of the user whose respect has to be retrieved.
        :return: The tag of the user.
        """
        json = self.fetch_json('cr', query_params={'id': discord_id})
        if 'clash_tag' not in json:
            raise AlleniteResourceNotFound('clash_tag')

        return json['clash_tag']

    def get_random_meme(self) -> tuple:
        """
        A random meme with a title and the link.

        **Example**:

            .. code-block:: python

                meme = client.get_random_meme()
                print('Title :', meme[0])
                print('Link :', meme[1])

        :return: A tuple containing the title at index zero and link at index one.
        """
        json = self.fetch_json('meme')
        if 'title' not in json:
            raise AlleniteResourceNotFound('title')
        if 'meme_url' not in json:
            raise AlleniteResourceNotFound('meme_url')

        return json['title'], json['meme_url']

    def get_nordvpn_account(self) -> str:
        """
        Get a link to the details of the VPN account.

        :return: The link to the details of the account.
        """
        json = self.fetch_json('nordvpn')
        if 'link' not in json:
            raise AlleniteResourceNotFound('link')

        return json['link']

    def get_encrypted_text(self, text: str) -> str:
        """
        Get an encrypted message based on the input entered.
        The message can be decrypted using :func:`~alleniteclient.AlleniteClient.get_decrypted_text`

        :param text: The text to encrypted
        :return: A string containing the encrypted text.
        """
        json = self.fetch_json('enc', query_params={'text': text})
        if 'encrypted' not in json:
            raise AlleniteResourceNotFound('encrypted')

        return json['encrypted']

    def get_decrypted_text(self, text: str) -> str:
        """
        Get the decrypted message based on the input entered.
        The text has to have beeen encrypted using :func:`~alleniteclient.AlleniteClient.get_encrypted_text`

        :param text: The text to be decrypted.
        :return: A string containing the decrypted text.
        """
        json = self.fetch_json('dec', query_params={'text': text})
        if 'decrypted' not in json:
            raise AlleniteResourceNotFound('decrypted')

        return json['decrypted']

    def fetch_json(self, url_path: str, http_method: str = 'GET', secure: bool = True, headers: dict = None,
                   query_params: dict = None, post_data: dict = None) -> dict:
        """
        Fetch some JSON from Allenite's API.

        :param url_path: The url to fetch the JSON from.
        :param http_method: The http method that will be used with the request.
        :param secure: Specify whether to use HTTPS (True) or HTTP (False).
        :param headers: The headers to pass through the request.
        :param query_params: The url parameters to include with the request.
        :param post_data: The post data to send with the request.

        :return: A dict containing the parsed JSON response
        :meta private:
        """
        # Specify values of method parameters explicitly
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_data is None:
            post_data = {}
        if secure is None:
            secure = False

        headers['Content-Type'] = 'application/json; charset=utf-8'
        headers['Accept'] = 'application/json'

        # Removes a leading slash if included in the url_path.
        if url_path[0] == '/':
            url_path = url_path[1:]
        url = ('https://' if secure else 'http://') + self.api_url + '/' + url_path

        # Perform the HTTP request using the provided parameters.
        response = requests.request(http_method, url, params=query_params, headers=headers, data=post_data)

        if response.status_code == 429:
            raise AlleniteRateLimited(url, response)
        if response.status_code != 200:
            raise AlleniteResponseUnavailable(url, response)

        return response.json()
