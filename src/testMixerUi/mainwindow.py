# File: main.py
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import *
import json
import serial
import threading


sliders = {}


def send_to_serial(values):
    """Encodes slider values to JSON and sends them to the serial port."""
    json_data = json.dumps(values)
    try:
        ser.write(json_data.encode('utf-8'))
        print(f"Sent to serial: {json_data}")
    except Exception as e:
        print(f"Error sending to serial: {e}")

def display_json_values(json_data):
    """Displays incoming JSON values in a separate label widget and updates slider colors."""
    try:
        data = json.loads(json_data)
        if len(data) != 8:
            print("Error: JSON must contain exactly 8 values.")
            return

        #for key, value in data.items():
        #    slider_index = int(key) - 1


        levelBar1.setValue(data["1"]*1000)
        levelBar2.setValue(data["2"]*1000)
        print(data["2"]*1000)

        #print(f"Displayed JSON values: {data}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON input: {e}")
    except ValueError as e:
        print(f"Error processing JSON data: {e}")

def read_serial():
    """Reads data from the serial port and updates the GUI."""
    while True:
        try:
            if ser.in_waiting > 0:
                #print(ser.readline().decode('utf-8').strip())
                json_data = ser.readline().decode('utf-8').strip()
                display_json_values(json_data)
        except Exception as e:
            print(f"Error reading from serial: {e}")





def dialInput():
    value = dial.value()


def faderChanged():
    value1 = fader1.value()
    value2 = fader2.value()
    value3 = fader3.value()

    values = {str(1): float(value1), str(2): float(value2), str(3): float(value3), str(4): 0.0, str(5): 0.0, str(6): 0.0, str(7): 0.0, str(8): 0.0}
    send_to_serial(values)

    def exit():

        sys.exit()

def setupW():
    window.hide()
    routingWindow.hide()
    mixesWindow.hide()
    overviewWindow.hide()
    setupWindow.show()

def mainW():
    setupWindow.hide()
    window.show()

def routingW():
    setupWindow.hide()
    routingWindow.show()

def mixesW():
    setupWindow.hide()
    mixesWindow.show()

def overviewW():
    setupWindow.hide()
    overviewWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    setupWindow = loader.load("setup.ui")
    setupWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    setupWindow.hide()

    routingWindow = loader.load("routingwindow.ui")
    routingWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    routingWindow.hide()


    mixesWindow = loader.load("mixes.ui")
    mixesWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    mixesWindow.hide()

    overviewWindow = loader.load("overview.ui")
    overviewWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    overviewWindow.hide()

    window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    dial = window.dial
    dial.valueChanged.connect(lambda: dialInput())

    fader1 = overviewWindow.Fader1
    fader1.valueChanged.connect(lambda: faderChanged())

    fader2 = overviewWindow.Fader2
    fader2.valueChanged.connect(lambda: faderChanged())

    fader3 = overviewWindow.Fader3
    fader3.valueChanged.connect(lambda: faderChanged())

    levelBar1 = overviewWindow.levelBar1
    levelBar2 = overviewWindow.levelBar2

    quitButton = setupWindow.quit
    quitButton.released.connect(lambda: exit())


    setupButton = window.pushButton

    setupButton.released.connect(lambda: setupW())


    mainButton = setupWindow.mainButton

    mainButton.released.connect(lambda: mainW())

    routingButton = setupWindow.routingButton

    routingButton.released.connect(lambda: routingW())

    routingWindow.setupButton.released.connect(lambda: setupW())

    mixesButton = setupWindow.mixesButton

    mixesButton.released.connect(lambda: mixesW())

    mixesWindow.setupButton.released.connect(lambda: setupW())

    overviewButton = setupWindow.overviewButton

    overviewButton.released.connect(lambda: overviewW())

    overviewWindow.setupButton.released.connect(lambda: setupW())

    print(dial.value())
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()


    app.setStyle('Plastique')


    try:
        ser = serial.Serial('COM11', 9600, timeout=1)  # Update COM11 as needed
    except Exception as e:
        print(f"Failed to open serial port: {e}")



    # Start a thread to read from the serial port
    serial_thread = threading.Thread(target=read_serial, daemon=True)
    serial_thread.start()



    sys.exit(app.exec())
