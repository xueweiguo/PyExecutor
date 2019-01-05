



class FactorialFun (CalculateFunction):
	String getName(){
		return "n!"
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) != 1)
	    {
			context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex para = paraList.getFirst()
	    if(para.i != 0)
	    {
	    	context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
	        return False
	    }
	    if(para.r < 1 || para.r != math.floor(para.r))
	    {
	    	context.setErrorMessage(self.getName(), R_string.error_invalid_input)
	        return False
	    }
	    
	    double result = 1
	    for(int i = 1 i <= (int)para.r ++i){
	    	result *= i
	    }
	    context.setCurrentResult(Complex(result))
	    return true
	}
}
