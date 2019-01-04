package calculator.xwg;

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NonterminalExpr extends Expr{
	protected LinkedList<Expr> exprList = new LinkedList<Expr>();
    protected LinkedList<Token> operatorList = new LinkedList<Token>();
    
	public void appendExpr(Expr expr){
		exprList.add(expr);
	}
    void appendOperator(Token token){
    	operatorList.add(token);
    }

    abstract class ValueOperator
    {
    	ValueOperator(String string){
    		operatorString = string;
    	}
    	
        boolean evaluate(Complex value1, Complex value2){
        	return false; 
    	}
        
        public Complex getResult(){ 
        	return evaluateResult; 
    	}
        
        public int getErrorMessage(){
        	return errorMessage;
    	}
        
        String getOperatorString(){
        	return operatorString;
        }
        
        protected Complex evaluateResult = new Complex();
        protected int errorMessage = 0;
        protected String operatorString;
    }

    public boolean evaluate(EvaluateContext context){
    	if(exprList.size() - operatorList.size() != 1){
    		context.clearResult();
            context.setErrorMessage("Operator count and Expr count is not match.");;
            return false;
    	}
    	
    	ListIterator<Expr> expr_it = exprList.listIterator();

        context.pushResult(new Complex(0));

        if(!expr_it.next().evaluate(context)) return false;

        ListIterator<Token> operator_it = operatorList.listIterator();
        {
            while(expr_it.hasNext())
            {
            	Expr expr = expr_it.next();
            	Token token = operator_it.next();
            	
            	Complex res_prev = context.getCurrentResult();
                if(expr.evaluate(context)){
	                Complex res_cur = context.popResult();
	                ValueOperator valueOperator = getValueOperator(token.getContent());
	                if(valueOperator.evaluate(res_prev, res_cur))
	                {
	                    context.pushResult(valueOperator.getResult());
	                }
	                else
	                {
	                    context.clearResult();
	                    context.setErrorMessage(valueOperator.getOperatorString(), 
	                    						valueOperator.getErrorMessage());
	                    return false;
	                }
                }else{
                	return false;
                }
            }
            context.setCurrentResult(context.popResult());
            return true;
        }
    }
    public ValueOperator getValueOperator(String operatorContent){ return null; }
    
    interface ChildExprBuildProxy{
		Expr buildExpr(BuildContext context);
	}
	
	interface ParentCreater {
		NonterminalExpr newInstance();
	}
	
	public static Expr buildExpr(ChildExprBuildProxy proxy, ParentCreater creator, 
							BuildContext context, String operatorRegex){
	    Expr firstExpr = proxy.buildExpr(context);
	
	    if(firstExpr == null) return null;

	    if(context.tokenList.size() == 0) return firstExpr;
	
	    Token token = context.tokenList.getFirst();
	
	    if((token.getType() != Token.EType.Operator)
	       && (token.getType() != Token.EType.Parenthese)
	       && (token.getType() != Token.EType.Comma)){
	        context.errorMessage = "Invalid token";
	        return null;
	    }
	
	    String content = token.getContent();
	    Pattern pattern = Pattern.compile(operatorRegex);
	    Matcher m = pattern.matcher(content);
	    if(!m.matches()) return firstExpr;

	    NonterminalExpr parentExpr = creator.newInstance();
	    parentExpr.appendExpr(firstExpr);
	    parentExpr.appendOperator(token);
	    context.tokenList.removeFirst();
	    while(true)
	    {
	        Expr expr = proxy.buildExpr(context);

	        if(expr == null) break;

	        parentExpr.appendExpr(expr);

	        if(context.tokenList.size() == 0) return parentExpr;

	        token = context.tokenList.getFirst();

	        if((token.getType() != Token.EType.Operator)
	             && (token.getType() != Token.EType.Parenthese))
	        {
	            return parentExpr;
	        }

	        content = token.getContent();
		    pattern = Pattern.compile(operatorRegex);
		    m = pattern.matcher(content);
		    if(!m.matches()) return parentExpr;
	
		    parentExpr.appendOperator(token);
	        context.tokenList.removeFirst();

	        if(context.tokenList.size() == 0)
	        {
	            context.errorMessage = "Expression is't complete";
	            break;
	        }
	    }
		return null;
	}
}





