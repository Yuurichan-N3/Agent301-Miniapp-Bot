from colorama import Fore, Style

def read_auth_tokens():
    auth_tokens = []
    try:
        with open('data.txt', 'r') as file:
            auth_tokens = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}File data.txt tidak ditemukan. Pastikan file ada dan berisi autentikasi yang valid.{Style.RESET_ALL}")
        exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error saat membaca data.txt: {str(e)}{Style.RESET_ALL}")
        exit(1)
    return auth_tokens