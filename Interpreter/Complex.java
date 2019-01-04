package calculator.xwg;

public class Complex {
	public Complex(){
		r = 0;
		i = 0;
	}
	public Complex(double _r){
		r = _r;
		i = 0;
	}
	
	public Complex(double _r, double _i){
		r = _r;
		i = _i;
	}
	
	public Complex(Complex other){
		r = other.r;
		i = other.i;
	}
	
	private void addBy(Complex other){
    	r += other.r;
        i += other.i;
    }
	
	public static Complex add(Complex c1, Complex c2){
		Complex result = new Complex(c1);
		result.addBy(c2);
		return result;
	}
	
	private void subBy(Complex other){
		r -= other.r;
	    i -= other.i;
	}
	public static Complex sub(Complex c1, Complex c2){
		Complex result = new Complex(c1);
		result.subBy(c2);
		return result;
	}
	
	private void mulBy(Complex other){
		if(i != 0 || other.i != 0)
	    {
	        double temp = r * other.r - i * other.i;
	        i = r * other.i + i * other.r;
	        r = temp;
	    }
	    else
	    {
	        r *= other.r;
	    }
	}
	public static Complex mul(Complex c1, Complex c2){
		Complex result = new Complex(c1);
		result.mulBy(c2);
		return result;
	}
	private void divBy(Complex other){
		if(i != 0 || other.i != 0)
	    {
	        double temp = (r * other.r + i * other.i)/(other.r * other.r + other.i * other.i);
	        i = (i * other.r - r * other.i)/(other.r * other.r + other.i * other.i);
	        r = temp;
	    }
	    else
	    {
	        r /= other.r;
	    }
	}
	public static Complex div(Complex c1, Complex c2){
		Complex result = new Complex(c1);
		result.divBy(c2);
		return result;
	}

	public double getAbs(){
		return Math.hypot(r, i);
	}
	
	double r;
	double i;
}

