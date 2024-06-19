'''
GET /house HTTP/1.1
Host: localhost:8002
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7       
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-US,en;q=0.9
Cookie: username-localhost-8888="2|1:0|10:1718040452|23:username-localhost-8888|44:MWFmNWMxYjM4MzlhNDBjNmEyYjJlNzdlOGYxY2U0NDU=|ae51afc7012ecc01b50bc3f3483dbcb9645ef8c8e7529b2e8b8becd98c3dc93a"; _xsrf=2|e14ac9cf|2ce390022c5c6398a909f7603d5ef5b8|1718040452

'''


def parseHTTPRequest(body: str):
    lines = body.split("\r\n")
    parsed = {}
    if len(lines) == 0:
        return parsed
    startLine = lines[0]
    startSplit = startLine.split(" ")
    try:
        parsed["type"] = startSplit[0]
        parsed["requested"] = startSplit[1]
        parsed["home"] = startSplit[2]
    except:
        pass
    return parsed

