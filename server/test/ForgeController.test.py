def example():
    a = 4
    
class TestForgeController(unittest.TestCase):
    def setUp(self):
        self.controller = ForgeController()

    def test_method1(self):
        # Test the 'method1' function in the 'ForgeController' class
        result = self.controller.method1()
        self.assertEqual(result, expected_output)

    def test_method2(self):
        # Test the 'method2' function in the 'ForgeController' class
        result = self.controller.method2()
        self.assertEqual(result, expected_output)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()