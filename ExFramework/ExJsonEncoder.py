import json
from ExFramework.ExComponent import *

class ExJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ExComponent):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)