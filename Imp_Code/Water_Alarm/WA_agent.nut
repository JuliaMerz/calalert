// Imp agent code @author Nick Firmani
// Handler for status queries 
function requestHandler(request, response) {
    server.log("Status query");
    try {
        // Check if the user sent status as a query parameter
        if ("status" in request.query) {
            //ping the device to check
            device.send("blinkgrn", null);
            // Send a response back saying everything was OK.
            response.send(200, "OK");
        }
    } catch (ex) {
    response.send(500, "Internal Server Error: " + ex);
    }
}
// Handler for alarms
function eventHandler(mac) {
    local alerttyp = "water";
    local uri = format("http://79cc6dea.ngrok.com/alert"); // Flask server address
    try {
        server.log(uri);
        local request = http.post(uri, { "Content-Type": "text/plain" }, mac); // Sends http POST request
        local response = request.sendsync();
        server.log(alerttyp + " SENT, SERVER RESPONSE: " + response.statuscode); // Logs result
    }
    catch (ex) {
        server.log(ex);
    }
}

// Register the HTTP handler
http.onrequest(requestHandler);
// Register alarm listener. 
device.on("sendmessage", eventHandler);
