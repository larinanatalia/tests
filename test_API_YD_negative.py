from ad_py.Test.new_folder import new_folder_negative
import unittest

class TestFails(unittest.TestCase):
    def test_wrong_type_args(self):
        self.assertRaises(TypeError, new_folder_negative, ("new_folder"))
