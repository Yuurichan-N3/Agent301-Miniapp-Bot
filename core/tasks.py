from curl_cffi import requests
import json
from colorama import Fore, Style
from .headers import base_headers

def get_task_types(auth_token, get_tasks_url):
    get_tasks_payload = {"country": "", "p": False}
    headers = base_headers.copy()
    headers["authorization"] = auth_token
    try:
        response = requests.post(get_tasks_url, json=get_tasks_payload, headers=headers, impersonate="chrome120")
        if response.status_code == 200:
            data = response.json()
            tasks = data.get("result", {}).get("data", [])
            return [task["type"] for task in tasks]
        else:
            print(f"{Fore.RED}Gagal mengambil tasks, status: {response.status_code}{Style.RESET_ALL}")
            return []
    except Exception as e:
        print(f"{Fore.RED}Error saat mengambil tasks: {str(e)}{Style.RESET_ALL}")
        return []