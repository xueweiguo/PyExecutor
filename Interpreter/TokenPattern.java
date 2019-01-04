package calculator.xwg;
import java.util.regex.Pattern;

public class TokenPattern
{
    TokenPattern(Token.EType _type, String _pattern){
    	pattern = Pattern.compile(_pattern);
    	type = _type;
    }
    
    Pattern pattern;
    Token.EType type;
}