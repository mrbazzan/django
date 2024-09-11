from django.shortcuts import make_cake
from django.test import SimpleTestCase


class MakeCakeTests(SimpleTestCase):
    def test_make_cake(self):
        self.assertEqual(make_cake(), 'cake')
