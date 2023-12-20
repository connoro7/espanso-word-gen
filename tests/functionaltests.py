import main
import unittest
import os
import sys
import time


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main(self):
        self.assertEqual(main.main(DEBUG=True), None)
