import schedule
import time
from src.main import main

def schedule_tasks():
    # Schedule the main task to run every hour
    schedule.every().hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_tasks()
