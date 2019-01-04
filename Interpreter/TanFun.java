package calculator.xwg;

import java.util.LinkedList;

public class TanFun extends CalculateFunction {
	static final double MIN_NUMBER = 1e-15;
	
	String getName(){
		return "tan";
	}
	
	boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		if(paraList.size() != 1)
	    {
			context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    Complex para = paraList.getFirst();
	    if(para.i != 0)
	    {
	    	context.setErrorMessage(getName(), R.string.error_invalid_date_type);
	        return false;
	    }
	    
	    double cycles = StrictMath.floor(para.r / 2 / StrictMath.PI);
		if(cycles < 0){
			cycles += 1;
		}
		double angle = para.r - cycles * 2 * StrictMath.PI;
		if((StrictMath.abs(angle - StrictMath.PI / 2) < MIN_NUMBER)
				||(StrictMath.abs(angle - StrictMath.PI * 3 / 2) < MIN_NUMBER)){
			context.setErrorMessage(getName(), R.string.error_invalid_input);
	        return false;
		}
	    
	    double result = Math.tan(angle);
	    context.setCurrentResult(new Complex(result));
	    return true;
	}
}
