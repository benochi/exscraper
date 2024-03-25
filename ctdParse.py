from bs4 import BeautifulSoup

# Read the HTML file insert your html filename
with open("filename.html", "r") as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the tag types you are interested in
tag_types = [
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "a",
    "div",
    "p",
    "img",
    "section",
    "article",
    "header",
    "footer",
    "nav",
]

# Initialize a dictionary to hold the count of each tag
tag_counts = {}

# Iterate over each tag type and count them
for tag_type in tag_types:
    tag_counts[tag_type] = len(soup.find_all(tag_type))

# Print out the counts
for tag, count in tag_counts.items():
    print(f"{tag}: {count}")

# Find all 'a' tags for links and save them to urls.txt
urls = [link["href"] for link in soup.find_all("a", href=True)]

with open("urls.txt", "w") as file:
    for url in urls:
        file.write(url + "\n")
