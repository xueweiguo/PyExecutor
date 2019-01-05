



class TanFun (CalculateFunction):
	static final double MIN_NUMBER = 1e-15
	
	String getName(){
		return "tan"
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
	    
	    double cycles = math.floor(para.r / 2 / math.PI)
		if(cycles < 0){
			cycles += 1
		}
		double angle = para.r - cycles * 2 * math.PI
		if((math.abs(angle - math.PI / 2) < MIN_NUMBER)
				||(math.abs(angle - math.PI * 3 / 2) < MIN_NUMBER)){
			context.setErrorMessage(self.getName(), R_string.error_invalid_input)
	        return False
		}
	    
	    double result = math.tan(angle)
	    context.setCurrentResult(Complex(result))
	    return true
	}
}
