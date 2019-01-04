package calculator.xwg;

import android.content.Context;

public class RadiusAngleFormatter extends ComplexFormatter {
	boolean asDegrees;
	RadiusAngleFormatter(Context _context, boolean deg){
		super(_context);
		asDegrees = deg;
	}
	public String toString(Complex complex){
		double radius = StrictMath.hypot(complex.r, complex.i);
		double angle = 0;
		
		if(complex.r == 0)
	    {
			if(complex.i > 0){
				angle = Math.PI / 2;
			}else if(complex.i < 0){
				angle = Math.PI  * 3 / 2;
			}else{
				angle = 0;
			}
	    }else{
	    	angle = StrictMath.atan(complex.i / complex.r);
	    	if(complex.r < 0){
	    		angle += StrictMath.PI;
	    	}else if(complex.i < 0){
	    		angle += StrictMath.PI * 2;
	    	}
	    }
		if(radius == 0){
			return new String("0");
		}else{
			String result = toString(radius, 8);
			CharSequence degreeChar = context.getText(R.string.character_degree);
			CharSequence angleChar = context.getText(R.string.character_angle);
			if(angle != 0){
				if(asDegrees){
					double degrees = StrictMath.toDegrees(angle);
					result += angleChar + toString(degrees, 8) + degreeChar;
				}else{
					result += angleChar + toString(angle, 8);
				}
			}
			return result;
		}
    }
}
