package calculator.xwg;

import java.util.LinkedList;

public class AtanhFun extends CalculateFunction {
	String getName(){
		return "atanh";
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
	        context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    context.setCurrentResult(new Complex((Math.log(1 + para.r) - Math.log(1 - para.r)) / 2));
	    return checkResult(context);
	}
}