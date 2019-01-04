package calculator.xwg;

public class NumberExpr extends TerminalExpr
{
	static NumberExpr buildExpr(BuildContext context){
		String value = context.tokenList.removeFirst().getContent();
		Complex constValue = context.constManager.find(value);
		if(constValue != null){
			return new NumberExpr(constValue);
		}else{
			int index = value.indexOf("∠");
			if(index != -1){
				double radius = Double.valueOf(value.substring(0, index));
				double angle;
				if(value.substring(value.length() - 1).compareTo("°") == 0){
					double degrees = Double.valueOf(value.substring(index + 1, value.length() - 1));
					double cycles = StrictMath.floor(degrees / 360);
					if(degrees < 0){
						cycles += 1;
					}
					angle = StrictMath.toRadians(degrees - cycles * 360);
				}else{
					angle = Double.valueOf(value.substring(index + 1));
				}
				return new NumberExpr(new Complex(radius * StrictMath.cos(angle), radius * StrictMath.sin(angle)));
			}else if(value.substring(value.length() - 1).compareTo("i") == 0){
				if(value.length() == 1){
		            return new NumberExpr(new Complex(0, 1));
		        }else{
		        	return new NumberExpr(new Complex(0, Double.valueOf(value.substring(0, value.length() - 1))));
		        }
		    }else if(value.substring(value.length() - 1).compareTo("°") == 0){
		        return new NumberExpr(new Complex(StrictMath.toRadians(Double.valueOf(value.substring(0, value.length() - 1)))));
		    }else if(value.substring(value.length() - 1).compareTo("%") == 0){
		    	return new NumberExpr(new Complex(Double.valueOf(value.substring(0, value.length() - 1))/100));
		    }else{
		    	return new NumberExpr(new Complex(Double.valueOf(value)));
		    }
		}
	}
	public NumberExpr(Complex val){
		complex = val;
	}
	
	public boolean evaluate(EvaluateContext context){
		context.setCurrentResult(complex);
	    return true;
	}
	
	private Complex complex;
}