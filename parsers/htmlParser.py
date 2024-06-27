from bs4 import BeautifulSoup
import os

def htmlParser(html: str) -> str:
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)

    soup = BeautifulSoup(html, "html.parser")

    cssResources = set()
    scriptResources = set() # TODO: Add same kind of linker for js script files as well!. This is not a test server though!

    links = soup.find_all('link')
    for res in links:
        if res.get("rel")[0] == "stylesheet":
            cssResources.add(res.get("href"))
    
    defaultAdd = ""
    if cssResources:
        for res in cssResources:
            try:
                resourcePath = os.path.join(parent_dir, f"styles\{res}")
                c = open(resourcePath, "r")
                defaultAdd += c.read()
                defaultAdd += "\n"
                c.close()
            except:
                print(f"Failed to GET {res}")
                return html
    
    data = f"\n<style> \n{defaultAdd} </style>"
    html += data
    return html
    