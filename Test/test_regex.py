import unittest
import re
class TettRegex(unittest.TestCase):
    
    def setup():
        pass
    def tearDown(self) -> None:
        pass

    def test_one_extension(self):
        extension = "rar"
        regex = re.compile(r'\.rar$', re.IGNORECASE)
        self.assertRegex("Android Studio 4.0 Development Essentials - Java Edition.rar",regex)

if __name__ == "__main__":
    unittest.main()