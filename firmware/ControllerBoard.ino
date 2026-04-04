#define BTN_OK 10
#define BTN_UP 9
#define BTN_DOWN 8

int activeBtn = 0;

void setup(){
  
  pinMode(BTN_OK, INPUT_PULLUP);
  pinMode(BTN_UP, INPUT_PULLUP);
  pinMode(BTN_DOWN, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop(){
  if(digitalRead(BTN_OK) == HIGH){
    Serial.println("Ok Pressed");
  }

  if(digitalRead(BTN_DOWN) == HIGH){
    Serial.println("Down pressed");
  }

  if(digitalRead(BTN_UP) == HIGH){
    Serial.println("Up pressed");
  }
}
