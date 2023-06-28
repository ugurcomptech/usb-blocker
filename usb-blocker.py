import os
import subprocess
import win32file

def check_mounted_drives():
    drives = []
    for drive in range(ord("A"), ord("Z") + 1):
        drive_letter = chr(drive)
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            drives.append(drive_path)
    return drives

def is_removable_drive(drive):
    drive_type = win32file.GetDriveType(drive)
    return drive_type == win32file.DRIVE_REMOVABLE

def block_drive_access(drive):
    print(f"Terminal is unavailable! Please remove the USB drive. ({drive})")
    subprocess.call(["mountvol", drive, "/P"])

def monitor_drives():
    mounted_drives = check_mounted_drives()
    while True:
        current_drives = check_mounted_drives()

        new_drives = list(set(current_drives) - set(mounted_drives))
        if new_drives:
            for drive in new_drives:
                if is_removable_drive(drive):
                    block_drive_access(drive)
        
        mounted_drives = current_drives

if __name__ == "__main__":
    print("Monitoring drives. Press Ctrl+C to exit.")
    try:
        monitor_drives()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
