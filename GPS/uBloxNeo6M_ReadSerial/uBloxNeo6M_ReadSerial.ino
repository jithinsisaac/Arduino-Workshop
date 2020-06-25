 

void setup()
{
  // Start the Arduino hardware serial port at 9600 baud
  Serial.begin(9600);

  // Start the software serial port at the GPS's default baud
  Serial1.begin(9600);
}

void loop()
{ 
    while (Serial1.available() > 0)
    Serial.write(Serial1.read());
}
