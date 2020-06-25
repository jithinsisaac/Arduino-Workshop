void setup() 
{
  pinMode(5,INPUT);
  pinMode(9,OUTPUT);
}

void loop() 
{
  // put your main code here, to run repeatedly:
    if (digitalRead(5)==LOW)
      {
        digitalWrite((9),HIGH);
      }
      else if(digitalRead(5)==HIGH)
      {
        digitalWrite((9),LOW);
      }    
}
