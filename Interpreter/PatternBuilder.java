

import java.util.Collections

import java.util.Set

class PatternBuilder {
	static String build(Set<String> set){
		String pattern = new String()
    	
		LinkedList<String> keyList = new LinkedList<String>()
        for(String key : set)
        {
        	keyList.add(key)
        }
        Collections.sort(keyList, Collections.reverseOrder())
        
        for(String key : keyList){
            if(pattern.length() > 0)
            {
            	pattern += "|"
            }
            pattern += key
        }
        return pattern
	}
}
