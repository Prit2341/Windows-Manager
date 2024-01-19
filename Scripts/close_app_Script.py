import time
import psutil
import ctypes
from plyer import notification  # Install plyer library: pip install plyer

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("dwTime", ctypes.c_ulong)]

def get_last_input_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0

def close_inactive_apps(target_inactive_duration_minutes):
    time.sleep(target_inactive_duration_minutes * 60)
    notification.notify(
        title="Auto Close App",
        message=f"System will close inactive apps now.",
        timeout=10
    )

    while True:
        try:
            for process in psutil.process_iter(['pid', 'name', 'create_time']):
                create_time = process.info['create_time']
                current_time = time.time()
                elapsed_time = current_time - create_time
                elapsed_minutes = elapsed_time / 60

                if elapsed_minutes >= target_inactive_duration_minutes:
                    process_name = process.info['name']
                    pid = process.info['pid']
                    if pid != 0:  # Exclude System Idle Process
                        print(f"Closing {process_name} (PID: {pid}) after {target_inactive_duration_minutes} minutes of inactivity.")
                        psutil.Process(pid).terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

        # Check for user inactivity
        if get_last_input_time() > target_inactive_duration_minutes * 60:
            print(f"No user activity detected for {target_inactive_duration_minutes} minutes. Closing inactive apps.")
            ctypes.windll.user32.LockWorkStation()  # Lock the workstation
            time.sleep(5)  # Allow time for the system to lock before terminating processes
            ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)  # Log off the user

        time.sleep(10)  # Adjust the interval as needed
