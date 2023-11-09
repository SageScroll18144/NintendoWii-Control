#include <Arduino.h>
#include "accelerometer.h"
#include "device_state.h"
#include "trigger_gun.h"

void setup() {
  Serial.begin(115200);
  buildAccelerometer();
  buildTrigger();
}

void loop() {
  send_packet(getAxis(), readTrigger());
}