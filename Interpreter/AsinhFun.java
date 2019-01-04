package calculator.xwg;

import java.util.LinkedList;

public class AsinhFun extends CalculateFunction {
	String getName(){
		return "asinh";
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
	    context.setCurrentResult(new Complex(Math.log(para.r + Math.sqrt(1 + para.r * para.r))));
	    return checkResult(context);
	}
}