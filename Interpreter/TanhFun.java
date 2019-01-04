package calculator.xwg;

import java.util.LinkedList;

public class TanhFun extends CalculateFunction {
	String getName(){
		return "tanh";
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
	    double result = Math.tanh(para.r);
	    context.setCurrentResult(new Complex(result));
	    return true;
	}
}