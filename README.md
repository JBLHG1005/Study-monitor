# Study-monitor
A lightweight Python command-line study timer and progress tracker that logs focus sessions by subject and generates study habit summaries.
# Study Timer & Monitor

A lightweight, command-line study timer and productivity tracker built in Python. This tool helps students stay focused using customizable countdown sessions, automatically logs completed study blocks, and breaks down total study hours by subject.

## Key Features
* **Custom Focus Timer:** Set timed study sessions for specific subjects or modules with a live terminal countdown.
* **Automatic Session Logging:** Saves completed sessions with timestamps to a local JSON file (`sessions.json`) so progress persists between runs.
* **Subject Breakdown:** Aggregates total minutes and hours studied per module, sorted from most to least studied.
* **Safe Cancellation:** Gracefully handles accidental interrupts (`Ctrl+C`) without logging incomplete sessions.
* **Zero External Dependencies:** Built entirely using Python's standard library (`json`, `os`, `time`, `datetime`).

## Project Structure
```text
study-monitor/
├── study.py         # Main CLI application and timer logic
├── sessions.json    # Auto-generated local storage for completed sessions
└── README.md        # Project documentation
```

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd study-monitor
   ```

2. **Run the application (Requires Python 3.8+):**
   ```bash
   python study.py
   ```

## Example Usage

```text
=== Study Timer & Monitor ===
1. Start a study session
2. View study summary
3. Exit
Choose an option (1-3): 2

--- Study Summary ---
• Computer Science: 90 mins (1.5 hrs)
• Mathematics: 25 mins (0.4 hrs)
---------------------
Total Time: 115 mins (1.9 hrs)
```

## Author
* [@JBLHG1005](https://github.com)
