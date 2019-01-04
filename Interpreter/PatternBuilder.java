package calculator.xwg;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Set;

public class PatternBuilder {
	static public String build(Set<String> set){
		String pattern = new String();
    	
		LinkedList<String> keyList = new LinkedList<String>();
        for(String key : set)
        {
        	keyList.add(key);
        }
        Collections.sort(keyList, Collections.reverseOrder());
        
        for(String key : keyList){
            if(pattern.length() > 0)
            {
            	pattern += "|";
            }
            pattern += key;
        }
        return pattern;
	}
}
