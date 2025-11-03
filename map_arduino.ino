#include <NewPing.h>
#include <Servo.h>
#include <math.h>

// === Ultrasonic Sensor ===
#define TRIG_PIN A5
#define ECHO_PIN A4
#define MAX_DISTANCE 200   // cm

NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

// === Servo ===
#define SERVO_PIN 3
Servo servo;

// === Mapping Parameters ===
#define CELL_SIZE 20      // cm per grid cell
#define MIN_DISTANCE 2    // cm
#define STEP_ANGLE 10     // degrees per sweep step

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO_PIN);

  Serial.println("Starting scan...");
  delay(1000);
}

void loop() {
  // Sweep left-to-right
  for (int angle = 0; angle <= 180; angle += STEP_ANGLE) {
    servo.write(angle);
    delay(200); // allow servo to reach position
    int distance = sonar.ping_cm();

    if (distance == 0) distance = MAX_DISTANCE;
    if (distance < MIN_DISTANCE) distance = MIN_DISTANCE;
    if (distance > MAX_DISTANCE) distance = MAX_DISTANCE;

    // Send angle and distance to Raspberry Pi
    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }

  // Sweep right-to-left
  for (int angle = 180; angle >= 0; angle -= STEP_ANGLE) {
    servo.write(angle);
    delay(200);
    int distance = sonar.ping_cm();

    if (distance == 0) distance = MAX_DISTANCE;
    if (distance < MIN_DISTANCE) distance = MIN_DISTANCE;
    if (distance > MAX_DISTANCE) distance = MAX_DISTANCE;

    Serial.print(angle);
    Serial.print(",");
    Serial.println(distance);
  }
}
