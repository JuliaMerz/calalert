// Imp device code @author Nick Firmani
// Configure the Imp
imp.configure("WATER ALARM", [], []);

//Configure LEDs
grnled <- hardware.pin8;
grnled.configure(DIGITAL_OUT);
redled <- hardware.pin9;
grnled.configure(DIGITAL_OUT);

// Configure sensor pins
sensin <- hardware.pin2;
sensin.configure(ANALOG_IN)

// Monitor function to check sensor status
function mon() {
    local sensval = sensin.read();
    if (sensval > 60000) { // Value here is scaled voltage (0 - 65555)
        blinkgrn(); // Light LED
        agent.send("sendmessage", imp.getmacaddress()); // Call server
        server.log(sensval);
    }
    imp.wakeup(2, mon);
}

// Function to blink the green LEDs
function blinkgrn() {
    grnled.write(1);
    imp.wakeup(1, ledsoff);
}
function ledsoff() {
    grnled.write(0);
    redled.write(0);
}
// Start monitoring
mon()
