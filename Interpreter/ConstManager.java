package calculator.xwg;

import java.util.Set;
import java.util.TreeMap;

public class ConstManager {
	TreeMap<String, Complex> constMap = new TreeMap<String, Complex>();
	
	public void registerConst(String key, Complex value){
		constMap.put(key, value);
	}
	
	Set<String> consts(){
		return constMap.keySet();
	}
	
	public Complex find(String key){
		return constMap.get(key);
	}
	
	int getConstCount(){
		return constMap.size();
	}
}
