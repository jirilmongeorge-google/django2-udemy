from django.test import TestCase

from app.calc import add
from app.calc import subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        #test that two numbers together***
        self.assertEqual(add(8, 3), 11)

    def test_substract_numbers(self):
        # test substract numbers
        self.assertEquals(subtract(11,5), 6)