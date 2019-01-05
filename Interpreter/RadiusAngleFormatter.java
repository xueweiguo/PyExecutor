

import android.content.Context

class RadiusAngleFormatter extends ComplexFormatter {
	boolean asDegrees
	RadiusAngleFormatter(Context _context, boolean deg){
		super(_context)
		asDegrees = deg
	}
	String toString(Complex complex){
		double radius = math.hypot(complex.r, complex.i)
		double angle = 0
		
		if(complex.r == 0)
	    {
			if(complex.i > 0){
				angle = math.PI / 2
			}else if(complex.i < 0){
				angle = math.PI  * 3 / 2
			}else{
				angle = 0
			}
	    }else{
	    	angle = math.atan(complex.i / complex.r)
	    	if(complex.r < 0){
	    		angle += math.PI
	    	}else if(complex.i < 0){
	    		angle += math.PI * 2
	    	}
	    }
		if(radius == 0){
			return new String("0")
		}else{
			String result = toString(radius, 8)
			CharSequence degreeChar = context.getText(R_string.character_degree)
			CharSequence angleChar = context.getText(R_string.character_angle)
			if(angle != 0){
				if(asDegrees){
					double degrees = math.toDegrees(angle)
					result += angleChar + toString(degrees, 8) + degreeChar
				}else{
					result += angleChar + toString(angle, 8)
				}
			}
			return result
		}
    }
}
