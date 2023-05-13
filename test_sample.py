import unittest
import sys

def fire():
    return "fire tech"

class FireTest(unittest.TestCase):
    def test_fire(self):
        self.assertEqual(fire(), "fire tech")

    def test_fire2(self):
        self.assertNotEqual(fire(),"Fire Tech")

if __name__ == "__main__":
    sys.argv = ["", "FireTest.test_fire"]
    unittest.main()
