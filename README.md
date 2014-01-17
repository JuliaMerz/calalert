

<table width="100%">
 <tr>
  <td width="25%"> 
  Angyl:<br />
  An extensible sensor interface system for home and personal safety. 
  </td><td width="75%">
  <img src="http://i.imgur.com/K2o00IN.jpg" alt="Angyl Image">
  </td>
 </tr>
</table>

The process for how it works is as follows:
  * The user registers their sensor devices with a unique ID and phone number for alert messages on the web interface.
    * For the Hackathon demo we used Electric imp sensors to send water intrusion or fire alerts to the server.
    * For the demo Imp, we 3D printed a case
  * The flask based server takes the alert information from the sensor, looks up the correct phone number in the database, and passes it to Twilio
  * Twilio sends out an SMS to the registered number(s)
  * An Android application reads the alert SMS if it contains key code words, and if it does, overrides the phone's settings to sound an alarm. 

The system is extensible in the manner that any device that can send a HTTP post request with a unique ID can be setup to send alerts through this system. 

The server also has the capability to read RSS feeds for alert messages and send these to the user in the same manner.

The SMS messages that the server sends out are also human readable for non smartphones or if the application was not installed.
