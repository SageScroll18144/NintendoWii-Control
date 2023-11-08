#include <Arduino.h>
#include "trigger.h"

void buildTrigger(void){
    pinMode(PIN_TRIGGER, INPUT_PULLUP);
}
bool readTrigger(void){
    return !digitalRead(PIN_TRIGGER);
}