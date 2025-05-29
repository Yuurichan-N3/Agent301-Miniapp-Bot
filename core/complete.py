from curl_cffi import requests
from colorama import Fore, Style
from .headers import base_headers

def complete_task(url, task_type, auth_token):
    headers = base_headers.copy()
    headers["authorization"] = auth_token
    payload = {"type": task_type}
    try:
        response = requests.post(url, json=payload, headers=headers, impersonate="chrome120")
        if response.status_code == 200:
            print(f"{Fore.GREEN}Berhasil menyelesaikan tugas untuk jenis: {task_type}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Task sudah pernah dikerjakan : {task_type}, status: {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan untuk task: {task_type}: {str(e)}{Style.RESET_ALL}")
