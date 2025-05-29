from curl_cffi import requests
from colorama import Fore, Style

base_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://static.agent301.org",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://static.agent301.org/",
    "sec-ch-ua": '"Microsoft Edge";v="136", "Microsoft Edge WebView2";v="136", "Not.A/Brand";v="99", "Chromium";v="136"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}