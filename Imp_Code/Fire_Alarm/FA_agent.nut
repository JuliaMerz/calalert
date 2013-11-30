// Imp agent code @author Nick Firmani
// Handles status queries
function requestHandler(request, response) {
    server.log("Status query");
    try {
        // check if the user sent status as a query parameter
        if ("status" in request.query) {
            //ping the device to check
            device.send("blinkgrn", null);
            // send a response back saying everything was OK.
            response.send(200, "OK");
        }
    } catch (ex) {
    response.send(500, "Internal Server Error: " + ex);
    }
}

// Handle an alarm from the Imp
function eventHandler(mac) {
    local alerttyp = "fire";
    local uri = format("http://79cc6dea.ngrok.com/alert"); // Flask server address
    try {
        local request = http.post(uri, { "Content-Type": "text/plain" }, mac); //Sends ID code and alarmtype
        local response = request.sendsync();
        server.log("ALARM SENT, SERVER RESPONSE: " + response.statuscode); // Logs response code
    }
    catch (ex) {
        server.log(ex);
    }
}

// register the HTTP handler
http.onrequest(requestHandler);
// register the Alarm handler
device.on("sendmessage", eventHandler);


