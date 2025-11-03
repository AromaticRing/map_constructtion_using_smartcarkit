import serial
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import math

# === Serial Settings ===
PORT = "/dev/ttyACM0"   # Change if needed
BAUD = 9600

# === Grid Parameters ===
CELL_SIZE = 5           # cm per cell (finer resolution)
MAX_DISTANCE_CM = 200
num_cells_side = int(MAX_DISTANCE_CM / CELL_SIZE)
GRID_WIDTH = num_cells_side * 2 + 1
GRID_HEIGHT = num_cells_side * 2 + 1

carX = GRID_WIDTH // 2
carY = GRID_HEIGHT // 2

grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))

# === Initialize Serial ===
ser = serial.Serial(PORT, BAUD, timeout=1)

# === Setup Live Plot ===
plt.ion()
fig, ax = plt.subplots(figsize=(6, 6))

try:
    while True:
        line = ser.readline().decode().strip()
        if not line:
            continue

        try:
            angle_str, distance_str = line.split(",")
            angle = float(angle_str)
            distance = float(distance_str)

            if distance < 2 or distance > MAX_DISTANCE_CM:
                continue

            # Convert to Cartesian coordinates
            rad = math.radians(angle)
            obsX = int(round((distance * math.cos(rad)) / CELL_SIZE))
            obsY = int(round((distance * math.sin(rad)) / CELL_SIZE))

            gridX = carX + obsX
            gridY = carY + obsY

            # Draw the line (free space)
            steps = int(distance / CELL_SIZE)
            for s in range(steps):
                x = carX + int((s * math.cos(rad)))
                y = carY + int((s * math.sin(rad)))
                if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                    grid[y][x] = 0.5  # free path (light blue)

            # Mark obstacle point
            if 0 <= gridX < GRID_WIDTH and 0 <= gridY < GRID_HEIGHT:
                grid[gridY][gridX] = 1.0  # obstacle (red)

            # Update visualization
            ax.clear()
            ax.imshow(grid, cmap="coolwarm", origin="lower")
            ax.plot(carX, carY, "go")  # car position
            ax.set_title("Lab 8: Ultrasonic Mapping (Colored Occupancy Grid)")
            plt.draw()
            plt.pause(0.05)

        except ValueError:
            continue

except KeyboardInterrupt:
    np.savetxt("lab8_map.csv", grid, fmt="%.1f", delimiter=",")
    print("\nMap saved to lab8_map.csv")
    ser.close()
    plt.close(fig)
