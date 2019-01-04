package calculator.xwg;

import java.util.LinkedList;

public class SumFun extends CalculateFunction {
	String getName(){
		return "sum";
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
	    context.setCurrentResult(result);
	    return checkResult(context);
	}
}


