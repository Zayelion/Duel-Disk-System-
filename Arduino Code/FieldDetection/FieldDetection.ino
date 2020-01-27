#include <Wire.h>
#include <SPI.h>
#include <Adafruit_PN532.h>

#define PN532_IRQ   (3)
#define PN532_RESET (23)

Adafruit_PN532 nfc(PN532_IRQ,PN532_RESET);
//Adafruit_PN532 nfc(PN532_SCK, PN532_MISO, PN532_MOSI, PN532_SS);

#if defined(ARDUINO_ARCH_SAMD)
// for Zero, output on USB Serial console, remove line below if using programming port to program the Zero!
// also change #define in Adafruit_PN532.cpp library file
   #define Serial SerialUSB
#endif

// constants won't change. They're used here to set pin numbers:
const int buttonPin_MTP = 4;     // the number of the pushbutton pin
const int buttonPin_Atk = 6;     // the number of the pushbutton pin
const int buttonPin_Def = 5;     // the number of the pushbutton pin

int Prev_Status_MTP = 1;
int Prev_Status_Atk = 1;
int Prev_Status_Def = 1;
int Aux_Status_MTP = 1;
int Aux_Status_Atk = 1;
int Aux_Status_Def = 1;
int buttonState_MTP ;
int buttonState_Atk;
int buttonState_Def;

int NextState = 0;
int State = 0;




void Process_Read_Card(String CardID){
//  Serial.println(CardID);
  delay(2000);
  // read the state of the pushbutton value:
  buttonState_MTP = Check_Position(buttonPin_MTP);
  buttonState_Atk = Check_Position(buttonPin_Atk);
  buttonState_Def = Check_Position(buttonPin_Def);
  
//  Serial.println(buttonState_MTP);
//  Serial.println(buttonState_Atk);
//  Serial.println(buttonState_Atk);

  if( buttonState_MTP!=Prev_Status_MTP || buttonState_Atk!=Prev_Status_Atk || buttonState_Def!=Prev_Status_Def){
//    Serial.println("New Change in field");
    delay(100);
    Aux_Status_MTP = buttonState_MTP;
    Aux_Status_Atk = buttonState_Atk;
    Aux_Status_Def = buttonState_Def;
    //Estos son nuestros estados nuevos
    buttonState_MTP = Check_Position(buttonPin_MTP);
    buttonState_Atk = Check_Position(buttonPin_Atk);
    buttonState_Def = Check_Position(buttonPin_Def);

//    Serial.println(buttonState_MTP);
//    Serial.println(buttonState_Atk);
//    Serial.println(buttonState_Atk);

    if(Aux_Status_MTP == buttonState_MTP && Aux_Status_Atk == buttonState_Atk && Aux_Status_Def == buttonState_Def){
//      Serial.println("Seleccionando estado");
      if( buttonState_Atk==1 && buttonState_Def==1 && buttonState_MTP==1){
        NextState = 0;
//        Serial.println("Campo Libre");
        }
      if( buttonState_Atk==0 && buttonState_Def==0 && buttonState_MTP==0){
        NextState = 5;
//        Serial.println("Ataque y MTP");
        }
      if( buttonState_Atk==1 && buttonState_Def==0 && buttonState_MTP==0){
        NextState = 4;
//        Serial.println("Defensa y MTP");
        }
      if( buttonState_Atk==1 && buttonState_Def==0 && buttonState_MTP==1){
        NextState = 2;
//        Serial.println("Defensa");
        }
      if( buttonState_Atk==0 && buttonState_Def==0 && buttonState_MTP==1){
        NextState = 1;
//        Serial.println("Ataque");
        }
      if( buttonState_Atk==1 && buttonState_Def==1 && buttonState_MTP==0){
        NextState = 3;
//        Serial.println("MTP");
        }
     State = MEF(State,NextState,CardID);
      
      Prev_Status_MTP = buttonState_MTP;
      Prev_Status_Atk = buttonState_Atk;
      Prev_Status_Def = buttonState_Def;
      
      }
  
  }
}

int Check_Position(int buttonPin){
  int sensorState = digitalRead(buttonPin);
  
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  delay(10);
  sensorState = sensorState + digitalRead(buttonPin);
  
  if(sensorState>8){
    return 1;
    }
  else{
    return 0;
    }
  }


