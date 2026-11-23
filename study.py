import json
import os
import time
from datetime import datetime

DATA_FILE = "sessions.json"


def load_sessions() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_session(subject: str, minutes: int) -> None:
    sessions = load_sessions()
    sessions.append({
        "subject": subject.strip().title(),
        "minutes": minutes,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4)


def start_timer() -> None:
    subject = input("Enter subject or module name: ").strip()
    if not subject:
        print("Subject cannot be empty.")
        return

    try:
        minutes = int(input("Enter study duration in minutes (e.g., 25): "))
        if minutes <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number.")
        return

    print(f"\nStarting {minutes}-minute session for '{subject}'. Press Ctrl+C to cancel.\n")
    total_seconds = minutes * 60

    try:
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            print(f"\rTime Remaining: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)
            total_seconds -= 1

        print("\n\nSession complete! Great work.")
        save_session(subject, minutes)
    except KeyboardInterrupt:
        print("\n\nTimer cancelled. Session was not saved.")


def view_summary() -> None:
    sessions = load_sessions()
    if not sessions:
        print("\nNo study sessions logged yet.")
        return

    totals = {}
    total_minutes = 0

    for entry in sessions:
        subj = entry["subject"]
        mins = entry["minutes"]
        totals[subj] = totals.get(subj, 0) + mins
        total_minutes += mins

    print("\n--- Study Summary ---")
    for subj, mins in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        hours = mins / 60
        print(f"• {subj}: {mins} mins ({hours:.1f} hrs)")
    print(f"---------------------")
    print(f"Total Time: {total_minutes} mins ({total_minutes / 60:.1f} hrs)\n")


def main() -> None:
    while True:
        print("\n=== Study Timer & Monitor ===")
        print("1. Start a study session")
        print("2. View study summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            start_timer()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

