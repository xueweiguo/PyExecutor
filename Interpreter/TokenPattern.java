
import java.util.regex.Pattern

class TokenPattern
{
    TokenPattern(TokenType _type, String _pattern){
    	pattern = Pattern.compile(_pattern)
    	type = _type
    }
    
    Pattern pattern
    TokenType type
}