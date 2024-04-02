from base64 import b64decode
from unittest import TestCase

from webqr import app


class Test(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_qr_encode(self):
        response = self.client.get(
            "/qr/encode?data=foo&box_size=1&border=0&error_correction=1&version=1"
        )
        expected_encoded = "iVBORw0KGgoAAAANSUhEUgAAABUAAAAVAQAAAACBbJg7AAAAX0lEQVR4nAFUAKv/AAGkAAJ86fAARSUQAgCIAAIAKAACOCDgAAFUAAD/J/gEEfngBJLb6ACMFyAE2ubjBA64qwD/SsACAv7gAH0CMABFSNACAFX4AEUXcAI4BlgBAXTLRTca6echFJcAAAAASUVORK5CYII="
        self.assertEqual(response.data, b64decode(expected_encoded))
