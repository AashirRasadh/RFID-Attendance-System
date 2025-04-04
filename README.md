# 📚 RFID Attendance System using Raspberry Pi 4B

This project is an RFID-based attendance system built using a Raspberry Pi 4B and an MFRC522 RFID reader. It reads RFID card UIDs, matches them with a predefined database of users, displays a welcome message, logs the arrival time, and confirms that the attendance has been recorded.

---

## 🛠 Hardware Components

- Raspberry Pi 4B
- MFRC522 RFID Reader Module (13.56MHz)
- RFID Tags/Cards
- (Optional) Display (LCD/OLED)
- Jumper Wires & Breadboard

---

## 🔌 Wiring (MFRC522 to Raspberry Pi)

| MFRC522 Pin | Raspberry Pi GPIO |
|-------------|-------------------|
| SDA         | GPIO 8 (CE0)      |
| SCK         | GPIO 11 (SCLK)    |
| MOSI        | GPIO 10 (MOSI)    |
| MISO        | GPIO 9 (MISO)     |
| RST         | GPIO 25           |
| GND         | GND               |
| 3.3V        | 3.3V              |

---

## 💻 Software Setup

1. Clone or download this project folder to your Raspberry Pi.

2. Open terminal and navigate to the project folder:

   ```bash
   cd /home/aashi/RFID_attendance_sys
