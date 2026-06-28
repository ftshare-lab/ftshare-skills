#!/usr/bin/env python3
"""获取可转债全量列表（market.ft.tech）"""
import json
import sys
import urllib.error
import urllib.request
import urllib.parse
SAFE_URLOPENER = urllib.request.build_opener()

BASE_URL = "https://market.ft.tech"

def safe_urlopen(req_or_url):
    if isinstance(req_or_url, urllib.request.Request):
        url = req_or_url.full_url
    else:
        url = str(req_or_url)
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "market.ft.tech":
        print(f"Invalid URL for safe_urlopen: {url}", file=sys.stderr)
        sys.exit(1)
    return SAFE_URLOPENER.open(req_or_url)



def main():
    url = BASE_URL + "/gateway/api/v1/market/data/cb/cb-lists"
    req = urllib.request.Request(url, method="GET")

    try:
        with safe_urlopen(req) as resp:
            data = json.loads(resp.read().decode())
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
