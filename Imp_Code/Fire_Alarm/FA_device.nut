// Imp device code @author Nick Firmani
// Configure the imp
imp.configure("Fire Alarm", [], []);
 
// Configure LEDs
grnled <- hardware.pin8;
grnled.configure(DIGITAL_OUT);
redled <- hardware.pin9;
grnled.configure(DIGITAL_OUT);

// Configure microphone
micin <- hardware.pin1;
micin.configure(ANALOG_IN)

// Init monitor function to test for fire alarm status
function mon() {
    local micval = micin.read();
    if (micval > 50000) { // Magic number here was determined by value of OpAmp output
        blinkgrn(); // Turn LED on
        agent.send("sendmessage", imp.getmacaddress());
        server.log(micval);
    }
    imp.wakeup(0.1, mon); // Wakeup value is low for demonstration
}

// Function to blink green LED
function blinkgrn() {
    grnled.write(1);
    imp.wakeup(1, ledsoff);
}
function ledsoff() {
    grnled.write(0);
    redled.write(0);
}
// Start monitor function
mon()
