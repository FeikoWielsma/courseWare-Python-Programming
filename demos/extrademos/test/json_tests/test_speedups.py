from unittest import TestCase

from json import decoder, encoder, scanner


class TestSpeedups(TestCase):
    def test_scanstring(self):
        self.assertEqual(decoder.scanstring.__module__, "_json")
        self.assertTrue(decoder.scanstring is decoder.c_scanstring)

    def test_encode_basestring_ascii(self):
        self.assertEqual(encoder.encode_basestring_ascii.__module__, "_json")
        self.assertTrue(
            encoder.encode_basestring_ascii is encoder.c_encode_basestring_ascii
        )


class TestDecode(TestCase):
    def test_make_scanner(self):
        self.assertRaises(AttributeError, scanner.c_make_scanner, 1)

    def test_make_encoder(self):
        self.assertRaises(
            TypeError,
            encoder.c_make_encoder,
            (True, False),
            b"\xcd\x7d\x3d\x4e\x12\x4c\xf9\x79\xd7\x52\xba\x82\xf2\x27\x4a\x7d\xa0\xca\x75",
            None,
        )
