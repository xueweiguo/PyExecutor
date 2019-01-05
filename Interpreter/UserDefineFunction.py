

class UserDefineFunction extends CustomFunction{
	static final String PREFS_NAME = "CustomFunction"
	
	UserDefineFunction(String key, String name, String expr){
		super(name)
		functionKey = key
		functionExpr = expr
	}
	
	String getKey(){
		return functionKey
	}
	
	String getExprString(){
		return functionExpr
	}
	
	static UserDefineFunction load(Context context, String key){
		SharedPreferences settings = context.getSharedPreferences(PREFS_NAME, 0)
	    String funInfo = settings.getString(key, "")
	    
	    if(funInfo.length() == 0) return null
	    
	    int pre_expr = funInfo.indexOf(":")
	    if(pre_expr >= 1 && pre_expr < (funInfo.length() - 1)){ 
	    	// Must has name and expression
	    	return new UserDefineFunction(key, 
	    								funInfo.substring(0, pre_expr),
	    								funInfo.substring(pre_expr + 1))
	    }else{
	    	return null
	    }
	}
	
	static void clear(Context context, String key){
		SharedPreferences settings = context.getSharedPreferences(PREFS_NAME, 0)
		Editor editor = settings.edit()
		editor.putString(key, "")
		editor.commit()
	}
	
	void saveMe(Context context){
		SharedPreferences settings = context.getSharedPreferences(PREFS_NAME, 0)
		Editor editor = settings.edit()
		editor.putString(functionKey, getName() + ":" + functionExpr)
		editor.commit()
	    
	}
	
	private String functionKey
	private String functionExpr
}
