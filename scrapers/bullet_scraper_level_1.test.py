import unittest
import subprocess

class TestBulletScraper(unittest.TestCase):
    def test_scraping(self):
        url = "https://www.eprbullets.com/AAC.htm"
        output_file = "testing-output"
        file_path = f"./{output_file}.txt"

        # Run the script as a subprocess
        process = subprocess.run(
            ["python3", "bullet_scraper_level_1.py"],
            input=f"{url}\n{output_file}\n",
            text=True,
            capture_output=True
        )

        # Check if the process exited successfully
        self.assertEqual(process.returncode, 0)

        # Check if the output file was created
        with open(file_path, "r") as file:
            content = file.read()
            self.assertTrue(content)

        # Clean up the created file
        subprocess.run(["rm", file_path])

if __name__ == '__main__':
    unittest.main()
