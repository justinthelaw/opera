import unittest
from server.services import ForgeService

class TestForgeService(unittest.TestCase):
    def setUp(self):
        self.service = ForgeService()

    def test_method1(self):
        # Replace 'method1' with the actual method name and add your test code
        result = self.service.method1(input)
        self.assertEqual(result, expected_output)

    def test_method2(self):
        # Replace 'method2' with the actual method name and add your test code
        result = self.service.method2(input)
        self.assertEqual(result, expected_output)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()