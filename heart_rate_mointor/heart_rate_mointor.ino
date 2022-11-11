int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider
 
void setup(void) {
  Serial.begin(9600);   
}
 
void loop(void) {
  float dataRead = analogRead(fsrPin);
//  fsrReading = analogRead(fsrPin);  
// 
//  Serial.println("Analog reading = ");
//  Serial.println(fsrReading);     // print the raw analog reading

   
    dataRead = (dataRead/2024.0) * 0.5;
    Serial.println(dataRead);
    delay(300);
 
  
   

  delay(1000);
}