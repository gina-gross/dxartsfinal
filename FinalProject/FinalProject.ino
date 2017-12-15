// include the servo library to control the servo
#include <Servo.h> 

Servo myservoL; // create servo object to control a servo 
                 // a maximum of eight servo objects can be created 

Servo myservoR; // create servo object to control a servo 
                 // a maximum of eight servo objects can be created 

int pos = 0; // variable to store the servo position 

// Set up a pin we are going to use to indicate our status using an LED.
int statusPin = LED_BUILTIN; 

const int sensorLeft = A5;
const int sensorRight = A2;

const int outputPinL = 5;
const int outputPinR = 10;

int sensorValL = 0;
int sensorValR = 0;


void setup() {
  // put your setup code here, to run once:
  myservoL.attach(outputPinL);   // attaches the servo on pin 5 (the left servo) to the servo object
  myservoR.attach(outputPinR);   // attached the servo on pin 6 (the right servo) to the servo object
  
  // Begin by setting up the Serial Port so we can output our results.
  Serial.begin(9600);

  // Ready an LED to indicate our status.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(sensorLeft, INPUT_PULLUP);
  pinMode(sensorRight, INPUT_PULLUP); 

}

void loop() {
  // put your main code here, to run repeatedly:

  sensorValL = analogRead(sensorLeft);
  sensorValR = analogRead(sensorRight);
  Serial.println(sensorValL);
  delay(1);

  // left ear

  if(sensorValL < 500 || sensorValR < 500) {
    digitalWrite(LED_BUILTIN, HIGH);
    for (pos = 0; pos <= 180; pos += 1) {    // left ear goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservoL.write(pos);   // tell servo to go to position in 'posL'
      myservoR.write(pos);
      delay(10);              // wait 15ms for servo to reach position
    }
    for (pos = 180; pos >= 0; pos -= 1) {    // left ear goes from 180 to 0 degrees
      myservoL.write(pos);
      myservoR.write(pos);
      delay(10);
    }
 /* } if (sensorValR < 500) {
    for (posR = 0; posR <= 180; posR += 1) {    // right ear goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservoR.write(posR);   // tell servo to go to position in 'posL'
      delay(15);              // wait 15ms for servo to reach position
    }
    for (posR = 180; posR >= 0; posR -= 1) {    // right ear goes from 180 to 0 degrees
      myservoR.write(posR);
      delay(15);
    }
  } if (sensorValL < 500 && sensorValR < 500) {
     for (posR = 0; posR <= 180; posR += 1) {    // right ear goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservoR.write(posR);   // tell servo to go to position in 'posL'
      myservoL.write(posR);
      delay(15);              // wait 15ms for servo to reach position
    }
    for (posR = 180; posR >= 0; posR -= 1) {    // right ear goes from 180 to 0 degrees
      myservoR.write(posR);
      myservoL.write(posR);
      delay(15);
    } */
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    
  }

}
