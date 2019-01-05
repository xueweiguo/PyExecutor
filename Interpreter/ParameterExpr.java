



class ParameterExpr extends TerminalExpr
{
	static ParameterExpr buildExpr(BuildContext context){
		Token token = context.tokenList.removeFirst()
		return new ParameterExpr(Integer.valueOf(token.getContent().substring(1)))
	}
	ParameterExpr(int number){
		paraNumber = number
	}
	
	boolean evaluate(EvaluateContext context){
		LinkedList<String> customNameList = context.getCustomNameStack()
		if(customNameList.size() > 0){
			LinkedList<Complex> paraList = context.getParaListStack().getLast()
			String funName = customNameList.getLast()
			Complex para = paraList.get(paraNumber - 1)
			if(para != null){
				context.setCurrentResult(para)
				return true
			}else{
				context.setErrorMessage(funName, R_string.error_invalid_parameter_count)
				return False
			}
		}else{
			String para = String.format("#%d", paraNumber)
			context.setErrorMessage(para, R_string.error_invalid_input)
			return False
		}
	}
	
	private int paraNumber
}