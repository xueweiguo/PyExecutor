

import java.util.Set
import java.util.TreeMap

class ConstManager {
	TreeMap<String, Complex> constMap = new TreeMap<String, Complex>()
	
	void registerConst(String key, Complex value){
		constMap.put(key, value)
	}
	
	Set<String> consts(){
		return constMap.keySet()
	}
	
	Complex find(String key){
		return constMap.get(key)
	}
	
	int getConstCount(){
		return constMap.size()
	}
}
