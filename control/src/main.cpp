#include <Wire.h>                 // Must include Wire library for I2C
#include "SparkFun_MMA8452Q.h"    // Click here to get the library: http://librarymanager/All#SparkFun_MMA8452Q

MMA8452Q accel;                   // create instance of the MMA8452 class

void setup() {
  Serial.begin(9600);
  Serial.println("MMA8452Q Orientation Test Code!");
  Wire.begin();

  if (accel.begin() == false) {
    Serial.println("Not Connected. Please check connections and read the hookup guide.");
    while (1);
  }
}

void loop() {
  if (accel.available()) {      // Wait for new data from accelerometer
    // Orientation of board (Right, Left, Down, Up);
    if (accel.isRight() == true) {
      Serial.println("Right");
    }
    else if (accel.isLeft() == true) {
      Serial.println("Left");
    }
    else if (accel.isUp() == true) {
      Serial.println("Up");
    }
    else if (accel.isDown() == true) {
      Serial.println("Down");
    }
    else if (accel.isFlat() == true) {
      Serial.println("Flat");
    }
  }
}