int MEF(int State,int NextState, String CardID){
  
  switch(State){
    case 0:
      if(NextState == 1){
        State = NextState;
        Serial.println("001"+CardID);
//        Serial.println(CardID);
        }
      if(NextState == 2){
        State = NextState;
        Serial.print("010");
        Serial.println(CardID);
        }
      if(NextState == 3){
        State = NextState;
        Serial.print("011");
        Serial.println(CardID);
        }
      break;
    case 1:
      if(NextState == 2){
        State = NextState;
        Serial.print("010");
        Serial.println(CardID);
        }
      if(NextState == 5){
        State = NextState;
        Serial.print("011");
        Serial.println(CardID);
        }
      if(NextState == 0){
        State = NextState;
        Serial.print("101");
        Serial.println(CardID);
        }
      break;
    case 2:
      if(NextState == 1){
        State = NextState;
        Serial.print("001");
        Serial.println(CardID);
        }
      if(NextState == 4){
        State = NextState;
        Serial.print("011");
        Serial.println(CardID);
        }
      if(NextState == 0){
        State = NextState;
        Serial.print("110");
        Serial.println(CardID);
        }
      break;
    case 3:
      if(NextState == 4){
        State = NextState;
        Serial.print("010");
        Serial.println(CardID);
        }
      if(NextState == 5){
        State = NextState;
        Serial.print("001");
        Serial.println(CardID);
        }
      if(NextState == 0){
        State = NextState;
        Serial.print("111");
        Serial.println(CardID);
        }
      break;
    case 4:
      if(NextState == 2){
        State = NextState;
        Serial.print("111");
        Serial.println(CardID);
        }
      if(NextState == 5){
        State = NextState;
        Serial.print("001");
        Serial.println(CardID);
        }
      if(NextState == 3){
        State = NextState;
        Serial.print("110");
        Serial.println(CardID);
        }
      break;
    case 5:
      if(NextState == 1){
        State = NextState;
        Serial.print("111");
        Serial.println(CardID);
        }
      if(NextState == 4){
        State = NextState;
        Serial.print("010");
        Serial.println(CardID);
        }
      if(NextState == 3){
        State = NextState;
        Serial.print("101");
        Serial.println(CardID);
        }
      break;
    
    }
    return State;
  
  
  }

void setup() {
  #ifndef ESP8266
    while (!Serial); // for Leonardo/Micro/Zero
  #endif
  Serial.begin(9600);
  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print("Didn't find PN53x board");
    while (1); // halt
  }  
  nfc.SAMConfig();
  pinMode(buttonPin_MTP, INPUT);
  pinMode(buttonPin_Atk, INPUT);
  pinMode(buttonPin_Def, INPUT);
  pinMode(7, OUTPUT);
  
}

void loop() {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };
  uint8_t uidLength;
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  if (success) {  
    if (uidLength == 4){
      uint8_t keya[6] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF };
      success = nfc.mifareclassic_AuthenticateBlock(uid, uidLength, 4, 0, keya);
      if (success){  
        uint8_t data[16];          
        // Para escribir una carta en el Bloque 4
        //memcpy(data, (const uint8_t[]){ '3', '9', '2', '7', '1', '5', '5', '3', 0, 0, 0, 0, 0, 0, 0, 0 }, sizeof data);
        //success = nfc.mifareclassic_WriteDataBlock (4, data);
        success = nfc.mifareclassic_ReadDataBlock(4, data);
        if (success){
          String ReadBlock;
          String ReadCard = "11111111";
          for (char c : data) ReadBlock += c;
          ReadCard[0] = ReadBlock[0];
          ReadCard[1] = ReadBlock[1];
          ReadCard[2] = ReadBlock[2];
          ReadCard[3] = ReadBlock[3];
          ReadCard[4] = ReadBlock[4];
          ReadCard[5] = ReadBlock[5];
          ReadCard[6] = ReadBlock[6];
          ReadCard[7] = ReadBlock[7];
//          Serial.println(ReadCard);
          digitalWrite(7, HIGH);   // turn the LED on (HIGH is the voltage level)
          delay(200);                       // wait for a second
          digitalWrite(7, LOW);
          Process_Read_Card(ReadCard);
          delay(100);
        }
        else{
          Serial.println("Ooops ... unable to read the requested block.  Try another key?");
        }
      }
      else{
        Serial.println("Ooops ... authentication failed: Try another key?");
      }
    }
  }
}
