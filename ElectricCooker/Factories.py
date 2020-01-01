from Framework.FactoryManager import FactoryManager
from ElectricCooker.EcComponentFactory import EcComponentFactory


def ecd_register():
    FactoryManager().register('Electric Appliance Control', 'element', EcComponentFactory())