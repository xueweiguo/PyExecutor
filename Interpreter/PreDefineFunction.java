

class PreDefineFunction extends CustomFunction{
	private String exprString
	PreDefineFunction(String name, String expr){
		super(name)
		exprString = expr
	}
	
	String getExprString(){
		 return exprString
	}
}
