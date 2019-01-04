package calculator.xwg;

import java.util.LinkedList;

public class ConvertFormatFun extends CalculateFunction {
	public ConvertFormatFun(String name, ComplexFormatter formatter){
		funName = name;
		complexFormatter = formatter;
	}
	
	public String getName(){
		return funName;
	}
	
	public boolean execute(LinkedList<Complex> paraList, EvaluateContext context){
		if(paraList.size() != 1)
	    {
	        context.setErrorMessage(getName(), R.string.error_invalid_parameter_count);
	        return false;
	    }
	    Complex para = paraList.getFirst();
	    context.setCurrentResult(para);
	    context.setFormatter(complexFormatter);
	    return checkResult(context);
	}
	
	private String funName;
	private ComplexFormatter complexFormatter;
}
