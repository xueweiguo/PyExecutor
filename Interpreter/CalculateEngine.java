package calculator.xwg;

import java.util.LinkedList;
import java.util.Set;
import android.content.Context;

public class CalculateEngine
{
	final static int CUSTOM_FUN_COUNT = 12;
	FunctionManager functionManager;
	ConstManager constManager = new ConstManager();
	private Context systemContext = null; 
	
	CalculateEngine(Context context){
		systemContext = context;
		functionManager = new FunctionManager(systemContext);
		registerConst();
		registerStandardFunctions();
	}
	
	void registerConst(){
		constManager.registerConst(systemContext.getText(R.string.character_pi).toString(), new Complex(Math.PI));
		constManager.registerConst("e", new Complex(Math.E));
	}
	
	void registerStandardFunctions(){
		functionManager.registerFunction(new AcosFun());
		functionManager.registerFunction(new AcoshFun());
		functionManager.registerFunction(new AsinFun());
		functionManager.registerFunction(new AsinhFun());
		functionManager.registerFunction(new AtanFun());
		functionManager.registerFunction(new AtanhFun());
		functionManager.registerFunction(new AverageFun());
		functionManager.registerFunction(new CosFun());
		functionManager.registerFunction(new CoshFun());
		functionManager.registerFunction(new Log10Fun());
		functionManager.registerFunction(new LogeFun());
		functionManager.registerFunction(new PowerFun());
		functionManager.registerFunction(new RootFun());
		functionManager.registerFunction(new SinFun());
		functionManager.registerFunction(new SinhFun());
		functionManager.registerFunction(new SumFun());
		functionManager.registerFunction(new TanFun());
		functionManager.registerFunction(new FactorialFun());
				
		functionManager.registerFunction(new ConvertFormatFun("to" + systemContext.getText(R.string.character_angle), 
										new RadiusAngleFormatter(systemContext, false)));
		functionManager.registerFunction(new ConvertFormatFun("to" + systemContext.getText(R.string.character_degree), 
										new DegreesFormatter(systemContext)));

		functionManager.registerFunction(new PreDefineFunction("x2", "pow(#1,2)"));
		functionManager.registerFunction(new PreDefineFunction("x3", "pow(#1,3)"));
		functionManager.registerFunction(new PreDefineFunction("2" + systemContext.getText(R.string.character_sqrt), "root(#1,2)"));
		functionManager.registerFunction(new PreDefineFunction("3" + systemContext.getText(R.string.character_sqrt), "root(#1,3)"));
		functionManager.registerFunction(new PreDefineFunction("ex", "pow(e,#1)"));
		
		for(int i = 1; i <= CUSTOM_FUN_COUNT; ++i){ 
			UserDefineFunction udf = UserDefineFunction.load(systemContext, "F" + i);
			if(udf != null){
				functionManager.registerUserDefineFunction(udf);
			}
		}
	}
	
	public LinkedList<Token> analyzeToken(String strQuestion){
		TokenAnalyzer analyzer = new TokenAnalyzer();
	    LinkedList<Token> tokenList = analyzer.analyzeToken(strQuestion, new TokenPatternFactory(){
	    	public int createPatterns(LinkedList<TokenPattern> list)
	        {
	        	String funPattern = PatternBuilder.build(functionManager.functions());
	            
	            if(funPattern.length() > 0){
	            	list.add(new TokenPattern(Token.EType.FunctionName, funPattern));
	            }
	            list.add(new TokenPattern(Token.EType.Parameter, "#[1-9]"));
	            
	            String constPattern = PatternBuilder.build(constManager.consts());
	            list.add(new TokenPattern(Token.EType.Number, "(" + constPattern + ")"));

	            String numberPattern = "(((\\.[0-9]+)|([0-9]+(\\.[0-9]*)?))[eE][+-]?[0-9]+)";
	            numberPattern += "|";
	            numberPattern += "((\\.[0-9]+)|([0-9]+\\.[0-9]*))"; 
	            numberPattern += "|";
	            numberPattern += "([0-9]+)";
	            
	            CharSequence degree = systemContext.getText(R.string.character_degree);
	            list.add(new TokenPattern(Token.EType.Number, "((\\.[0-9]+)|([0-9]+\\.[0-9]*)|([0-9]+))%"));
	            list.add(new TokenPattern(Token.EType.Number, "(" + numberPattern + ")[" + degree + "i]?"));
	            list.add(new TokenPattern(Token.EType.Number, "[i]"));
	            CharSequence angle = systemContext.getText(R.string.character_angle);
	            list.add(new TokenPattern(Token.EType.Operator, "[-+×/" + angle + "]"));
	            list.add(new TokenPattern(Token.EType.Parenthese, "[()]"));
	            list.add(new TokenPattern(Token.EType.Comma, ","));
	            return list.size();
	        }
	    });
	    return tokenList;
	}
	
	public String calculate(String strQuestion, boolean convertFormat){
		if(currentRecord == null){
			currentRecord = new Record();
		}
	    LinkedList<Token> tokenList = analyzeToken(strQuestion);
	    if(!convertFormat){
	    	currentRecord.question = strQuestion;
	    }
	    String result = calculate(tokenList);
	    tokenList = null;
	    return result;
	}

