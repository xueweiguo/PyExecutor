package calculator.xwg;

public class Token
{
    enum EType
    {
        NoType,
        Operator,
        Parenthese,
        Comma,
        Number,
        Parameter,
        FunctionName
    }

    Token(EType type, String content){
    	mType = type;
    	mContent = content;
    }
    
    Token(String content){
    	mType = EType.NoType;
    	mContent = content;
    }
    EType getType(){
    	return mType;
    }
    String getContent(){
    	return mContent;
    }
    void setType(EType type){
    	mType = type;
    }
    boolean isNoType(){
    	return (mType == EType.NoType);
    }
    void setContent(String content){
    	mContent = content;
    }
    EType mType;
    String mContent;
};

