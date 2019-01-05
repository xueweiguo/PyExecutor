



class SumFun (CalculateFunction):
	String getName(){
		return "sum"
	}
	
	boolean execute(self, paraList, context){
		if(len(paraList) == 0)
	    {
	        context.setErrorMessage(self.getName(), R_string.error_invalid_parameter_count)
	        return False
	    }
	    Complex result = Complex()
	    for(Complex c : paraList){
	    	result = Complex.add(result, c)
	    }
	    context.setCurrentResult(result)
	    return self.checkResult(context)
	}
}


