from Framework.FactoryManager import FactoryManager
from Framework.JsonAdapter import JsonAdapter
from FunctionBlock.FbdComponentFactory import FbdComponentFactory, \
    FbdStrategy, Generator, Filter, CommPort, DataPacker
from FunctionBlock.FbdBuilderFactory import FbdBuilderFactory


def fbd_register():
    FactoryManager().register('Function Block Diagram', 'element', FbdComponentFactory())
    FactoryManager().register('Function Block Diagram', 'builder', FbdBuilderFactory())
    JsonAdapter().register_serializable(FbdStrategy)
    JsonAdapter().register_serializable(Generator)
    JsonAdapter().register_serializable(Filter)
    JsonAdapter().register_serializable(CommPort)
    JsonAdapter().register_serializable(DataPacker)