	boolean isFunction(String name){
		return (functionManager.getFunction(name) != null);
	}
	
	CharSequence[] getCustomFunctionItems(){
		CharSequence items[] = new CharSequence[CUSTOM_FUN_COUNT];
		
		for(int i = 1; i <= CUSTOM_FUN_COUNT; ++i){
			String key = "F" + i;
			String item = null;
			
			UserDefineFunction udf = functionManager.getUserDefineFunction(key);
			if(udf != null){
				item = udf.getName() + ":" + udf.getExprString(); 
			}else{
				item = key + ":Empty";
			}
			
			items[i - 1] = item;
		}
		return items;
	}
	
	public int saveCustomFunction(String key, String funName, String funText){
		return functionManager.registerUserDefineFunction(key, funName, funText);
	}
	
	public void clearCustomFunctions(){
		for(int i = 1; i <= CUSTOM_FUN_COUNT; ++i){ 
			UserDefineFunction.clear(systemContext, "F" + i);
		}
	}
	
	public ConstManager getConstManager(){
		return constManager;
	}
	
	CharSequence[] getConstItems(){
		int count = constManager.getConstCount();
		CharSequence items[] = new CharSequence[count];
		
		Set<String> set = constManager.consts();
		
		StandardFormatter formatter = new StandardFormatter(systemContext);
		
		int index = 0;
        for(String key : set)
        {
        	String item = key + ":" + formatter.toString(constManager.find(key));
        	items[index] = item;
        	index++;
        }
        return items;
	}

	public class Record
	{
		boolean success;
	    String question;
	    Complex result;
	}

	public int getRecordCount(){
		return recordList.size();
	}
	
	public Record getRecord(int index){
		if(index >= 0 && index < recordList.size())
	    {
	        return recordList.get(index);
	    }
	    else
	    {
	        return null;
	    }
	}
	
	public boolean saveRecord(){
		if(currentRecord != null && currentRecord.success)
	    {
	        recordList.add(currentRecord);
	        currentRecord = null;
	        return true;
	    }else{
	    	return false;
	    }
	}
	
	CharSequence[] getRecordItems(){
		StandardFormatter formator = new StandardFormatter(systemContext);
		int record_count = getRecordCount();
		CharSequence items[] = new CharSequence[record_count];
		for(int i = 0; i < record_count; ++i){
			Record record = getRecord(i);
			String recordString = formator.toString(record.result) + ":" + record.question;
			items[i] = recordString;
		}
		return items;
	}
	
	public boolean clearRecord(int index){
		if(index >= 0 && index < recordList.size())
	    {
	        recordList.remove(index);
	                                                               
	        return true;
	    }
	    else
	    {
	        return false;
	    }
	}
	
	public boolean clearAllRecord(){
		recordList.clear();
	    return true;
	}
	
	public Context getSystemContext(){
    	return systemContext;
    }
	
	public String calculate(LinkedList<Token> tokenList){
		String result = new String();

	    String unknownToken = new String();
	    for(Token token : tokenList)
	    {
	        if(token.getType() == Token.EType.NoType)
	        {
	            if(unknownToken.length() > 0)
	            {
	                unknownToken += ",";
	            }
	            unknownToken += token.getContent();
	        }
	    }
	    if(unknownToken.length() > 0)
	    {
	        currentRecord.success = false;
	        return systemContext.getString(R.string.error_unknown_keyword) + unknownToken;
	    }
	    
	    BuildContext bContext = new BuildContext(systemContext, constManager, tokenList);

	    Expr expr = AdditiveExpr.buildExpr(bContext);
	    if(expr != null){
	    	if(bContext.tokenList.size() > 0){
	    		String tokenString = new String();
	    		for(Token token : tokenList){
	    			if(tokenString.length() != 0){
	    				tokenString += ",";
	    			}
	    			tokenString += token.getContent();
	    		}
	    		currentRecord.success = false;
    	        result = systemContext.getString(R.string.error_unnecessary_keyword) + tokenString;
	    	}else{
		        EvaluateContext eContext = new EvaluateContext(systemContext, this);
		        eContext.pushResult(new Complex(0));
		        if(expr.evaluate(eContext))
		        {
		        	Complex value = eContext.popResult();
		        	result = eContext.getFormatter().toString(value);
		        	if(result != null){
		        		currentRecord.success = true;
		        		currentRecord.result = value;
		        	}else{
		        		currentRecord.success = false;
		    	        result = systemContext.getString(R.string.error_invalid_input);
		        	}
		        }
		        else
		        {
		            currentRecord.success = false;
		            result = eContext.getErrorMessage();
		        }
	    	}
	    }
	    else
	    {
	        currentRecord.success = false;
	        result = bContext.errorMessage;
	    }
	    return result;
		
	}
	
	boolean isSuccess(){
		return currentRecord.success;
	}
	
	private Record currentRecord;
	private LinkedList<Record> recordList = new LinkedList<Record>();
}
