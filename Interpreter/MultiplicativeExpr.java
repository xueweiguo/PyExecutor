package calculator.xwg;

public class MultiplicativeExpr  extends NonterminalExpr {
	static Expr buildExpr(BuildContext context){
		class MyProxy implements ChildExprBuildProxy{
			public Expr buildExpr(BuildContext context){
				return RadiusAngleExpr.buildExpr(context);
			}
		} 
		class MyCreater implements ParentCreater {
			public NonterminalExpr newInstance(){
				return new MultiplicativeExpr();
			}
		}
		
		return buildExpr(new MyProxy(), new MyCreater(), context, "[×/]");
    }
	public ValueOperator getValueOperator(String operatorContent){
    	class MyOperator extends ValueOperator
        {
	        public MyOperator(String _operatorString){
	        	super(_operatorString);
	    	}
            public boolean evaluate(Complex value1, Complex value2)
            {
                if(operatorString.compareTo("×") == 0)
                {
                    evaluateResult = Complex.mul(value1, value2);
                    return true;
                }
                else{		//operatorString.compareTo("/") == 0
                	evaluateResult = Complex.div(value1, value2);
                    return true;
                }
            }
        };
        return new MyOperator(operatorContent);
    }
}

