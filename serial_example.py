import serial
import time

# === Configure your serial port and baudrate ===
# Change 'COM3' to the port where your Arduino is connected
# For Linux/Mac, it would be like '/dev/ttyUSB0' or '/dev/ttyACM0'
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

# === Open serial connection ===
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for Arduino to reset
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baudrate.")
except Exception as e:
    print(f"Error connecting to serial port: {e}")
    exit()

# === Function to send a message ===
def send_message(message):
    if arduino.is_open:
        # Encode the message to bytes and send it
        arduino.write((message + '\n').encode('utf-8'))
        print(f"Sent: {message}")
    else:
        print("Serial port is not open!")

# === Example usage ===
try:
    while True:
        msg = input("Enter message to send (or type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        send_message(msg)
except KeyboardInterrupt:
    print("\nExiting program...")

# === Close serial connection ===
arduino.close()
print("Serial port closed.")