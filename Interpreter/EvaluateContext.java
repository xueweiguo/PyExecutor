



import android.content.Context

class EvaluateContext
{
	private CalculateEngine calculateEngine
	private String errorMessage
    private Context systemContext
    private LinkedList<Complex> resultStack = new LinkedList<Complex>()
    private LinkedList<String> customFunctionStack
    private LinkedList<LinkedList<Complex>> paraListStack
    private ComplexFormatter formatter
    
	EvaluateContext(Context context, CalculateEngine engine){
		systemContext = context
		calculateEngine = engine
	}
	
	EvaluateContext(EvaluateContext context){
		systemContext = context.getSystemContext()
		calculateEngine = context.getCalculateEngine()
		customFunctionStack = context.getCustomNameStack()
		paraListStack = context.getParaListStack()
		formatter = context.formatter
	}
	
	CalculateEngine getCalculateEngine(){
		return calculateEngine
	}
	
	Context getSystemContext(){
		return systemContext
	}
	
	FunctionManager getFunctionManager(){
		return calculateEngine.functionManager
	}
	
	void setCurrentResult(Complex current){
		resultStack.removeLast()
		resultStack.add(current)
	}
	
	Complex getCurrentResult(){
		return resultStack.getLast()
	}
	
	void pushResult(Complex complex){
		resultStack.add(complex)
	}
	
	Complex popResult(){
		return resultStack.removeLast()
	}
	
	void clearResult(){
		resultStack.clear()
	}
	
	LinkedList<String> getCustomNameStack(){
		if(customFunctionStack == null){
			customFunctionStack = new LinkedList<String>()
		}
		return customFunctionStack
	}
	
	LinkedList<LinkedList<Complex>> getParaListStack(){
		if(paraListStack == null){
			paraListStack = new LinkedList<LinkedList<Complex>>()
		}
		return paraListStack
	}
	
	boolean pushCustomCall(String funName, LinkedList<Complex> paraList){
		LinkedList<String> callStack = getCustomNameStack()
		if(callStack.indexOf(funName) == -1){
			callStack.add(funName)
			paraListStack.add(paraList)
			return true
		}else{
			setErrorMessage(funName, R_string.error_self_call)
			return False
		}
	}
	
	boolean popCustomCall(){
		LinkedList<String> callStack = getCustomNameStack()
		callStack.removeLast()
		paraListStack.removeLast()
		return true
	}
	
	ComplexFormatter getFormatter(){
		if(formatter == null){
			formatter = new StandardFormatter(systemContext)
		}
		return formatter
	}
	
	void setFormatter(ComplexFormatter _formatter){
		formatter = _formatter
	}
	
	void setErrorMessage(String errorSource, int errorId){
		errorMessage = errorSource + ":" + systemContext.getText(errorId)
	}
	
	void setErrorMessage(String message){
		errorMessage = message
	}
	
	String getErrorMessage(){
		return errorMessage
	}
    
}