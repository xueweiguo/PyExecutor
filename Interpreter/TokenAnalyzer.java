package calculator.xwg;

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.regex.Matcher;

public class TokenAnalyzer
{
	class Context{
    	LinkedList<Token> tokenList;
        ListIterator<Token> it;
        TokenPattern pattern;
        String content;
    }
    
    void analyzeContent(Context context){
        Token token = context.it.next();
        context.it.previous();
        
        Matcher m = context.pattern.pattern.matcher(context.content); 
                
        if(m.find()){
        	int start = m.start();
        	int end = m.end();
            if(start > 0){
                context.it.add(new Token(context.content.substring(0, start)));
            }
            
            if(end < context.content.length()){
                context.it.add(new Token(context.pattern.type, context.content.substring(start, end)));
                context.content = context.content.substring(end, context.content.length());
                analyzeContent(context);
            }else{
                token.setContent(context.content.substring(start, end));
                token.setType(context.pattern.type);
                context.content = context.content.substring(end, context.content.length());
            }
        }
        else
        {
            token.setContent(context.content);
        }
    }
    
    LinkedList<Token> analyzeToken(String strInput, TokenPatternFactory factory){
        
    	LinkedList<TokenPattern> list = new LinkedList<TokenPattern>();
        factory.createPatterns(list);
        
        LinkedList<Token> tokenList = new LinkedList<Token>();
        tokenList.add(new Token(strInput));

        for(TokenPattern pattern:list){
            ListIterator<Token> it = tokenList.listIterator();
            while(it.hasNext()){
                Token token = it.next();
                it.previous();
                
                if(token.isNoType()){
                    String content = token.getContent();
                    Context context = new Context();
                    context.tokenList = tokenList;
                    context.it = it;
                    context.pattern = pattern;
                    context.content = content;
                    analyzeContent(context);
                }
                it.next();
            }
        }
        return tokenList;
    }
}


