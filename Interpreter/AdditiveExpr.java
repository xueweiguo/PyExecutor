package calculator.xwg;

public class AdditiveExpr extends NonterminalExpr {
	static Expr buildExpr(BuildContext context){
		class MyProxy implements ChildExprBuildProxy{
			public Expr buildExpr(BuildContext context){
				return MultiplicativeExpr.buildExpr(context);
			}
		} 
		
		class MyCreater implements ParentCreater {
			public NonterminalExpr newInstance(){
				return new AdditiveExpr();
			}
		}
		return buildExpr(new MyProxy(), new MyCreater(), context, "[-+]");
    }
	public ValueOperator getValueOperator(String operatorContent){
    	class MyOperator extends ValueOperator
        {
	        public MyOperator(String _operatorString){
	    		super(_operatorString);
	    	}
            public boolean evaluate(Complex value1, Complex value2)
            {
                if(operatorString.compareTo("+") == 0)
                {
                    evaluateResult = Complex.add(value1, value2);
                    return true;
                }
                else// if(operatorString.compareTo("-") == 0)
                {
                	evaluateResult = Complex.sub(value1, value2);
                    return true;
                }
            }
        };
        return new MyOperator(operatorContent);
    }
}
