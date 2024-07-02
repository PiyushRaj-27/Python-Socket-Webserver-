from bs4 import BeautifulSoup
import os

'''
Function to parse the html page for linking any style sheet.
Though server should send css file when requested.
'''

def htmlParser(html: str) -> str:
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)

    soup = BeautifulSoup(html, "html.parser")

    cssResources = set()

    # Find and remove all link tags with rel="stylesheet"
    links = soup.find_all('link', rel='stylesheet')
    for link in links:
        cssResources.add(link.get("href"))
        link.decompose()  # Remove the CSS request from head

    # This will contain all the CSS content
    defaultAdd = ""
    if cssResources:
        for res in cssResources:
            try:
                resourcePath = os.path.join(parent_dir, f"styles/{res}")
                with open(resourcePath, "r") as c:
                    defaultAdd += c.read()
                    defaultAdd += "\n"
            except Exception as e:
                print(f"Failed to GET {res}: {e}")
                return html

    # Add the combined CSS styles to the HTML
    style_tag = soup.new_tag("style")
    style_tag.string = defaultAdd
    soup.head.append(style_tag)

    return str(soup)
    