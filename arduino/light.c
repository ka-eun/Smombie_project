void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  char flag = 'n';
  flag = Serial.read();
  if(flag=='s'){
    digitalWrite(13, HIGH);
    delay(100);
    Serial.println("flag = 1");
  }
  else if (flag=='n'){
    digitalWrite(13, LOW);
    Serial.println("flag = 0");
      
  }
 /* 
  while(Serial.available() > 0){
    flag = Serial.read();
    if(flag=='s'){
      digitalWrite(13, HIGH);
      delay(100000);
      Serial.println("flag = 1");
    }
    else if (flag=='n'){
      digitalWrite(13, LOW);
      Serial.println("flag = 0");
      
    }
  }
  */
}
