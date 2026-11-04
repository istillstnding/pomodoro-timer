#!/usr/bin/env python3

import time
import os
import subprocess

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_str = f"{mins:02d}:{secs:02d}"

        os.system('clear')
        columns, lines = os.get_terminal_size()

        big_text = subprocess.check_output(["figlet", "-f", "standard", timer_str]).decode("utf-8")
        big_lines = big_text.splitlines()

        top_pad = (lines - len(big_lines)) // 2
        print("\n" * top_pad, end="")

        for line in big_lines:
            print(line.center(columns))

        time.sleep(1)
        seconds -= 1
    print()


def send_notification(title, message):
    try:
        subprocess.run(["notify-send", "-u", "critical", title, message])
        print("\a", end="", flush=True)
    except FileNotFoundError:
        pass

try:
    os.system('clear')
    
    
    while True:
        try:
            mode = int(input("1. 50 work + 10 rest\n2. 30 work + 5 rest\nChoose your mode: "))
            if mode in (1, 2):
                break
            print("Please enter 1 or 2!")
        except ValueError:
            print("Please enter a valid number!")

    if mode == 1:
        work_sec, rest_sec = 3000, 600
    else:
        work_sec, rest_sec = 1800, 300

    while True:
        send_notification("🍅 Pomodoro", "Time to work!")
        countdown(work_sec)

        send_notification("☕ Rest!", "Time to rest!")
        countdown(rest_sec)

        input("\nPress Enter to start next cycle (or Ctrl+C to exit)...")

except KeyboardInterrupt:
    os.system('clear')
    print("\nTimer was stopped ")
