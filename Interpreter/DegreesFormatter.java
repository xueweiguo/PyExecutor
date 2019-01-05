

import android.content.Context

class DegreesFormatter  extends ComplexFormatter {
	DegreesFormatter(Context _context){
		super(_context)
	}
	
	String toString(Complex complex){
		if(complex.i == 0){
			return  toString(math.toDegrees(complex.r), 12) + context.getText(R_string.character_degree)
		}else{
			RadiusAngleFormatter formatter = new RadiusAngleFormatter(context, true)
			return formatter.toString(complex)
		}
	}
}