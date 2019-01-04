package calculator.xwg;

import java.util.LinkedList;

public class Log10Fun extends CalculateFunction {
	String getName(){
		return "log10";
	}
	
	boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		if(paraList.size() != 1)
	    {
	        context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    Complex para = paraList.getFirst();
	    if(para.r < 0)
	    {
	    	context.setErrorMessage(getName(), R.string.error_invalid_input);
	        return false;
	    }
	    if(para.i != 0)
	    {
	        context.setErrorMessage(getName(), R.string.error_invalid_date_type);
	        return false;
	    }
	    context.setCurrentResult(new Complex(Math.log10(para.r)));
	    return checkResult(context);
	}
}
