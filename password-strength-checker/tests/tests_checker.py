import unittest
from password_strength.checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_password(self):
        result = check_password_strength("abc")
        self.assertEqual(result["strength"], "Weak")

    def test_strong_password(self):
        result = check_password_strength("Str0ngPass!")
        self.assertIn(result["strength"], ["Strong", "Very Strong"])

    def test_common_password(self):
        result = check_password_strength("password")
        self.assertEqual(result["strength"], "Very Weak")

if __name__ == "__main__":
    unittest.main()
