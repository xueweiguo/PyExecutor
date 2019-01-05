



class PowerFun (CalculateFunction):
	String getName(){
		return "pow"
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) != 2)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex x = paraList.removeFirst()
	    if(x.i != 0)
	    {
	    	context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
	        return False
	    }
	    Complex y = paraList.removeFirst()
	    if(y.i != 0)
	    {
	    	context.setErrorMessage(self.getName(), R_string.error_invalid_date_type)
	        return False
	    }
	    context.setCurrentResult(Complex(math.pow(x.r, y.r)))
	    return self.checkResult(context)
	}
}
