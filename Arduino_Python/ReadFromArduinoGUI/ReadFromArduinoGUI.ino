void setup() 
{
      Serial.begin(9600);  
}

int PotentiometerValue = 0;
float voltage;

void loop() 
{

      PotentiometerValue = analogRead(A0);           //READ VALUE OF POTENTIOMETER CONNECTED TO A0
      voltage=(5.0/1023.0*PotentiometerValue);    
      
      Serial.println(voltage);
    
      delay(1000);
}
