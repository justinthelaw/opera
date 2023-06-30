import httpx
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

 # Track visited URLs to avoid duplicates
visited_urls = set()

# crawl and scrape a page based on the bullet regex pattern
async def crawl_page(url, file_name):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Prepend 'http://' protocol if missing

    async with httpx.AsyncClient() as client:
        # Send an async GET request to fetch the web page content
        response = await client.get(url)
        page_content = response.text

        # Create BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_content, 'html.parser')

        # Define the regex pattern
        pattern = r'\-\s*([\w\W\s]*?);\s*([\w\W\s]*?)--\s*([\w\W\s]*)'

        # Extract the relevant portions from the parsed HTML
        relevant_content = soup.find_all(string=re.compile(pattern))

        # Write the matching snippets to a text file
        with open(file_name, "a") as file:
            for _, content in enumerate(relevant_content):
                matches = re.findall(pattern, content)
                for _, match in enumerate(matches):
                    snippet = " - ".join(match)
                    file.write(snippet + "\n")
        
        clean_lines(file_name)

        # Find all links on the page and crawl them recursively
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if absolute_link not in visited_urls:
                visited_urls.add(absolute_link)
                crawl_page(absolute_link, file_name)

# clean extra new line spacing
def clean_lines(file_name):
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

async def main():
    print("==> Welcome to the Bullet Scraper Level 1 (Simple HTML) <==")

    # Prompt the user to input a website URL and file name
    url = input("==> Enter the website URL: ")
    file_name = input("==> Enter the output file name: ") + ".txt"

    await crawl_page(url, file_name)

    print(f"==> Matching snippets have been saved to {file_name}.")

# Run the main function asynchronously
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
