from colorama import Fore, Style

def check_empty_tokens(auth_tokens):
    if not auth_tokens:
        print(f"{Fore.RED}Tidak ada token autentikasi yang valid di data.txt. Program berhenti.{Style.RESET_ALL}")
        exit(1)