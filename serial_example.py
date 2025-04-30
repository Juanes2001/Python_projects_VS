import serial
import time

# === Configure your serial port and baudrate ===
# Change 'COM3' to the port where your Arduino is connected
# For Linux/Mac, it would be like '/dev/ttyUSB0' or '/dev/ttyACM0'
SERIAL_PORT = 'COM11'
BAUD_RATE = 9600
flag = False

# === Function to send a message ===
def send_message(message):
    global flag
    if arduino.is_open:

        if '@' in message:
            # Encode the message to bytes and send it
            arduino.write((message + '\n').encode('utf-8'))
            print(f"Python: {message}")
            flag = True

        else:
            print("Comando mal copiado, recuerde la terminacion @\n")        
    else:
        print("Serial port is not open!")

def receive_message_init():
    response = ""
    if arduino.is_open:
        while True:
            response += arduino.readline().decode()
            if '||' in response :
                print(f"Arduino: {response.replace("||","")}" )
                break

print("Hola mundo")

def receive_message():
    response = ""
    global flag
    if arduino.is_open:
        while True:
            response += arduino.readline().decode()
            if '\n' in response :
                print(f"Arduino: {response}")
                flag = False
                break


# === Open serial connection ===
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for Arduino to reset
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baudrate.")
    receive_message_init()

except Exception as e:
    print(f"Error connecting to serial port: {e}")
    exit()

# === Example usage ===
try:
    while True:
        msg = input("Enter command to send (or type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        send_message(msg)
        if flag:
            receive_message()


except KeyboardInterrupt:
    print("\nExiting program...")

# === Close serial connection ===
arduino.close()
print("Serial port closed.")