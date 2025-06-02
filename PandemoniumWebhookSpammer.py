import requests
import json
import os
import time
import threading
import re
from concurrent.futures import ThreadPoolExecutor

class Colors:
    # Main UI / Title / Input
    RICH_CYAN = '\033[38;5;51m'  # Deep glowing cyan

    # Status Messages
    NEON_GREEN = '\033[38;5;46m'   # Bright green
    RED = '\033[38;5;196m'        # Vivid red
    YELLOW = '\033[38;5;226m'     # Bright yellow
    PALE_BLUE = '\033[38;5;117m'  # Soft light blue
    ORANGE = '\033[38;5;202m'     # Orange for warnings

    RESET = '\033[0m'

# Set Console Title
os.system('title Pandemonium Webhook Spammer | https://discord.com/invite/HazvsVHxyE')

def print_boxed_title():
    banner = f"""
{Colors.RICH_CYAN}┌───────────────────────────────────────────────┐{Colors.RESET}
{Colors.RICH_CYAN}│                                               │{Colors.RESET}
{Colors.RICH_CYAN}│         Welcome to Pandemonium Webhook        │{Colors.RESET}
{Colors.RICH_CYAN}│                    Spammer                    │{Colors.RESET}
{Colors.RICH_CYAN}│                                               │{Colors.RESET}
{Colors.RICH_CYAN}└───────────────────────────────────────────────┘{Colors.RESET}
    """
    print(banner)

FOOTER_LINK = "https://discord.com/invite/HazvsVHxyE"

def validate_webhook(url):
    pattern = r"^https:\/\/discord\.com\/api\/webhooks\/\d+\/.+"
    return re.match(pattern, url) is not None

