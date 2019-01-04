package calculator.xwg;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.util.TreeMap;

import android.app.Activity;
import android.app.Dialog;
import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.text.TextPaint;
import android.text.method.ScrollingMovementMethod;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.TextView;
import android.widget.Toast;

public class CalculatorMainActivity extends Activity {
	final static String CONVERT_FORMAT = "convertFormat";
	final static String CALCULATE = "=";
	final static String COMMAND_TEXT = "commandText";
	final static String ITEM_ARRAY = "ItemArray";
	
	final static String HISTORY_LIST = "HistoryList";
	final static String CALCULATE_FINISHED = "CalculateFinished";
	final static String INV_STATUS = "InvStatus";
	final static String QUESTION_TEXT = "QuestionText";
	final static String ANSWER_TEXT = "AnswerText";
	
	
	ArrayList<String> historyList;// = new ArrayList<String>();
	boolean calculateFinished = true;
	
	class ButtonTextManager{
		class TextPair{
			TextPair(String normal, String inv){
				textNormal = normal;
				textInv = inv;
			}
			String textNormal;
			String textInv;
		}
		TreeMap<Integer, TextPair> textMap = new TreeMap<Integer, TextPair>(); 
		
		void resetButtonText(boolean isChecked){
			Set<Integer> ids = textMap.keySet();
			if(isChecked){
				for(Integer i : ids){
					((Button)findViewById(i)).setText(textMap.get(i).textInv);
				}
			}else{
				for(Integer i : ids){
					((Button)findViewById(i)).setText(textMap.get(i).textNormal);
				}
			}
		}
		
		void registerButtonText(int id, String normal, String inv){
			textMap.put(id, new TextPair(normal, inv));
		}
	}
	
	public CalculateEngine engine = null;
	HashMap<String, TextCommand> commandMap = new HashMap<String, TextCommand>();
	InputTextCommand defaultCommand = new InputTextCommand();
	ButtonTextManager buttonTextManager = new ButtonTextManager();
	
	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if(this.getResources().getConfiguration().orientation == Configuration.ORIENTATION_LANDSCAPE) {    
        	setContentView(R.layout.main_h);    
        } else if (this.getResources().getConfiguration().orientation == Configuration.ORIENTATION_PORTRAIT) {    
        	setContentView(R.layout.main);    
        }
        
        engine = new CalculateEngine(this);
        
        initializeCommandMap();
        initializeButtonTextManager();
        
