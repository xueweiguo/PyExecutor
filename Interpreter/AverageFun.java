package calculator.xwg;

import java.util.LinkedList;

public class AverageFun extends CalculateFunction {
	String getName(){
		return "avg";
	}
	
	boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		if(paraList.size() == 0)
	    {
	        context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    Complex result = new Complex();
	    for(Complex c : paraList){
	    	result = Complex.add(result, c);
	    }
	    result = Complex.div(result, new Complex(paraList.size()));
	    context.setCurrentResult(result);
	    return checkResult(context);
	}
}
