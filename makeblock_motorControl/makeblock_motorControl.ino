#include "MeOrion.h"
#include <Wire.h>
//#include <Stream.h>
#include <SoftwareSerial.h>

MeEncoderMotor rightMotor(0x09, SLOT1);
MeEncoderMotor leftMotor(0x09, SLOT2);

uint16_t rightSpeed = 0;
uint16_t leftSpeed = 0;
boolean speedUpdate = false;


void serialEvent()
{
  char* opCode;
  Serial.readBytes(opCode, 1);

  //if(opCode[0] == '$')
  //{

  //char opCode[1];
  //Serial.readBytes(opCode,1);

  switch (int(opCode[0]))
  {
    // Set right wheel
    case (int('R')):
      Serial.readBytes((char*)(&rightSpeed), 2);
      speedUpdate = true;
      break;

    // Set left wheel
    case (int('L')):
      Serial.readBytes((char*)(&leftSpeed), 2);
      speedUpdate = true;
      break;

    // Set both wheels
    case (int('B')):
      Serial.readBytes((char*)(&rightSpeed), 2);
      leftSpeed = rightSpeed;
      speedUpdate = true;
      break;

    case (int('S')):
      leftSpeed = 0;
      rightSpeed = 0;
      speedUpdate = true;
      break;

  }

  //}


}

void setup()
{
  // put your setup code here, to run once:
  rightMotor.begin();
  leftMotor.begin();
  Serial.begin(9600);
  int16_t rightSpeed = 0;
  int16_t leftSpeed = 0;

}

void loop()
{

  /*char* opCode;
    Serial.readBytes(opCode,1);

    switch(int(*opCode))
    {
     // Set right wheel
     case(int('R')):
     Serial.readBytes((char*)(&rightSpeed), 2);
     speedUpdate = true;
     break;

     // Set left wheel
     case(int('L')):
     Serial.readBytes((char*)(&leftSpeed), 2);
     speedUpdate = true;
     break;

     // Set both wheels
     case(int('B')):
     Serial.readBytes((char*)(&rightSpeed), 2);
     leftSpeed = rightSpeed;
     speedUpdate = true;
     break;

     case(int('S')):
     leftSpeed = 0;
     rightSpeed = 0;
     speedUpdate = true;
     break;

    }*/

  // put your main code here, to run repeatedly:
  if (speedUpdate)
  {
    /*Serial.println("Speed data: ");
      Serial.println(rightSpeed);
      Serial.println(" ");
      Serial.println(leftSpeed);*/
      if (rightSpeed == 0 && leftSpeed == 0) {
        rightMotor.reset();
        leftMotor.reset();

          /**
          rightMotor.runSpeed(0.0);
          leftMotor.runSpeed(0.0);
          */
      }
     else {
    float normalizedRightSpeed = -((float)rightSpeed * 100.0 / 32768.0);
    float normalizedLeftSpeed = ((float)leftSpeed * 100.0 / 32768.0);
    rightMotor.runSpeed(normalizedRightSpeed);
    leftMotor.runSpeed(normalizedLeftSpeed);
     }
    speedUpdate = false;
  }

}

