#include <Arduino.h>
#include "trigger_gun.h"

void buildTrigger(void){
    pinMode(PIN_TRIGGER, INPUT_PULLUP);
}
bool readTrigger(void){
    return digitalRead(PIN_TRIGGER);
}