int speakerpin = 2; //스피커가 연결된 디지털핀 설정
int state = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 
    
    char flag = 'n';
    flag = Serial.read();
    Serial.println(flag);
    if(flag=='s'){
      tone(speakerpin,500,100);  //500: 음의 높낮이(주파수), 1000: 음의 지속시간(1초)
      delay(100);
      digitalWrite(11, HIGH);
      delay(100);
      Serial.println("flag = 1");
    }
    else if (flag=='n'){
      digitalWrite(11, LOW);
      Serial.println("flag = 0");
      noTone(speakerpin);
    }


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


void alarm(){
  
   
}
