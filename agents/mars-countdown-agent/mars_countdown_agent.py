# mars_countdown_agent.py

import time

def start_countdown():
    for i in range(10, 0, -1):
        print(f"Mars Countdown: {i}")
        time.sleep(1)
    print("Liftoff to Mars!")

if __name__ == "__main__":
    start_countdown()
