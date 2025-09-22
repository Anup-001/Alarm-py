import time
from datetime import datetime
import winsound

def get_current_time():
    return datetime.now().strftime("%H:%M")
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        current_time=get_current_time()
        if current_time==alarm_time:
            print("Wake up! Alarm ringing...")
            winsound.Beep(3000, 3000) 
            break
        time.sleep(3) 
alarm_time= input("Enter alarm time (HH:MM): ")
set_alarm(alarm_time)