package calculator.xwg;

import java.util.LinkedList;

import android.content.Context;

public class BuildContext
{
    public BuildContext(Context context, ConstManager _manager, LinkedList<Token> list){
    	systemContext = context;
    	constManager = _manager;
    	tokenList = list;
    	
    }
    public Context getSystemContext(){
    	return systemContext;
    }
    Context systemContext;
    ConstManager constManager;
    LinkedList<Token> tokenList = new LinkedList<Token>();
    String errorMessage;
}
