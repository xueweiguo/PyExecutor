from Framework.JsonAdapter import *
from FunctionBlock.FbdComponentFactory import *
from FunctionBlock.FbdBuilderFactory import *


FactoryManager().register('Function Block Diagram', 'element', FbdComponentFactory())
FactoryManager().register('Function Block Diagram', 'builder', FbdBuilderFactory())
JsonAdapter().register_serializable(FbdStrategy)
JsonAdapter().register_serializable(Generator)
JsonAdapter().register_serializable(Filter)
JsonAdapter().register_serializable(CommPort)
JsonAdapter().register_serializable(DataPacker)
