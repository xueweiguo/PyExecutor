



class LogeFun (CalculateFunction):
	String getName(){
		return "loge"
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) != 1)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex para = paraList.getFirst()
	    if(para.r < 0)
	    {
	    	context.setErrorMessage(self.getName(), R_string.error_invalid_input)
	        return False
	    }
	    if(para.i != 0)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
	        return False
	    }
	    context.setCurrentResult(Complex(math.log(para.r)))
	    return self.checkResult(context)
	}
}
