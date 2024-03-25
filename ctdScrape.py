import requests
from urllib.parse import urlparse

# URL of the website you want to download
url = ""

# Parse the URL to extract the domain
parsed_url = urlparse(url)
domain = parsed_url.netloc

# Optional: Remove common prefixes and suffixes (like 'www.' or '.com')
clean_domain = domain.replace("www.", "").split(".")[0]

# Name of the file where you want to save the HTML content
file_name = f"{clean_domain}.html"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the page
    html_content = response.text

    # Open the file in write mode and write the HTML content
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"The HTML content has been saved to '{file_name}'")
else:
    print("Failed to retrieve the website content")
