package com.example.safet;
 
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsMessage;
import android.util.Log;

/** Broadcast reciever for SMS messages.
 * This listens for alarm messages that get sent to phone.
 * @author Nick Firmani */
 
public class SmsReceiver extends BroadcastReceiver
{
    @Override
    public void onReceive(Context context, Intent intent) {
        // Get the SMS message that gets passedin
    	Log.d("Angyl", "SMS Recieved");
        Bundle bundle = intent.getExtras();        
        SmsMessage[] messages = null;    
               
        if (bundle != null) {
            // Parse the SMS info
            Object[] pdus = (Object[]) bundle.get("pdus");
            messages = new SmsMessage[pdus.length];    
            // Iterate over messages recieved and act accordingly        
            for (int i = 0; i < messages.length; i++) {
                // Get info
                messages[i] = SmsMessage.createFromPdu((byte[])pdus[i]);                
                String number = messages[i].getOriginatingAddress(); 
                String body =  messages[i].getMessageBody().toString();   
                // Hardcoded Twilio phone number, to prevent abuse
                if (number.equals("+14089164543") || number.equals("+12064376680")) {
                    Log.d("Angyl", "SMS trigger from: " + number);
                    Log.d("Angyl", "SMS trigger text: " + body);
                    // Start the alarm activity
                	Intent outintent = new Intent(context, AlarmActivity.class);
                	outintent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                	outintent.putExtra("mess", body);
                	context.startActivity(outintent);
                }
            }
        }                         
    }
}
