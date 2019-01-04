package calculator.xwg;

import java.util.LinkedList;

public abstract class CalculateFunction {
	CalculateFunction(){
		
	}
	
	boolean checkResult(EvaluateContext context){
		if(context.getCurrentResult().r == Double.NaN){
			context.setErrorMessage(getName(), R.string.error_mathmatic_error);
			return false;
		}
		return true;
    }
    String getName(){ return ""; }
   
    boolean execute(LinkedList<Complex> paraList, EvaluateContext context){ return false; }
}
