void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}


// the loop function runs over and over again forever
void loop() 
{
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  Serial.println("LED ON:");
  delay(2000);                       // wait for a second  
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  Serial.println("LED OFF");
  dela(3000);                       // wait for a second
}
