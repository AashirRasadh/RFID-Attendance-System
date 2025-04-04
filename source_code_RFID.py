from mfrc522 import SimpleMFRC522
import time
import datetime

# Initialize RFID Reader
reader = SimpleMFRC522()

# Database of known users (RFID_UID: Name)
users_db = {
    1028202438192: "Aashir",
    76028803954: "Abdul Basith"
}

# Path to attendance log file
log_file = "attendance_log.txt"

print("?? RFID Attendance System Ready")

try:
    while True:
        print("?? Please scan your RFID card...")
        rfid_uid, _ = reader.read()
        
        # Clean UID
        rfid_uid = int(rfid_uid)
        
        # Get current time
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        if rfid_uid in users_db:
            name = users_db[rfid_uid]
            print(f"\n?? Welcome, {name}!")
            print(f"?? Arrival time: {timestamp}")
            print(f"? Attendance recorded for {name}\n")

            # Save to log file
            with open(log_file, "a") as file:
                file.write(f"{timestamp} - {name} (RFID: {rfid_uid})\n")
        else:
            print(f"\n? Unknown RFID: {rfid_uid}")
            print("?? Access Denied!\n")

        time.sleep(2)  # Avoid double scans

except KeyboardInterrupt:
    print("\n?? Program stopped.")

finally:
    reader.GPIO.cleanup()
