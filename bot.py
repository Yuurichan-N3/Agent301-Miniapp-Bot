from colorama import init
from core.tasks import get_task_types
from core.complete import complete_task
from core.api import get_tasks_url, complete_task_url
from utils.file_reader import read_auth_tokens
from utils.logger import log_account_processing, log_no_tasks, log_task_request, log_account_done, log_all_done
from utils.sleeper import sleep_between_tasks, sleep_between_accounts
from utils.error_handler import check_empty_tokens
from utils.banner import display_banner

init()

display_banner()

auth_tokens = read_auth_tokens()
check_empty_tokens(auth_tokens)

for idx, auth_token in enumerate(auth_tokens, 1):
    log_account_processing(idx)
    task_types = get_task_types(auth_token, get_tasks_url)
    if not task_types:
        log_no_tasks(idx)
        continue
    for task_type in task_types:
        log_task_request(task_type, idx)
        complete_task(complete_task_url, task_type, auth_token)
        sleep_between_tasks()
    log_account_done(idx)
    sleep_between_accounts()

log_all_done()
