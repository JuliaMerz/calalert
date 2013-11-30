package com.example.safet;

import android.animation.ArgbEvaluator;
import android.animation.ObjectAnimator;
import android.animation.ValueAnimator;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.media.AudioManager;
import android.media.SoundPool;
import android.os.Bundle;
import android.os.Vibrator;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.Window;
import android.widget.RelativeLayout;
import android.widget.TextView;


/** Activity to start if there is an alarm state
 * Includes a dismiss button, plays a sound and flashes lights
 * @author Nick Firmani */

public class AlarmActivity extends Activity {

	final static int S1 = R.raw.tornado_siren;
	final int RED = Color.parseColor("red");
    final int YELLOW = Color.parseColor("yellow");
    
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		Log.d("Second", "Second process started.");
		super.onCreate(savedInstanceState);
        // Disable the top bar
		requestWindowFeature(Window.FEATURE_NO_TITLE); 
        // Set up content
		setContentView(R.layout.activity_alarm);
        // New background
		RelativeLayout ri = (RelativeLayout) findViewById(R.id.alarm_view);
        // Set up text field on screen
		TextView ti = (TextView) findViewById(R.id.text_v);
        // Bind the vibrator
		Vibrator vib = (Vibrator) getSystemService(VIBRATOR_SERVICE);
        // Pull the message from the intent extras
		Intent intent = getIntent();
		String message = intent.getStringExtra("mess");
        // Start the soundPool (for playing alarm sound)
		SoundPool soundPool = new SoundPool(1, AudioManager.STREAM_MUSIC, 0);
		int sound = soundPool.load(this, S1, 1);
		// Set text on screen
		ti.setText(message);
        
		if (message.toLowerCase().contains("emergency")) {
			Log.d("Alarm!", "alarm!!!");
			vib.vibrate(6000);
			soundPool.play(sound, 1.0f, 1.0f, 0, 0, 1.0f);
			// Flash the screen red and yellow
			ValueAnimator colorAnim = ObjectAnimator.ofInt(ri, "backgroundColor", RED, YELLOW);
			colorAnim.setDuration(3000);
	        colorAnim.setEvaluator(new ArgbEvaluator());
	        colorAnim.setRepeatCount(ValueAnimator.INFINITE);
	        colorAnim.setRepeatMode(ValueAnimator.REVERSE);
	        colorAnim.start();	
		}
	}
	// Close the activity on button press
	public void breakMessage(View view) {
		Intent goMain = new Intent(Intent.ACTION_MAIN);
		goMain.addCategory(Intent.CATEGORY_HOME);
		goMain.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
		startActivity(goMain);
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.alarm, menu);
		return true;
	}

}
