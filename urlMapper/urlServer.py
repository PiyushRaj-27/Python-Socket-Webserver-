from .urlMapped import urls, DEFAULT_NOT_FOUND
from parsers.htmlParser import htmlParser
import os
mappings = urls
defaultNF = DEFAULT_NOT_FOUND

def returnFiles(parsed: dict):

    # current Dir and Parent Directory!
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)

    # fallback resource path
    defaultNFresourcePath = os.path.join(parent_dir, f"pages\{defaultNF}")

    # not a valid request, send fallback
    if len(parsed) == 0:
        try:
            with open(defaultNFresourcePath, "r") as f:
                data = f.read()
                return data
        except:
            print(f"Could not open the file! {resourcePath}")
            return ""
    
    #valid request, send resource
    try:
        requestedResource = parsed["requested"]
        docLocation = ""

        # Find html page corresoponding to the url
        if requestedResource in mappings:
            docLocation = mappings[requestedResource]
        else:
            docLocation = defaultNF

        resourcePath = os.path.join(parent_dir, f"pages\{docLocation}")
        try:
            with open(resourcePath, "r") as f:
                data = f.read()
                data = htmlParser(data)
                return data
        except:
            print(f"Could not open the file! {resourcePath}")
            return ""
    except:
        try:
            with open(defaultNFresourcePath, "r") as f:
                data = f.read()
                return data
        except:
            print(f"Could not open the file! {resourcePath}")
            return ""