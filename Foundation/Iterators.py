from collections import Iterable,Iterator
from itertools import *
from Framework.DictProxy import *


def type_filter(it, object_type):
    return filter(lambda o: isinstance(o, object_type), it)


def name_filter(it, object_name):
    return filter(lambda o: o.name == object_name, it)

