package calculator.xwg;

import android.content.Context;

public abstract class ComplexFormatter {
	
	static final double MIN_NUMBER = 1e-15;
	Context context;
	
	ComplexFormatter(Context _context){
		context = _context;
	}
	
	public String toString(Complex complex){return null;};
	
	public String toString(double value, int length){
		if(Math.abs(value) < MIN_NUMBER)
	    {
			value = 0;
	    }
		
		String format = "%." + String.format("%d", length) + "g";
		String real = String.format(format, value);
		
		//remove the 0 at the end of number.
		String before = null;
		String after = null;
		int e_index = real.indexOf("e");
		if(e_index != -1){
			before = real.substring(0, e_index);
			after = real.substring(e_index);
		}else{
			before = real;
		}
		int point_index = before.indexOf(".");
		if(point_index != -1){
			int index = before.length() - 1;
			while(index >= point_index && 
					(before.charAt(index) == '0' || before.charAt(index) == '.')){
				--index;
			}
			real = before.substring(0, index + 1);
		}else{
			real = before;
		}
		if(after != null){
			real += after;
		}
		return real;
	}
}
