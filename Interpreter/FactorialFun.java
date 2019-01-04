package calculator.xwg;

import java.util.LinkedList;

public class FactorialFun extends CalculateFunction {
	String getName(){
		return "n!";
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
	    if(para.r < 1 || para.r != StrictMath.floor(para.r))
	    {
	    	context.setErrorMessage(getName(), R.string.error_invalid_input);
	        return false;
	    }
	    
	    double result = 1;
	    for(int i = 1; i <= (int)para.r; ++i){
	    	result *= i;
	    }
	    context.setCurrentResult(new Complex(result));
	    return true;
	}
}
