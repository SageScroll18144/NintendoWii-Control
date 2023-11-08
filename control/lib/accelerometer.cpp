#include <Arduino.h>
#include <Wire.h> 
#include "accelerometer.h"
#include "SparkFun_MMA8452Q.h"

MMA8452Q accel;   

void buildAccelerometer(void){
    Serial.println("MMA8452Q Orientation Test Code!");
    Wire.begin();

    if (accel.begin() == false) {
        Serial.println("Not Connected. Please check connections and read the hookup guide.");
        while (1);
    }
}

char getAxis(void){
    char ans = -1;
    if (accel.available()) {      
        if (accel.isRight()) ans = 'F';
        else if (accel.isLeft()) ans = 'L';
        else if (accel.isUp()) ans = 'U';
        else if (accel.isDown()) ans = 'D';
        else if (accel.isFlat()) ans = 'F';
    }

    return ans;
}