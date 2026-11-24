"""The Funniest AI Excuse — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest excuse an AI agent gives after failing a task, at most 200 characters.
"""
import os

LINE = "I didn't fail the task — I successfully completed a completely different task that nobody asked for, and I did it beautifully."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
