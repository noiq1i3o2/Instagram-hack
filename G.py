import time
import random
import sys

VALID_USER = "xxgam_er0"


def slow(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def progress(label, steps=20, speed=(0.05, 0.25)):
    for i in range(steps + 1):
        bar = "█" * i + "░" * (steps - i)
        pct = int(i / steps * 100)
        sys.stdout.write(f"\r{label} [{bar}] {pct}%")
        sys.stdout.flush()
        time.sleep(random.uniform(*speed))
    print()


def fake_install():
    modules = ["igcore", "sessionbypass", "cryptolib-x", "proxyrotator", "tokenfetch"]
    for m in modules:
        slow(f"Installing module: {m} ...", 0.02)
        progress("  Downloading", 15, (0.02, 0.15))
        print(f"  {m} installed successfully.")
        time.sleep(0.3)


def fake_agreements():
    print("\n--- TERMS & AGREEMENTS ---")
    terms = [
        "1. You accept full responsibility for all actions performed.",
        "2. You agree not to share this tool with third parties.",
        "3. You confirm you have permission to access the target.",
    ]
    for t in terms:
        slow(t, 0.02)
        time.sleep(0.4)
    input("\nPress ENTER to accept all agreements... ")


def fake_work(tasks=None):
    tasks = tasks or [
        "Connecting to server",
        "Bypassing security layer",
        "Fetching session token",
        "Decrypting data",
        "Finalizing",
    ]
    for t in tasks:
        progress(t, 20)
        time.sleep(0.2)


def main():
    slow("=== IG TOOL v2.4 ===", 0.04)
    username = input("Enter username: ").strip()

    if username != VALID_USER:
        print("Out of credits. Please try again later.")
        return

    fake_install()
    fake_agreements()
    fake_work()
    print("\nComplete. Successfully located account.\n")

    options = {
        "1": "Delete latest post",
        "2": "Delete latest reel",
        "3": "Delete latest",
        "4": "Delete accounts",
        "5": "Hack accounts",
    }

    print("Choose an action:")
    for k, v in options.items():
        print(f"  [{k}] {v}")

    choice = input("\n> ").strip()

    if choice not in options:
        print("Invalid option.")
        return

    if choice == "5":
        target = input("Which account would you like to give this username to? ").strip()
        fake_work([
            "Locating target account",
            "Injecting payload",
            "Transferring ownership",
            "Verifying changes",
        ])
        print("\nHacking successful. Please check")
        print(f"Username: {target}")
    else:
        fake_work()
        print("\nInstagram account hack successful.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")
   