package com.example.safet;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;

/** Placeholder class for eventual Splash screen for the Imp status
 * Interface for registration of Imps too. (Expansion)
 * @author Nick Firmani*/

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
