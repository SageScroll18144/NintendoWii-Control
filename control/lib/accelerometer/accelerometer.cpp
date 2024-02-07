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

char sideAxis(void){
    char ans = 'E';
    if (accel.available()) {      
        // if (accel.isRight()) ans = 'R';
        // else if (accel.isLeft()) ans = 'L';
        // else if (accel.isUp()) ans = 'U';
        // else if (accel.isDown()) ans = 'D';
        // else if (accel.isFlat()) ans = 'F';

        if(accel.getCalculatedY() <= -0.1) ans =  'L';
        else if(accel.getCalculatedY() > 0.49) ans =  'R';
        else if(accel.getCalculatedZ() <= 0.20) ans =  'D';
        else if(accel.getCalculatedZ() >= 0.80) ans =  'U';     
        else ans = 'F';
    }

    return ans;
}

float getAxisY(void){
    return accel.getCalculatedY();
}

float getAxisZ(void){
    return accel.getCalculatedZ();
}


void debugAxis(void){
    Serial.print("getX() | getY() | getZ(): "); Serial.print(accel.getX()); Serial.print(" "); Serial.print(accel.getY()); Serial.print(" "); Serial.println(accel.getZ());
    Serial.print("getCalculatedX() | getCalculatedY() | getCalculatedZ(): "); Serial.print(accel.getCalculatedX()); Serial.print(" "); Serial.print(accel.getCalculatedY()); Serial.print(" "); Serial.println(accel.getCalculatedZ());
}