from Interpreter.FunctionManager import *
from Interpreter.ConstManager import *
from Interpreter.R_string import *
from Interpreter.Complex import *

from Interpreter.AcosFun import *
from Interpreter.AcoshFun import *
from Interpreter.AsinFun import *
from Interpreter.AsinhFun import *
from Interpreter.AtanFun import *
from Interpreter.AtanhFun import *
from Interpreter.AverageFun import *

class CalculateEngine:
	CUSTOM_FUN_COUNT = 12

	def __init__(self, context):
		self.systemContext = context
		self.functionManager = FunctionManager(context)
		self.constManager = ConstManager()
		self.registerConst()
		self.registerStandardFunctions()

	def registerConst(self):
		self.constManager.registerConst(self.systemContext.getText(R_string.character_pi).toString(), Complex(math.PI))
		self.constManager.registerConst("e", Complex(math.E))

	
	def registerStandardFunctions(self):
		self.functionManager.registerFunction(AcosFun())
		self.functionManager.registerFunction(AcoshFun())
		self.functionManager.registerFunction(AsinFun())
		self.functionManager.registerFunction(AsinhFun())
		self.functionManager.registerFunction(AtanFun())
		self.functionManager.registerFunction(AtanhFun())
		self.functionManager.registerFunction(AverageFun())
		self.functionManager.registerFunction(CosFun())
		self.functionManager.registerFunction(CoshFun())
		self.functionManager.registerFunction(Log10Fun())
		self.functionManager.registerFunction(LogeFun())
		self.functionManager.registerFunction(PowerFun())
		self.functionManager.registerFunction(RootFun())
		self.functionManager.registerFunction(SinFun())
		self.functionManager.registerFunction(SinhFun())
		self.functionManager.registerFunction(SumFun())
		self.functionManager.registerFunction(TanFun())
		self.functionManager.registerFunction(FactorialFun())
				
		self.functionManager.registerFunction(ConvertFormatFun("to" + self.systemContext.getText(R_string.character_angle),
										RadiusAngleFormatter(self.systemContext, False)))
		self.functionManager.registerFunction(ConvertFormatFun("to" + self.systemContext.getText(R_string.character_degree),
										DegreesFormatter(self.systemContext)))

		self.functionManager.registerFunction(PreDefineFunction("x2", "pow(#1,2)"))
		self.functionManager.registerFunction(PreDefineFunction("x3", "pow(#1,3)"))
		self.functionManager.registerFunction(PreDefineFunction("2" + self.systemContext.getText(R_string.character_sqrt), "root(#1,2)"))
		self.functionManager.registerFunction(PreDefineFunction("3" + self.systemContext.getText(R_string.character_sqrt), "root(#1,3)"))
		self.functionManager.registerFunction(PreDefineFunction("ex", "pow(e,#1)"))
		
		for(int i = 1 i <= CUSTOM_FUN_COUNT ++i){
			UserDefineFunction udf = UserDefineFunction.load(systemContext, "F" + i)
			if(udf != null){
				functionManager.registerUserDefineFunction(udf)
			}
		}
	}
	
	LinkedList<Token> analyzeToken(String strQuestion){
		TokenAnalyzer analyzer = new TokenAnalyzer()
	    LinkedList<Token> tokenList = analyzer.analyzeToken(strQuestion, new TokenPatternFactory(){
	    	int createPatterns(LinkedList<TokenPattern> list)
	        {
	        	String funPattern = PatternBuilder.build(functionManager.functions())
	            
	            if(funPattern.length() > 0){
	            	list.add(new TokenPattern(Token.EType.FunctionName, funPattern))
	            }
	            list.add(new TokenPattern(Token.EType.Parameter, "#[1-9]"))
	            
	            String constPattern = PatternBuilder.build(constManager.consts())
	            list.add(new TokenPattern(Token.EType.Number, "(" + constPattern + ")"))

	            String numberPattern = "(((\\.[0-9]+)|([0-9]+(\\.[0-9]*)?))[eE][+-]?[0-9]+)"
	            numberPattern += "|"
	            numberPattern += "((\\.[0-9]+)|([0-9]+\\.[0-9]*))"
	            numberPattern += "|"
	            numberPattern += "([0-9]+)"
	            
	            CharSequence degree = systemContext.getText(R_string.character_degree)
	            list.add(new TokenPattern(Token.EType.Number, "((\\.[0-9]+)|([0-9]+\\.[0-9]*)|([0-9]+))%"))
	            list.add(new TokenPattern(Token.EType.Number, "(" + numberPattern + ")[" + degree + "i]?"))
	            list.add(new TokenPattern(Token.EType.Number, "[i]"))
	            CharSequence angle = systemContext.getText(R_string.character_angle)
	            list.add(new TokenPattern(Token.EType.Operator, "[-+×/" + angle + "]"))
	            list.add(new TokenPattern(Token.EType.Parenthese, "[()]"))
	            list.add(new TokenPattern(Token.EType.Comma, ","))
	            return list.size()
	        }
	    })
	    return tokenList
	}
	
	String calculate(String strQuestion, boolean convertFormat){
		if(currentRecord == null){
			currentRecord = new Record()
		}
	    LinkedList<Token> tokenList = analyzeToken(strQuestion)
	    if(!convertFormat){
	    	currentRecord.question = strQuestion
	    }
	    String result = calculate(tokenList)
	    tokenList = null
	    return result
	}

	boolean isFunction(String name){
		return (functionManager.getFunction(name) != null)
	}
	
	CharSequence[] getCustomFunctionItems(){
		CharSequence items[] = new CharSequence[CUSTOM_FUN_COUNT]
		
		for(int i = 1 i <= CUSTOM_FUN_COUNT ++i){
			String key = "F" + i
			String item = null
			
			UserDefineFunction udf = functionManager.getUserDefineFunction(key)
			if(udf != null){
				item = udf.getName() + ":" + udf.getExprString()
			}else{
				item = key + ":Empty"
			}
			
			items[i - 1] = item
		}
		return items
	}
	
	int saveCustomFunction(String key, String funName, String funText){
		return functionManager.registerUserDefineFunction(key, funName, funText)
	}
	
	void clearCustomFunctions(){
		for(int i = 1 i <= CUSTOM_FUN_COUNT ++i){
			UserDefineFunction.clear(systemContext, "F" + i)
		}
	}
	
	ConstManager getConstManager(){
		return constManager
	}
	
	CharSequence[] getConstItems(){
		int count = constManager.getConstCount()
		CharSequence items[] = new CharSequence[count]
		
		Set<String> set = constManager.consts()
		
		StandardFormatter formatter = new StandardFormatter(systemContext)
		
		int index = 0
        for(String key : set)
        {
        	String item = key + ":" + formatter.toString(constManager.find(key))
        	items[index] = item
        	index++
        }
        return items
	}

	class Record
	{
		boolean success
	    String question
	    Complex result
	}

	int getRecordCount(){
		return recordList.size()
	}
	
	Record getRecord(int index){
		if(index >= 0 && index < recordList.size())
	    {
	        return recordList.get(index)
	    }
	    else
	    {
	        return null
	    }
	}
	
	boolean saveRecord(){
		if(currentRecord != null && currentRecord.success)
	    {
	        recordList.add(currentRecord)
	        currentRecord = null
	        return true
	    }else{
	    	return False
	    }
	}
	
	CharSequence[] getRecordItems(){
		StandardFormatter formator = new StandardFormatter(systemContext)
		int record_count = getRecordCount()
		CharSequence items[] = new CharSequence[record_count]
		for(int i = 0 i < record_count ++i){
			Record record = getRecord(i)
			String recordString = formator.toString(record.result) + ":" + record.question
			items[i] = recordString
		}
		return items
	}
	
	boolean clearRecord(int index){
		if(index >= 0 && index < recordList.size())
	    {
	        recordList.remove(index)
	                                                               
	        return true
	    }
	    else
	    {
	        return False
	    }
	}
	
	boolean clearAllRecord(){
		recordList.clear()
	    return true
	}
	
	Context getSystemContext(){
    	return systemContext
    }
	
	String calculate(LinkedList<Token> tokenList){
		String result = new String()

	    String unknownToken = new String()
	    for(Token token : tokenList)
	    {
	        if(token.getType() == Token.EType.NoType)
	        {
	            if(unknownToken.length() > 0)
	            {
	                unknownToken += ","
	            }
	            unknownToken += token.getContent()
	        }
	    }
	    if(unknownToken.length() > 0)
	    {
	        currentRecord.success = false
	        return systemContext.getString(R_string.error_unknown_keyword) + unknownToken
	    }
	    
	    BuildContext bContext = new BuildContext(systemContext, constManager, tokenList)

	    Expr expr = AdditiveExpr.buildExpr(bContext)
	    if(expr != null){
	    	if(bContext.tokenList.size() > 0){
	    		String tokenString = new String()
	    		for(Token token : tokenList){
	    			if(tokenString.length() != 0){
	    				tokenString += ","
	    			}
	    			tokenString += token.getContent()
	    		}
	    		currentRecord.success = false
    	        result = systemContext.getString(R_string.error_unnecessary_keyword) + tokenString
	    	}else{
		        EvaluateContext eContext = new EvaluateContext(systemContext, this)
		        eContext.pushResult(Complex(0))
		        if(expr.evaluate(eContext))
		        {
		        	Complex value = eContext.popResult()
		        	result = eContext.getFormatter().toString(value)
		        	if(result != null){
		        		currentRecord.success = true
		        		currentRecord.result = value
		        	}else{
		        		currentRecord.success = false
		    	        result = systemContext.getString(R_string.error_invalid_input)
		        	}
		        }
		        else
		        {
		            currentRecord.success = false
		            result = eContext.getErrorMessage()
		        }
	    	}
	    }
	    else
	    {
	        currentRecord.success = false
	        result = bContext.errorMessage
	    }
	    return result
		
	}
	
	boolean isSuccess(){
		return currentRecord.success
	}
	
	private Record currentRecord
	private LinkedList<Record> recordList = new LinkedList<Record>()
}
