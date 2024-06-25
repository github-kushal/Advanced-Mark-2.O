int relayPin = 7;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
  // Blink relay LED three times on start for confirmation
  // for (int i = 0; i < 3; i++) {
  //   digitalWrite(relayPin, HIGH);
  //   delay(100);
  //   digitalWrite(relayPin, LOW);
  //   delay(100);
  
  // Serial.println("Setup complete");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the input until a newline character
    command.trim(); // Remove any leading or trailing whitespace

    Serial.print("Received command: ");
    Serial.println(command);

    if (command == "on") {
      digitalWrite(relayPin, LOW);
      Serial.println("Light turned on");
    } 
    else if (command == "off") {
      digitalWrite(relayPin, HIGH);
      Serial.println("Light turned off");
    }
  }
}
