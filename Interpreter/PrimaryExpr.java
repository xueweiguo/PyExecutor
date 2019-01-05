

class PrimaryExpr extends TerminalExpr
{
	static Expr buildExpr(BuildContext context){
		if(context.tokenList.size() == 0){
	        context.errorMessage = "Expression is't complete"
	        return null
	    }
    	
		Token token = context.tokenList.getFirst()
    	
	    switch(token.getType())
	    {
	    case Number:
	        return NumberExpr.buildExpr(context)
	    case Parenthese:
	    	if(token.getContent().compareTo("(") == 0)
	        {
	            context.tokenList.removeFirst()
	            
	            Expr expr = AdditiveExpr.buildExpr(context)
	            if(expr == null) return null
	            
	            if(context.tokenList.size() > 0){
	            	token = context.tokenList.removeFirst()
		            if(token.getType() == TokenType.Parenthese && token.getContent().compareTo(")") == 0)
		            {
		                return expr
		            }
	            }
	            context.errorMessage = "\')\'is necessary"
	            return null
	        }
	        else
	        {
	            context.errorMessage = "\'(\'is necessary"
	            return null
	        }
	    case FunctionName:
	        return FunctionExpr.buildExpr(context)
	    case Parameter:
	    	return ParameterExpr.buildExpr(context)
	    default:
	    	context.errorMessage = context.getSystemContext().getText(R_string.error_invalid_input).toString()
	        return null
	    }
	}
}
