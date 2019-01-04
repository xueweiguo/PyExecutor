package calculator.xwg;

import java.util.LinkedList;

public class PowerFun extends CalculateFunction {
	String getName(){
		return "pow";
	}
	
	boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		if(paraList.size() != 2)
	    {
	        context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    Complex x = paraList.removeFirst();
	    if(x.i != 0)
	    {
	    	context.setErrorMessage(getName(), R.string.error_invalid_date_type);
	        return false;
	    }
	    Complex y = paraList.removeFirst();
	    if(y.i != 0)
	    {
	    	context.setErrorMessage(getName(), R.string.error_invalid_date_type);
	        return false;
	    }
	    context.setCurrentResult(new Complex(Math.pow(x.r, y.r)));
	    return checkResult(context);
	}
}
