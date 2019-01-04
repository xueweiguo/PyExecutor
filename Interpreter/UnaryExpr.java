package calculator.xwg;

public class UnaryExpr extends TerminalExpr{
	void setPrimaryExpr(Expr expr){
		primaryExpr = expr;
	}
	static Expr buildExpr(BuildContext context){
		int minusCount = 0;
	    while(context.tokenList.size() > 0 &&
	          context.tokenList.getFirst().getType() == Token.EType.Operator)
	    {
	        String content = context.tokenList.getFirst().getContent();
	        if(content.compareTo("-") == 0)// == "-")
	        {
	            ++minusCount;
	        }
	        else if(content.compareTo("+") != 0)// != "+")
	        {
	            context.errorMessage = "Invalid token:" + content;
	            return null;
	        }
	        context.tokenList.removeFirst();
	    }

	    if(context.tokenList.size() == 0)
	    {
	        context.errorMessage = "Expression is't complete";
	        return null;
	    }

	    Expr expr = PrimaryExpr.buildExpr(context);

	    if(expr == null) return null;

	    if((minusCount % 2) == 1)
	    {
	        UnaryExpr unary = new UnaryExpr();
	        unary.setPrimaryExpr(expr);
	        return unary;
	    }
	    else
	    {
	        return expr;
	    }
	}
	
	public boolean evaluate(EvaluateContext context){
		if(primaryExpr.evaluate(context))
	    {
			Complex result = context.popResult();
	        result.r = -result.r;
	        result.i = -result.i;
	        context.pushResult(result);
	        return true;
	    }
	    else
	    {
	        return false;
	    }
	}
	
	private Expr primaryExpr;
}