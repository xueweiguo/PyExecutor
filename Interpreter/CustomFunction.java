



class CustomFunction (CalculateFunction):
	
	protected String funName
	CustomFunction(String name){
		funName = name
	}
	String getName(){
		return funName
	}
	
	String getExprString(){ return null }
	
	boolean execute(self, paraList, context){
		String functionString = getExprString()
	    
	    if(functionString == null || functionString.length() == 0){
	    	context.setErrorMessage(self.getName(), R_string.error_undefined_custom_function)
	        return False
	    }
	    
	    CalculateEngine engine = context.getCalculateEngine()
	    
	    LinkedList<Token> tokenList = engine.analyzeToken(functionString)
	    
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
	    	context.setErrorMessage(context.getSystemContext().getText(R_string.error_invalid_token) + " in " + getName() + ":" + unknownToken)
	        return False
	    }
	    	    
	    BuildContext bContext = new BuildContext(engine.getSystemContext(), 
	    										engine.getConstManager(), 
	    										tokenList)

	    Expr expr = AdditiveExpr.buildExpr(bContext)
	    if(expr != null){
	        EvaluateContext eContext = new EvaluateContext(context)
	        eContext.pushResult(Complex(0))
	        
	        if(!eContext.pushCustomCall(self.getName(), paraList)){
	        	context.setErrorMessage(eContext.getErrorMessage())
	        	return False
	        }
	        boolean success = expr.evaluate(eContext)
	        eContext.popCustomCall()
	        if(success)
	        {
	        	context.setCurrentResult(eContext.popResult())
	        	context.setFormatter(eContext.getFormatter())
	        	return true
	        }else{
	        	context.setErrorMessage(eContext.getErrorMessage())
	        	return False
	        }
	    }
	    else
	    {
	    	context.setErrorMessage(bContext.errorMessage)
	    	return False
	    }
	}
}