        CheckBox checkBoxInv = (CheckBox)this.findViewById(R.id.checkInv);
        checkBoxInv.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener(){
        	public void onCheckedChanged(CompoundButton buttonView, boolean isChecked){
        		buttonTextManager.resetButtonText(isChecked);
        	}
        });
        
        TextView question_view = (TextView)findViewById(R.id.textQuestion);
        question_view.setMovementMethod(ScrollingMovementMethod.getInstance());
                
        if(savedInstanceState != null){
        	checkBoxInv.setChecked(savedInstanceState.getBoolean(INV_STATUS, false));
        	historyList = savedInstanceState.getStringArrayList(HISTORY_LIST);
        	setCalculateFinished(savedInstanceState.getBoolean(CALCULATE_FINISHED, true));
        	question_view.setText(savedInstanceState.getString(QUESTION_TEXT));
        	TextView answer_view = (TextView)findViewById(R.id.textAnswer);
            answer_view.setText(savedInstanceState.getString(ANSWER_TEXT));
        }
        
        if(historyList == null){
        	historyList = new ArrayList<String>();
        }
    }
    
    @Override
	protected void onSaveInstanceState(Bundle outState) {
		outState.putBoolean(CALCULATE_FINISHED, calculateFinished);
		outState.putStringArrayList(HISTORY_LIST, historyList);
		
		CheckBox checkBoxInv = (CheckBox)this.findViewById(R.id.checkInv);
		outState.putBoolean(INV_STATUS, checkBoxInv.isChecked());
	       
        TextView question_view = (TextView)findViewById(R.id.textQuestion);
        outState.putString(QUESTION_TEXT, question_view.getText().toString());
        
        TextView answer_view = (TextView)findViewById(R.id.textAnswer);
        outState.putString(ANSWER_TEXT, answer_view.getText().toString());
        		
		super.onSaveInstanceState(outState);
	}
    
    // Implement the OnClickListener callback
    public void onButtonClick(View v) {
      Button button = (Button)v;
      String buttonText = button.getText().toString();
      onButtonClick(buttonText);
    }
    
    public void onButtonClick(String buttonText){
    	TextCommand cmd = commandMap.get(buttonText);
        if(cmd == null){
      	  cmd = defaultCommand;
        }
        cmd.execute(buttonText);
        
        CheckBox checkBoxInv = (CheckBox)this.findViewById(R.id.checkInv);
        if(checkBoxInv.isChecked()){
      	  checkBoxInv.setChecked(false);
        }
    }
      
    public Dialog mDialog;		//open for test.
    @Override
    protected Dialog onCreateDialog(int id, Bundle bundle) {
    	mDialog = null;
    	DialogCreator creator = new DialogCreator(this);
    	switch(id){
		case R.string.memory_recall_dialog:
			mDialog = creator.createAlertDialog(id, bundle.getCharSequenceArray(ITEM_ARRAY), new AppendTextListener(id));
			break;
		case R.string.memory_clear_dialog:
			mDialog = creator.createAlertDialog(id, bundle.getCharSequenceArray(ITEM_ARRAY), new ClearMemoryListener(id));
			break;
		case R.string.function_set_dialog:
			mDialog = creator.createAlertDialog(id, bundle.getCharSequenceArray(ITEM_ARRAY), new SaveQuestionListener(id, bundle.getCharSequence(COMMAND_TEXT)));
			break;
		case R.string.const_select_dialog:
			mDialog = creator.createAlertDialog(id, bundle.getCharSequenceArray(ITEM_ARRAY), new AppendTextListener(id));
			break;
		case R.string.input_fun_name_dlg:
			mDialog = creator.createInputTextDialog(id, null, new FsCommand());
			break;
		case R.string.error_msg_dialog:
			mDialog = creator.createAlertDialog(id, bundle.getCharSequence(COMMAND_TEXT));
			break;
		}
		return mDialog;
	}
    
    @Override
	public boolean onCreateOptionsMenu(Menu menu) {
    	MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.main, menu);
        return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		if(item.getItemId() == R.id.menu_item_help){
			Intent i = new Intent(this, HelpActivity.class);
			startActivityForResult(i, 0);
			return true;
		}else{
			return super.onOptionsItemSelected(item);
		}
	}
	
	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		super.onActivityResult(requestCode, resultCode, data);
	}

	void initializeButtonTextManager(){
    	buttonTextManager.registerButtonText(R.id.button10, "sin", "sinh");
    	buttonTextManager.registerButtonText(R.id.button11, "cos", "cosh");
    	buttonTextManager.registerButtonText(R.id.button12, "tan", "tanh");
    	buttonTextManager.registerButtonText(R.id.button13, "asin", "asinh");
    	buttonTextManager.registerButtonText(R.id.button14, "acos", "acosh");
    	buttonTextManager.registerButtonText(R.id.button15, "atan", "atanh");
    	
    	buttonTextManager.registerButtonText(R.id.button20, "x2", "sum");
    	buttonTextManager.registerButtonText(R.id.button21, "x3", "avg");
    	buttonTextManager.registerButtonText(R.id.button22, "2" + getText(R.string.character_sqrt), "n!");
    	buttonTextManager.registerButtonText(R.id.button23, "3" + getText(R.string.character_sqrt), "ex");
    	buttonTextManager.registerButtonText(R.id.button24, "pow", "log10");
    	buttonTextManager.registerButtonText(R.id.button25, "root", "loge");
    	
    	resetCustomFuntionButton();
    	
    	CheckBox checkBoxInv = (CheckBox)this.findViewById(R.id.checkInv);
    	buttonTextManager.resetButtonText(checkBoxInv.isChecked());
    }
	
	void resetCustomFuntionButton(){
		CharSequence[] items = engine.getCustomFunctionItems();
    	int[] buttonId = new int[]{R.id.buttonF1, R.id.buttonF2, R.id.buttonF3, R.id.buttonF4, R.id.buttonF5, R.id.buttonF6};
    	for(int i = 0; i < 6; ++i){
    		String strNormal = items[i].toString();
    		strNormal = strNormal.substring(0, strNormal.indexOf(":"));
    		String strInv = items[i + 6].toString();
    		strInv = strInv.substring(0, strInv.indexOf(":"));
    	   	buttonTextManager.registerButtonText(buttonId[i], strNormal, strInv);
    	}
	}
    
    void initializeCommandMap(){
    	commandMap.put("MR", new MrCommand());
    	commandMap.put("MC", new McCommand());
    	commandMap.put("MS", new MsCommand());
    	commandMap.put("FS", new GetFunNameCommand());
    	commandMap.put(getText(R.string.character_degree).toString(), new ConvertCommand());
    	commandMap.put(getText(R.string.character_angle).toString(), new ConvertCommand());
    	commandMap.put("const", new ConstCommand());
    	commandMap.put("AC", new AcCommand());
    	commandMap.put("<=", new BackCommand());
    	commandMap.put("exp", new ExpCommand());
    	commandMap.put(CALCULATE, new CalculateCommand());
    	commandMap.put(CONVERT_FORMAT, new CalculateCommand());
    }
    
    void setCalculateFinished(boolean finished){
    	calculateFinished = finished;
    }
    
    boolean isCalculateFinished(){
    	return calculateFinished;
    }
    
    void appendQustionText(CharSequence text)
    {
    	String question = getQuestionText().toString() + text;
    	setQuestionText(question);
    	TextView qv = (TextView)findViewById(R.id.textQuestion);
    	TextPaint tp = qv.getPaint();
    	int txt_width = (int)tp.measureText(question);
    	int disp_width = qv.getWidth() - qv.getPaddingLeft() - qv.getPaddingRight();
    	if(txt_width - qv.getScrollX() > disp_width){
    		qv.scrollTo(txt_width - disp_width + disp_width * 2 / 3, 0);
    	}
    }
    
    void setQuestionText(CharSequence text){
    	historyList.add(getQuestionText().toString());
    	TextView qv = (TextView)findViewById(R.id.textQuestion);
    	qv.setText(text);
    }
    
    void backQustionText()
    {
    	if(historyList.size() > 0){
    		String prevText = historyList.remove(historyList.size() - 1);
    		TextView qv = (TextView)findViewById(R.id.textQuestion);
        	qv.setText(prevText);
        	TextPaint tp = qv.getPaint();
        	int txt_width = (int)tp.measureText(prevText);
        	int disp_width = qv.getWidth() - qv.getPaddingLeft() - qv.getPaddingRight();
        	if(txt_width - qv.getScrollX() < 0){
        		int new_pos = txt_width - disp_width + disp_width / 3;
        		qv.scrollTo(StrictMath.max(0, new_pos), 0);
        	}
    		clearAnswerText();
    	}
    }
    
    CharSequence getQuestionText(){
    	String question = ((TextView)findViewById(R.id.textQuestion)).getText().toString();
    	return question.trim();
    }
    
    void setAnswerText(CharSequence text){
    	((TextView)findViewById(R.id.textAnswer)).setText(text);
    }
    
    CharSequence getAnswerText(){
    	return ((TextView)findViewById(R.id.textAnswer)).getText();
    }
    
    void clearQuestionText()
    {
    	TextView qv = (TextView)findViewById(R.id.textQuestion);
    	qv.setText("");
    	qv.scrollTo(0, 0);
    	historyList.clear();
    }
    
    void clearAnswerText()
    {
    	setAnswerText("0");
    }
    
    class InputTextCommand implements TextCommand
	{
		public boolean execute(CharSequence buttonText){
			if(isCalculateFinished())
			{
				clearQuestionText();
				clearAnswerText();
				setCalculateFinished(false);
			}
			String buttonString = buttonText.toString();
			if(engine.isFunction(buttonString)){
				buttonString += "(";
			}
			appendQustionText(buttonString);
			return true;
		}
	}
	
    class MrCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		Bundle bundle = new Bundle();
    		bundle.putCharSequence(COMMAND_TEXT, buttonText);
    		bundle.putCharSequenceArray(ITEM_ARRAY, engine.getRecordItems());
    		showDialog(R.string.memory_recall_dialog, bundle);
			return true;
		}
    }
    
    class McCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		Bundle bundle = new Bundle();
    		bundle.putCharSequence(COMMAND_TEXT, buttonText);
    		bundle.putCharSequenceArray(ITEM_ARRAY, engine.getRecordItems());
    		showDialog(R.string.memory_clear_dialog, bundle);
			return true;
		}
    }
    
    class MsCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		if(engine.saveRecord())
    		{
    			Toast.makeText(getApplicationContext(), "Memory Set succesfully.",
  		              Toast.LENGTH_SHORT).show();
    		}
			return true;
		}
    }
    
    class GetFunNameCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		Bundle bundle = new Bundle();
    		bundle.putCharSequence(COMMAND_TEXT, buttonText);
    		bundle.putCharSequenceArray(ITEM_ARRAY, engine.getCustomFunctionItems());
    		showDialog(R.string.input_fun_name_dlg, bundle);
			return true;
		}
    }
    
    class FsCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		String buttonString = buttonText.toString();
    		if(buttonString.matches("[a-zA-Z][0-9a-zA-Z]{0,3}")){
    			Bundle bundle = new Bundle();
    			bundle.putCharSequence(COMMAND_TEXT, buttonText);
    			bundle.putCharSequenceArray(ITEM_ARRAY, engine.getCustomFunctionItems());
    			showDialog(R.string.function_set_dialog, bundle);
    		}else{
    			Bundle bundle = new Bundle();
    			bundle.putCharSequence(COMMAND_TEXT, getText(R.string.error_invalid_fun_name));
    			showDialog(R.string.error_msg_dialog, bundle);
    		}
    		return true;	
		}
    }
    
    class ConvertCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		if(isCalculateFinished()){
	    		String question = getQuestionText().toString();
	    		String buttonString = "to" + buttonText.toString();
	    		((TextView)findViewById(R.id.textQuestion)).setText(buttonString + "(" + question.toString() + ")");	
	    		onButtonClick(CONVERT_FORMAT);
	    		((TextView)findViewById(R.id.textQuestion)).setText(question);
			}else{
    			InputTextCommand cmd = new InputTextCommand();
    			cmd.execute(buttonText);
    		}
			return true;
		}
    }
    
    class ConstCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		Bundle bundle = new Bundle();
    		bundle.putCharSequence(COMMAND_TEXT, buttonText);
    		bundle.putCharSequenceArray(ITEM_ARRAY, engine.getConstItems());
    		showDialog(R.string.const_select_dialog, bundle);
			return true;
		}
    }
    
    class BackCommand implements TextCommand{
    	public boolean execute(CharSequence buttonText){
    		backQustionText();
    		setCalculateFinished(false);
			return true;
		}
    }
    
    class AcCommand implements TextCommand
	{
		public boolean execute(CharSequence buttonText){
			clearQuestionText();
			clearAnswerText();
			return true;
		}
	}
    
	class ExpCommand implements TextCommand
	{
		public boolean execute(CharSequence buttonText){
			appendQustionText("e");
			return true;
		}
	}
    
    class CalculateCommand implements TextCommand
	{
		public boolean execute(CharSequence buttonText){
			String result = engine.calculate(getQuestionText().toString(), 
											buttonText.toString().compareTo(CONVERT_FORMAT) == 0);
			setAnswerText(result);
			if(engine.isSuccess()){
				setCalculateFinished(true);
			}
			return true;
		}
	}
    
    class AppendTextListener implements OnItemClickListener{
    	private int dialogId = 0;
    	public AppendTextListener(int id){
    		dialogId = id;
    	}
	    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
	    	String text = ((TextView)view).getText().toString();
	    	InputTextCommand cmd = new InputTextCommand();
	    	cmd.execute(text.subSequence(0, text.indexOf(":")));
	    	removeDialog(dialogId);
	    }
	 }
    class SaveQuestionListener implements OnItemClickListener{
    	private int dialogId = 0;
    	private CharSequence funName;
    	public SaveQuestionListener(int id, CharSequence name){
    		dialogId = id;
    		funName = name;
    	}
	    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
	    	String key = String.format("F%d", position + 1);
	    	int result = engine.saveCustomFunction(key, funName.toString(), getQuestionText().toString());
	    	if(result == 0){
		    	setCalculateFinished(true);
		    	resetCustomFuntionButton();
		    	CheckBox checkBoxInv = (CheckBox)findViewById(R.id.checkInv);
		    	buttonTextManager.resetButtonText(checkBoxInv.isChecked());
	    	}else{
	    		Bundle bundle = new Bundle();
	    		bundle.putCharSequence(COMMAND_TEXT, getText(R.string.error_invalid_fun_name));
	    		showDialog(R.string.error_msg_dialog, bundle);
	    	}
	    	removeDialog(dialogId);
	    }
	 }
    class ClearMemoryListener implements OnItemClickListener{
    	private int dialogId = 0;
    	public ClearMemoryListener(int id){
    		dialogId = id;
    	}
	    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
	    	engine.clearRecord(position);
	    	removeDialog(dialogId);
	    }
	 }
}