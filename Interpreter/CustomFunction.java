package calculator.xwg;

import java.util.LinkedList;

public class CustomFunction extends CalculateFunction {
	
	protected String funName; 
	CustomFunction(String name){
		funName = name;
	}
	String getName(){
		return funName;
	}
	
	public String getExprString(){ return null; }
	
	boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		String functionString = getExprString();
	    
	    if(functionString == null || functionString.length() == 0){
	    	context.setErrorMessage(getName(), R.string.error_undefined_custom_function);
	        return false;
	    }
	    
	    CalculateEngine engine = context.getCalculateEngine();
	    
	    LinkedList<Token> tokenList = engine.analyzeToken(functionString);
	    
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
	    	context.setErrorMessage(context.getSystemContext().getText(R.string.error_invalid_token) + " in " + getName() + ":" + unknownToken);
	        return false; 
	    }
	    	    
	    BuildContext bContext = new BuildContext(engine.getSystemContext(), 
	    										engine.getConstManager(), 
	    										tokenList);

	    Expr expr = AdditiveExpr.buildExpr(bContext);
	    if(expr != null){
	        EvaluateContext eContext = new EvaluateContext(context);
	        eContext.pushResult(new Complex(0));
	        
	        if(!eContext.pushCustomCall(getName(), paraList)){
	        	context.setErrorMessage(eContext.getErrorMessage());
	        	return false;
	        }
	        boolean success = expr.evaluate(eContext);
	        eContext.popCustomCall();
	        if(success)
	        {
	        	context.setCurrentResult(eContext.popResult());
	        	context.setFormatter(eContext.getFormatter());
	        	return true;
	        }else{
	        	context.setErrorMessage(eContext.getErrorMessage());
	        	return false;
	        }
	    }
	    else
	    {
	    	context.setErrorMessage(bContext.errorMessage);
	    	return false;
	    }
	}
}
