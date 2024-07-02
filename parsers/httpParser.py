

'''
Function to parse incoming HTTP request.
We only need to extract the type of request, requested resource and version
'''
def parseHTTPRequest(body: str):

    # spliting the request body
    lines = body.split("\r\n")

    # dictionary to store the information
    parsed = {}

    if len(lines) == 0:
        return parsed
    
    # the first line contains all the information for us right now
    startLine = lines[0]
    startSplit = startLine.split(" ")

    try:
        parsed["type"] = startSplit[0]
        parsed["requested"] = startSplit[1]
        parsed["version"] = startSplit[2]

        print(f"{parsed['type'].capitalize()} {parsed['requested']}")
    except:
        pass

    return parsed

