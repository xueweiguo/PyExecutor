



class ConvertFormatFun (CalculateFunction):
	ConvertFormatFun(String name, ComplexFormatter formatter){
		funName = name
		complexFormatter = formatter
	}
	
	String getName(){
		return funName
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) != 1)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex para = paraList.getFirst()
	    context.setCurrentResult(para)
	    context.setFormatter(complexFormatter)
	    return self.checkResult(context)
	}
	
	private String funName
	private ComplexFormatter complexFormatter
}
