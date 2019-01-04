package calculator.xwg;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.nio.CharBuffer;

import android.app.Activity;
import android.os.Bundle;
import android.text.method.ScrollingMovementMethod;
import android.widget.TextView;

public class HelpActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.help);
		
		CharBuffer buffer = null;
		
		InputStream is = getResources().openRawResource(R.raw.help);
		InputStreamReader reader = null;
		try {
			reader = new InputStreamReader(is, "UTF-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			buffer = CharBuffer.allocate(is.available());
			reader.read(buffer.array(), 0, is.available());
			is.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if(buffer != null){
			((TextView)findViewById(R.id.helpView)).setText(buffer);
			((TextView)findViewById(R.id.helpView)).setMovementMethod(ScrollingMovementMethod.getInstance());
		}
	}
	
}
