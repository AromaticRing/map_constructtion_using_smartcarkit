# 🗺️ Ultrasonic Mapping System using Arduino & Raspberry Pi

## 📘 Project Overview
This project implements a **real-time ultrasonic mapping system** using an **Arduino microcontroller** and a **Raspberry Pi**.  
The Arduino continuously measures distances using an **ultrasonic sensor** mounted on a servo motor, scanning the environment and transmitting distance–angle data to the Raspberry Pi via serial communication.  
The Raspberry Pi then processes this data and visualizes it as a **2D occupancy grid map** in real-time using Python and Matplotlib.

---

## 🧩 Components Used

### 🛠️ Hardware
- Arduino Uno (or compatible)
- Raspberry Pi (any model with Python & serial support)
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor
- Jumper Wires
- Breadboard
- USB Cable (for serial communication)

### 💻 Software
- Arduino IDE
- Python 3.x (on Raspberry Pi)
- Required Python Libraries:
  ```bash
  pip install numpy matplotlib pyserial
⚙️ System Architecture
Module	Function
Arduino (map_arduino.ino)	Controls the ultrasonic sensor and servo motor, collects distance readings, and sends formatted data (angle,distance) to the Raspberry Pi.
Raspberry Pi (map_rpi_program.py)	Reads serial data from the Arduino, converts polar coordinates to Cartesian coordinates, and displays a real-time occupancy grid map showing detected obstacles and free space.

🚀 How It Works
1️⃣ Arduino Side — Environment Scanning
The servo rotates the ultrasonic sensor from 0° to 180°.

For each angle, the ultrasonic sensor measures the distance to the nearest obstacle.

The Arduino sends the data in this format:

matlab
Copy code
angle,distance
Example:

Copy code
90,56.78
2️⃣ Raspberry Pi Side — Map Visualization
The Raspberry Pi listens to the serial port (default: /dev/ttyACM0).

It converts the received data to Cartesian coordinates and updates a colored occupancy grid:

🔴 Red cells: Obstacles

🔵 Blue cells: Free space

🟢 Green point: Vehicle/sensor position

The map updates dynamically as new data arrives.

When stopped (Ctrl + C), the final map is saved as lab8_map.csv.

🧠 Code Explanation
map_arduino.ino
Initializes servo and ultrasonic pins.

Rotates the servo incrementally across the scanning range.

For each angle:

Triggers the ultrasonic sensor.

Calculates the distance.

Sends angle and distance to the serial monitor.

map_rpi_program.py
Opens a serial connection with the Arduino.

Continuously reads and parses data.

Converts polar coordinates (angle, distance) → Cartesian (x, y).

Plots an occupancy grid using Matplotlib in real-time.

Saves the final map to a .csv file when the program ends.

🧪 Running the Project
Step 1: Setup Arduino
Open map_arduino.ino in Arduino IDE.

Connect the Arduino via USB and upload the sketch.

Ensure the correct COM port is selected.

Step 2: Setup Raspberry Pi
Copy map_rpi_program.py to your Raspberry Pi.

Connect the Arduino to Raspberry Pi via USB.

Run the following command:

bash
Copy code
python3 map_rpi_program.py
A live visualization window will appear.

Press Ctrl + C to stop and save the map to lab8_map.csv.

🖼️ Output Example
Live View
Real-time occupancy grid visualization with car position and obstacle markings.

Saved Output
A CSV file representing the final grid map.

📹 Demonstration Video
📺 YouTube Demo: https://youtu.be/your-video-link

👨‍💻 Authors
Developed by:

Anshul Dewangan

Pratyaksh Lodhi

Aaron David Don

Joshua Benchamin

🪪 License
This project is released under the MIT License — feel free to use and modify it with proper attribution.
