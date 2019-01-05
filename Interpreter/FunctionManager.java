

import java.util.HashMap
import java.util.Set

import android.content.Context

class FunctionManager {
	Context systemContext
	
	FunctionManager(Context context){
		systemContext = context
	}
	
	boolean registerFunction(CalculateFunction fun){
		if(functionMap.get(fun.getName()) == null)
	    {
	       functionMap.put(fun.getName(), fun)
	       return true
	    }
	    else
	    {
	        return False
	    }
	}
	
	int registerUserDefineFunction(String key, String funName, String funText){
		CalculateFunction fun = getFunction(funName)
		
		if(fun != null){
			if(fun.getClass().getSimpleName().compareTo("UserDefineFunction") != 0){
				//Has been registered as a system function.
				return R_string.error_used_fun_name
			}
			UserDefineFunction udf = (UserDefineFunction)fun
			if(udf.getKey().compareTo(key) != 0){
				//The name has been used by other UserDefineFunctio.
				return R_string.error_used_fun_name
			}
			functionMap.remove(udf.getName())
			userDefineMap.remove(key)
		}
		
		//Now, we can register the UserdefineFunction safety.
		UserDefineFunction udf_new = new UserDefineFunction(key, funName, funText)
		udf_new.saveMe(systemContext)
		return registerUserDefineFunction(udf_new)
	}
	
	int registerUserDefineFunction(UserDefineFunction udf){
		userDefineMap.put(udf.getKey(), udf)
		functionMap.put(udf.getName(), udf)
		return 0
	}
	
	UserDefineFunction getUserDefineFunction(String key){
		return userDefineMap.get(key)
	}
	
	Set<String> functions(){
		return functionMap.keySet()
	}
	
	CalculateFunction getFunction(String name){
		return functionMap.get(name)
	}
	
	private HashMap<String, CalculateFunction> functionMap = new HashMap<String, CalculateFunction>()
	private HashMap<String, UserDefineFunction> userDefineMap = new HashMap<String, UserDefineFunction>()
}