def send_webhook_message(webhook_url, message, username=None, avatar_url=None, max_retries=5, backoff_factor=0.5):
    embed = {
        "description": f"Sent using [Pandemonium Webhook Spammer]({FOOTER_LINK})",
        "color": 35723  # Discord-compatible dark cyan
    }

    data = {
        "content": message,
        "embeds": [embed],
        "username": username or "Pandemonium Webhook Spammer",
        "avatar_url": avatar_url or "https://cdn.discordapp.com/attachments/1377890116328099854/1377890244053045259/Pandemonium.png?ex=683a9bca&is=68394a4a&hm=32e4632fdb6f463879460be3cf4ca46cf0dc59e3f13b4168ba3f7bc2cd9a5fde&"
    }

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(
                webhook_url,
                data=json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 204:
                print(f"{Colors.NEON_GREEN}[+] Message sent successfully!{Colors.RESET}")
                return True

            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After')
                wait_time = float(retry_after) if retry_after else (backoff_factor * attempt)
                print(f"{Colors.ORANGE}[!] Rate limited. Retrying in {wait_time:.2f}s (Attempt {attempt}/{max_retries}){Colors.RESET}")
                time.sleep(wait_time)

            else:
                print(f"{Colors.RED}[-] Unexpected status code: {response.status_code}{Colors.RESET}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}[!] Connection error: {str(e)}{Colors.RESET}")
            if attempt < max_retries:
                wait_time = backoff_factor * attempt
                print(f"{Colors.YELLOW}[*] Retrying in {wait_time:.2f}s (Attempt {attempt+1}/{max_retries}){Colors.RESET}")
                time.sleep(wait_time)
            else:
                print(f"{Colors.RED}[X] Failed after {max_retries} attempts.{Colors.RESET}")
                return False

    print(f"{Colors.RED}[X] Max retries reached. Message failed.{Colors.RESET}")
    return False

def get_user_input():
    webhook_url = input(f"[?]{Colors.RICH_CYAN} Enter Webhook URL >>> {Colors.RESET}")
    if not validate_webhook(webhook_url):
        print(f"{Colors.RED}[!] Invalid webhook URL format!{Colors.RESET}")
        return None

    message = input(f"[?]{Colors.RICH_CYAN} Message to Spam >>> {Colors.RESET}")
    if not message:
        print(f"{Colors.RED}[!] Message cannot be empty.{Colors.RESET}")
        return None

    username = input(f"[?]{Colors.RICH_CYAN} Custom Username (optional, press Enter to skip) >>> {Colors.RESET}")

    avatar_url = input(f"[?]{Colors.RICH_CYAN} Custom Avatar URL (optional, press Enter to skip) >>> {Colors.RESET}")

    mode = input(f"[?]{Colors.RICH_CYAN} Mode [1=Fixed, 2=Infinite]: {Colors.RESET}")
    if mode not in ['1', '2']:
        print(f"{Colors.RED}[!] Invalid mode selected.{Colors.RESET}")
        return None

    iterations = 0
    if mode == '1':
        try:
            iterations = int(input(f"[?]{Colors.RICH_CYAN} Number of Messages to Send >>> {Colors.RESET}"))
            if iterations <= 0:
                print(f"{Colors.RED}[!] Please enter a positive number.{Colors.RESET}")
                return None
        except ValueError:
            print(f"{Colors.RED}[!] Invalid input for iterations.{Colors.RESET}")
            return None
    else:
        iterations = float('inf')  # Infinite loop

    print(f"\n{Colors.PALE_BLUE}[INFO] Recommended Thread Count: 1–10 (Higher may cause rate limiting){Colors.RESET}")
    try:
        threads = int(input(f"[?]{Colors.RICH_CYAN} Number of Threads (e.g., 5) >>> {Colors.RESET}"))
        if threads <= 0:
            print(f"{Colors.RED}[!] Threads must be greater than zero.{Colors.RESET}")
            return None
    except ValueError:
        print(f"{Colors.RED}[!] Invalid thread count.{Colors.RESET}")
        return None

    print(f"\n{Colors.PALE_BLUE}[INFO] Recommended delay to avoid rate limit: 0.5 seconds{Colors.RESET}")
    delay = float(input(f"[?]{Colors.RICH_CYAN} Delay Between Requests (seconds): {Colors.RESET}"))

    return {
        "webhook_url": webhook_url,
        "message": message,
        "mode": mode,
        "iterations": iterations,
        "threads": threads,
        "delay": delay,
        "username": username,
        "avatar_url": avatar_url
    }

def start_spam(config):
    webhook_url = config["webhook_url"]
    message = config["message"]
    total_iterations = config["iterations"]
    num_threads = config["threads"]
    delay = config["delay"]
    username = config["username"]
    avatar_url = config["avatar_url"]

    print(f"\n{Colors.NEON_GREEN}[*] Starting spam attack...{Colors.RESET}")
    print(f"{Colors.PALE_BLUE}Webhook URL: {webhook_url}{Colors.RESET}")
    print(f"{Colors.PALE_BLUE}Message: {message}{Colors.RESET}")
    print(f"{Colors.PALE_BLUE}Threads: {num_threads}{Colors.RESET}")
    print(f"{Colors.PALE_BLUE}Delay: {delay}s{Colors.RESET}")
    print("-" * 50)

    count = [0]
    lock = threading.Lock()
    stop_flag = [False]

    def spam_task():
        while True:
            with lock:
                if count[0] >= total_iterations:
                    return
                count[0] += 1
            success = send_webhook_message(webhook_url, message, username, avatar_url)
            if not success:
                print(f"{Colors.PALE_BLUE}[DEBUG] Message failed after retries.{Colors.RESET}")
            time.sleep(delay)
            if stop_flag[0]:
                return

    def keyboard_listener():
        try:
            input()
            stop_flag[0] = True
            print(f"\n{Colors.RED}[*] Stopping spammer...{Colors.RESET}")
        except:
            pass

    listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
    listener_thread.start()

    try:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(spam_task) for _ in range(num_threads)]
            for future in futures:
                future.result()
    except KeyboardInterrupt:
        stop_flag[0] = True
        print(f"\n{Colors.RED}[*] Keyboard interrupt detected. Stopping...{Colors.RESET}")

    print(f"{Colors.NEON_GREEN}[+] Spamming completed. Total messages sent: {count[0]}{Colors.RESET}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_boxed_title()

        config = get_user_input()
        if config:
            start_spam(config)
        else:
            print(f"{Colors.RED}[!] Failed to start spammer due to invalid input.{Colors.RESET}")

        restart = input(f"\n{Colors.RICH_CYAN}[?] Would you like to restart Pandemonium? [y/n] → {Colors.RESET}").strip().lower()
        if restart != 'y':
            print(f"{Colors.NEON_GREEN}[*] Exiting... Thank you for using Pandemonium.{Colors.RESET}")
            break

if __name__ == "__main__":
    main()