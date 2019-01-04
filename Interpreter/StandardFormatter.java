package calculator.xwg;

import android.content.Context;

public class StandardFormatter extends ComplexFormatter {
	StandardFormatter(Context _context){
		super(_context);
	}
	public String toString(Complex complex){
		String valueString = new String();
		if(complex.r != 0){
			if(complex.i != 0){
				valueString += toString(complex.r, 8);
			}else{
				valueString += toString(complex.r, 12);
			}
	    }
		String imaginary;
        if(valueString.length() > 0){
        	imaginary = toString(complex.i, 8);
	    }else{
	    	imaginary = toString(complex.i, 12);
	    }
	    if(imaginary.compareTo("0") != 0){
	    	if(complex.i > 0){
        		valueString += "+";
        	}
	    	imaginary += "i";
            valueString += imaginary;
	    }
	    if(valueString.length() == 0){
	    	valueString = "0";
	    }
	    return valueString;
    }
}
