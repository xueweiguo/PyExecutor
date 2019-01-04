package calculator.xwg;

import android.content.Context;

public class DegreesFormatter  extends ComplexFormatter {
	public DegreesFormatter(Context _context){
		super(_context);
	}
	
	public String toString(Complex complex){
		if(complex.i == 0){
			return  toString(StrictMath.toDegrees(complex.r), 12) + context.getText(R.string.character_degree);
		}else{
			RadiusAngleFormatter formatter = new RadiusAngleFormatter(context, true);
			return formatter.toString(complex);
		}
	}
}