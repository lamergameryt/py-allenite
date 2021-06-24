import unittest
from allenite_api import AlleniteClient
import re


class EndpointsTestCase(unittest.TestCase):
    """
    Tests for AlleniteClient API. These tests only test for one discord id.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls._client = AlleniteClient()
        cls._regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def test_clash_royale(self):
        tag = self._client.get_clash_royale_tag('287888563020890138')
        self.assertEqual(tag, '#UVUYG900', msg='The clash royale tag does not match.')

    def test_meme(self):
        meme = self._client.get_random_meme()
        self.assertIsNotNone(meme[0], msg='The meme title is None.')
        self.assertIsNotNone(meme[1], msg='The meme URL is None.')
        self.assertTrue(re.match(self._regex, meme[1]) is not None, msg='The meme url is not a valid url.')

    def test_nordvpn(self):
        account = self._client.get_nordvpn_account()
        self.assertIsNotNone(account, msg='The nordvpn account url is None.')
        self.assertTrue(re.match(self._regex, account), msg='The account url is not a valid url.')

    def test_encryption(self):
        original = "Hello, world!"
        encrypted = self._client.get_encrypted_text(original)
        decrypted = self._client.get_decrypted_text(encrypted)
        self.assertEqual(original, decrypted, msg='The enc/dec endpoints failed to function as expected.')
