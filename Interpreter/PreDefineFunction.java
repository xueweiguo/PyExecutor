package calculator.xwg;

public class PreDefineFunction extends CustomFunction{
	private String exprString; 
	public PreDefineFunction(String name, String expr){
		super(name);
		exprString = expr;
	}
	
	public String getExprString(){
		 return exprString;
	}
}
