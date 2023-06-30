import requests
import re
from bs4 import BeautifulSoup

print("==> Welcome to the Bullet Scraper Level 1 (Simple HTML) <==")

# Prompt the user to input a website URL and file name
url = input("==> Enter the website URL: ")
file_name = input("==> Enter the output file name: ") + ".txt"

# Send a GET request to fetch the web page content
response = requests.get(url)
page_content = response.text

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_content, 'html.parser')

# Define the regex pattern
pattern = r'\-\s*([\w\W\s]*?);\s*([\w\W\s]*?)--\s*([\w\W\s]*)'

# Extract the relevant portions from the parsed HTML
relevant_content = soup.find_all(string=re.compile(pattern))

# Write the matching snippets to a text file
with open(file_name, "w") as file:
    for i, content in enumerate(relevant_content):
        matches = re.findall(pattern, content)
        for j, match in enumerate(matches):
            snippet = " - ".join(match)
            file.write(snippet)

# Clean up the file by removing repeated new lines
with open(file_name, 'r') as file:
    lines = file.readlines()

cleaned_lines = []
for line in lines:
    cleaned_line = line.rstrip('\n')
    if cleaned_line:
        cleaned_lines.append(cleaned_line)

with open(file_name, 'w') as file:
    file.write('\n'.join(cleaned_lines))

print(f"==> Matching snippets have been saved to {file_name}.")
