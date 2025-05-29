from colorama import Fore, Style

def log_account_processing(idx):
    print(f"{Fore.YELLOW}\nMemproses akun {idx}...{Style.RESET_ALL}")

def log_no_tasks(idx):
    print(f"{Fore.RED}Tidak ada task yang ditemukan untuk akun {idx}. Lanjut ke akun berikutnya.{Style.RESET_ALL}")

def log_task_request(task_type, idx):
    print(f"{Fore.CYAN}Memulai pengerjaan tugas untuk jenis: {task_type} (Akun {idx}){Style.RESET_ALL}")

def log_account_done(idx):
    print(f"{Fore.YELLOW}Selesai memproses akun {idx}.{Style.RESET_ALL}")

def log_all_done():
    print(f"{Fore.GREEN}\nSemua akun telah diproses.{Style.RESET_ALL}")
