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
        if (accel.isDown()) ans = 'R';
        else if (accel.isUp()) ans = 'L';
        else if (accel.isRight()) ans = 'U';
        else if (accel.isLeft()) ans = 'D';
        else if (accel.isFlat()) ans = 'F';
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
    Serial.println(digitalRead(32));
    Serial.print("getX() | getY() | getZ(): "); Serial.print(accel.getX()); Serial.print(" "); Serial.print(accel.getY()); Serial.print(" "); Serial.println(accel.getZ());
    Serial.print("getCalculatedX() | getCalculatedY() | getCalculatedZ(): "); Serial.print(accel.getCalculatedX()); Serial.print(" "); Serial.print(accel.getCalculatedY()); Serial.print(" "); Serial.println(accel.getCalculatedZ());
}