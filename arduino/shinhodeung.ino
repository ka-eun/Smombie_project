void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);

}
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(11, HIGH);

  for(int i=0;i<5000;i++){
    Serial.print(0);
  }
 
  digitalWrite(11, LOW);
  
  digitalWrite(12, HIGH);

  for(int i=0;i<5000;i++){
    Serial.print(1);
  }
  
  //delay(4000);
  //attachInterrupt()
  //Serial.print(1);
  
  digitalWrite(12, LOW);

}
